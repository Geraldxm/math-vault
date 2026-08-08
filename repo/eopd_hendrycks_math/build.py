#!/usr/bin/env python3
"""Build the EOPD/verl training parquet from normalized MATH train data."""

import hashlib
import json
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / "derived/hendrycks_math/train.jsonl"
OUTPUT = HERE / "train.parquet"
EXPECTED_ROWS = 7_500
SOURCE_SHA256 = "9079588d96e75288cbeb557cdd2212dcf8949629f346d3a1615dcf3632bc2ac5"
PROMPT_SUFFIX = r" Please reason step by step, and put your final answer within \boxed{{}}."
SCHEMA = pa.schema(
    [
        ("data_source", pa.string()),
        ("prompt", pa.list_(pa.struct([("content", pa.string()), ("role", pa.string())]))),
        ("ability", pa.string()),
        ("reward_model", pa.struct([("ground_truth", pa.string()), ("style", pa.string())])),
        ("extra_info", pa.struct([("index", pa.string())])),
    ]
)


def build() -> None:
    if hashlib.sha256(SOURCE.read_bytes()).hexdigest() != SOURCE_SHA256:
        raise ValueError("unexpected normalized MATH train contents")
    rows = [json.loads(line) for line in SOURCE.open(encoding="utf-8")]
    if len(rows) != EXPECTED_ROWS or len({row["id"] for row in rows}) != EXPECTED_ROWS:
        raise ValueError("unexpected normalized MATH train contents")

    eopd_rows = [
        {
            "data_source": "hendrycks_math",
            "prompt": [{"content": row["problem"] + PROMPT_SUFFIX, "role": "user"}],
            "ability": "MATH",
            "reward_model": {"ground_truth": row["answer"] or "", "style": "rule-lighteval/MATH_v2"},
            "extra_info": {"index": row["id"]},
        }
        for row in rows
    ]
    temporary = OUTPUT.with_suffix(".parquet.tmp")
    try:
        pq.write_table(pa.Table.from_pylist(eopd_rows, schema=SCHEMA), temporary, compression="snappy")
        written = pq.read_table(temporary)
        if written.num_rows != EXPECTED_ROWS or not written.schema.equals(SCHEMA):
            raise ValueError("parquet verification failed")
        temporary.replace(OUTPUT)
    finally:
        temporary.unlink(missing_ok=True)
    print(f"train.parquet: {EXPECTED_ROWS} rows sha256={hashlib.sha256(OUTPUT.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    build()

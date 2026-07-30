import hashlib
import json
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / "derived/dapo_math_17k_dedup/train.jsonl"
OUTPUT = HERE / "train.parquet"
SOURCE_SHA256 = "7131540f334375c5fed33ac89b8728cdda851bde9ee95a755d74a33b201d8b25"
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


def build():
    source_bytes = SOURCE.read_bytes()
    if hashlib.sha256(source_bytes).hexdigest() != SOURCE_SHA256:
        raise ValueError("unexpected dedup source contents")

    source_rows = [json.loads(line) for line in source_bytes.splitlines()]
    if len(source_rows) != 17_176:
        raise ValueError("unexpected dedup row count")
    if len({" ".join(row["problem"].split()) for row in source_rows}) != len(source_rows):
        raise ValueError("duplicate normalized problems remain")

    rows = [
        {
            "data_source": "math_dapo",
            "prompt": [{"content": row["problem"] + PROMPT_SUFFIX, "role": "user"}],
            "ability": "MATH",
            "reward_model": {
                "ground_truth": str(row["answer"]),
                "style": "rule-lighteval/MATH_v2",
            },
            "extra_info": {"index": row["id"]},
        }
        for row in source_rows
    ]
    table = pa.Table.from_pylist(rows, schema=SCHEMA)
    temporary = OUTPUT.with_suffix(".parquet.tmp")
    try:
        pq.write_table(table, temporary, compression="snappy")
        written = pq.read_table(temporary)
        if written.num_rows != len(rows) or not written.schema.equals(SCHEMA):
            raise ValueError("parquet verification failed")
        temporary.replace(OUTPUT)
    finally:
        temporary.unlink(missing_ok=True)

    print(f"wrote {len(rows):,} rows to {OUTPUT}")
    print(f"sha256 {hashlib.sha256(OUTPUT.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    build()

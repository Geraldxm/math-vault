#!/usr/bin/env python3
"""Make the EOPD/DAPO training JSON from normalized Hendrycks MATH."""

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "train.jsonl"
OUTPUT = HERE / "eopd_train.json"
SOURCE_SHA256 = "9079588d96e75288cbeb557cdd2212dcf8949629f346d3a1615dcf3632bc2ac5"
PROMPT_SUFFIX = r" Please reason step by step, and put your final answer within \boxed{{}}."


def main() -> None:
    if hashlib.sha256(SOURCE.read_bytes()).hexdigest() != SOURCE_SHA256:
        raise ValueError(f"unexpected source contents: {SOURCE}")
    rows = []
    for line in SOURCE.open(encoding="utf-8"):
        row = json.loads(line)
        rows.append(
            {
                "data_source": "math_dapo",
                "prompt": [{"role": "user", "content": row["problem"] + PROMPT_SUFFIX}],
                "ability": "MATH",
                "reward_model": {
                    "style": "rule-lighteval/MATH_v2",
                    "ground_truth": row["answer"] or "",
                },
                "extra_info": {"index": row["id"]},
            }
        )
    if len(rows) != 7_500:
        raise ValueError(f"expected 7500 rows, got {len(rows)}")
    with OUTPUT.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(f"{OUTPUT.name}: {len(rows)} rows sha256={hashlib.sha256(OUTPUT.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()

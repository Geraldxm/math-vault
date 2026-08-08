#!/usr/bin/env python3
"""Losslessly merge the seven official MATH subject splits into JSONL."""

import argparse
import hashlib
import json
from pathlib import Path

import pyarrow.parquet as pq


REVISION = "21a5633873b6a120296cce3e2df9d5550074f4a3"
SUBSETS = (
    "algebra",
    "counting_and_probability",
    "geometry",
    "intermediate_algebra",
    "number_theory",
    "prealgebra",
    "precalculus",
)
EXPECTED_ROWS = {"train": 7500, "test": 5000}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build(raw_root: Path, output_root: Path, split: str) -> None:
    rows = []
    filename = f"{split}-00000-of-00001.parquet"
    for subset in SUBSETS:
        path = raw_root / subset / filename
        if not path.is_file():
            raise SystemExit(f"missing upstream artifact: {path}")
        rows.extend(pq.read_table(path).to_pylist())

    if len(rows) != EXPECTED_ROWS[split]:
        raise SystemExit(f"{split}: expected {EXPECTED_ROWS[split]} rows, got {len(rows)}")

    destination = output_root / f"{split}.jsonl"
    with destination.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")))
            handle.write("\n")
    print(f"{destination.name}: {len(rows)} rows sha256={sha256(destination)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("raw_root", type=Path, help="hf download directory for EleutherAI/hendrycks_math")
    args = parser.parse_args()
    output_root = Path(__file__).resolve().parent
    for split in ("train", "test"):
        build(args.raw_root, output_root, split)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Normalize official MATH train/test data without filtering or deduplication."""

import hashlib
import json
import re
from pathlib import Path
from typing import Optional


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / "source/hendrycks_math"
EXPECTED = {
    "train": (7_500, "505a29f3461da54981f8f4d26b89ef4077aaf14dc8d1611b29d96ab1a28a13d1"),
    "test": (5_000, "36fe05b2aa3f100458f123e59dedf6efe772b930119e353b208b24788fd45174"),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def last_boxed(text: str) -> Optional[str]:
    candidates = []
    for marker in (r"\boxed", r"\fbox"):
        offset = 0
        while (position := text.find(marker, offset)) >= 0:
            start = position + len(marker)
            while start < len(text) and text[start].isspace():
                start += 1
            if start < len(text) and text[start] == "{":
                depth = 0
                for end in range(start, len(text)):
                    if text[end] == "{":
                        depth += 1
                    elif text[end] == "}":
                        depth -= 1
                        if depth == 0:
                            candidates.append((position, text[start + 1 : end].strip()))
                            break
            offset = position + len(marker)
    if not candidates:
        for match in re.finditer(r"\\(?:boxed|fbox)\s+(.+?)(?=\$|[.\n])", text):
            value = match.group(1).strip()
            if value:
                candidates.append((match.start(), value))
    return max(candidates)[1] if candidates else None


def slug(value: str) -> str:
    return "_".join("".join(char.lower() if char.isalnum() else " " for char in value).split())


def build(split: str) -> None:
    expected_rows, expected_sha = EXPECTED[split]
    source = SOURCE / f"{split}.jsonl"
    if sha256(source) != expected_sha:
        raise ValueError(f"unexpected source contents: {source}")

    subject_counts = {}
    rows = []
    for source_line, line in enumerate(source.open(encoding="utf-8"), 1):
        row = json.loads(line)
        subject = str(row["type"])
        subject_counts[subject] = subject_counts.get(subject, 0) + 1
        answer = last_boxed(str(row["solution"]))
        answer_status = "extracted" if answer else "missing_boxed_answer"
        level = str(row["level"])
        if level == "Level ?":
            level_value = None
        elif level.startswith("Level ") and level.removeprefix("Level ").isdigit():
            level_value = int(level.removeprefix("Level "))
        else:
            raise ValueError(f"{source}:{source_line}: malformed level {level!r}")
        rows.append(
            {
                "id": f"{split}/{slug(subject)}/{subject_counts[subject]:04d}",
                "problem": str(row["problem"]),
                "answer": answer,
                "answer_status": answer_status,
                "solution": str(row["solution"]),
                "subject": subject,
                "level": level_value,
                "level_raw": level,
                "source": "EleutherAI/hendrycks_math",
            }
        )

    if len(rows) != expected_rows or len({row["id"] for row in rows}) != expected_rows:
        raise ValueError(f"{split}: expected {expected_rows} unique rows, got {len(rows)}")
    output = HERE / f"{split}.jsonl"
    with output.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(f"{output.name}: {len(rows)} rows sha256={sha256(output)}")


if __name__ == "__main__":
    for split in ("train", "test"):
        build(split)

import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "dapo_math_17k_compact/train.jsonl"


def normalize(text):
    return " ".join(text.split())


def build():
    groups = defaultdict(list)
    with SOURCE.open() as f:
        for line in f:
            row = json.loads(line)
            groups[normalize(row["problem"])].append(row)

    if sum(map(len, groups.values())) != 17_917 or len(groups) != 17_188:
        raise ValueError("unexpected compact source contents")

    output, conflicts = [], []
    for rows in groups.values():
        answers = {str(row["answer"]) for row in rows}
        if len(answers) > 1:
            conflicts.append(
                {
                    "problem": rows[0]["problem"],
                    "ids": [row["id"] for row in rows],
                    "answers": sorted(answers),
                    "source_rows": [{"id": row["id"], "answer": str(row["answer"])} for row in rows],
                }
            )
        else:
            output.append(
                {
                    "id": rows[0]["id"],
                    "problem": rows[0]["problem"],
                    "answer": answers.pop(),
                    "datasource": "dapo17k",
                    "source": "BytedTsinghua-SIA/DAPO-Math-17k",
                }
            )

    if len(output) != 17_176 or len(conflicts) != 12:
        raise ValueError("unexpected dedup result")
    if len({normalize(row["problem"]) for row in output}) != len(output):
        raise ValueError("duplicate normalized problems remain")
    if len({row["id"] for row in output}) != len(output):
        raise ValueError("duplicate ids remain")

    with (HERE / "train.jsonl").open("w", encoding="utf-8", newline="\n") as f:
        for row in output:
            f.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
    with (HERE / "conflicts.jsonl").open("w", encoding="utf-8", newline="\n") as f:
        for row in conflicts:
            f.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(f"wrote {len(output):,} clean rows and {len(conflicts)} conflicts")


if __name__ == "__main__":
    build()

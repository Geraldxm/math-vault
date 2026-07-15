"""Build canonical JSONL inputs for math-eval using only the stdlib."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# output: (parent, rows, upstream, id field, problem field, conversion mode)
SPECS = {
    "aime_2024/train.jsonl": ("source/aime_2024/train.jsonl", 30, "HuggingFaceH4/aime_2024", "id", "problem", "direct"),
    "aime_2025/train.jsonl": ("source/aime_2025/train.jsonl", 30, "MathArena/aime_2025", "problem_idx", "problem", "direct"),
    "aime_2026/train.jsonl": ("source/aime_2026/train.jsonl", 30, "MathArena/aime_2026", "problem_idx", "problem", "direct"),
    "aimo_validation_aime/train.jsonl": ("source/aimo_validation_aime/train.jsonl", 90, "AI-MO/aimo-validation-aime", "id", "problem", "direct"),
    "aimo_validation_amc/train.jsonl": ("source/aimo_validation_amc/train.jsonl", 83, "AI-MO/aimo-validation-amc", "url", "problem", "direct"),
    "amc_2023/test.jsonl": ("source/amc_2023/test.jsonl", 40, "math-ai/amc23", "id", "question", "direct"),
    "brumo_2025/train.jsonl": ("source/brumo_2025/train.jsonl", 30, "MathArena/brumo_2025", "problem_idx", "problem", "direct"),
    "cmimc_2025/train.jsonl": ("source/cmimc_2025/train.jsonl", 40, "MathArena/cmimc_2025", "problem_idx", "problem", "direct"),
    "dapo_math_17k_dedup/train.jsonl": ("derived/dapo_math_17k_dedup/train.jsonl", 17_176, "BytedTsinghua-SIA/DAPO-Math-17k", "id", "problem", "direct"),
    "gsm8k/train.jsonl": ("source/gsm8k/train.jsonl", 7_473, "openai/gsm8k", None, "question", "gsm8k"),
    "gsm8k/test.jsonl": ("source/gsm8k/test.jsonl", 1_319, "openai/gsm8k", None, "question", "gsm8k"),
    "hmmt_feb_2025/train.jsonl": ("source/hmmt_feb_2025/train.jsonl", 30, "MathArena/hmmt_feb_2025", "problem_idx", "problem", "direct"),
    "math_500/test.jsonl": ("source/math_500/test.jsonl", 500, "HuggingFaceH4/MATH-500", "unique_id", "problem", "direct"),
    "minerva_math/train.jsonl": ("source/minerva_math/train.jsonl", 272, "knoveleng/Minerva-Math", "idx", "problem", "minerva"),
    "omni_math/train.jsonl": ("source/omni_math/train.jsonl", 4_411, "KbsdJames/Omni-MATH", None, "problem", "omni"),
    "olympiad_bench/train.jsonl": ("source/olympiad_bench/train.jsonl", 674, "Hothan/OlympiadBench:OE_TO_maths_en_COMP", "id", "question", "olympiad"),
}

OMNI_MATH_ISSUES = {
    446: "malformed_latex",
    906: "malformed_latex",
    1077: "malformed_latex",
    1081: "piecewise_text",
    1759: "verification_error",
    2408: "malformed_latex",
    2429: "malformed_latex",
    4108: "multiple_boxed_answers",
    4147: "empty_answer",
    4161: "empty_answer",
    4168: "empty_answer",
    4182: "empty_answer",
    4233: "empty_answer",
    4250: "empty_answer",
    4340: "empty_answer",
    4400: "empty_answer",
    4416: "empty_answer",
}


def last_boxed(text: str) -> str | None:
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
    return max(candidates)[1] if candidates else None


def unwrap_math(value: object) -> str:
    answer = str(value).strip()
    if answer.startswith("$"):
        closing = answer.rfind("$")
        if closing > 0 and not answer[closing + 1 :].strip(" ."):
            answer = answer[1:closing].strip()
    return answer


def canonical_row(row: dict, index: int, split: str, spec: tuple) -> dict:
    _, _, source_name, id_field, problem_field, mode = spec
    problem = str(row[problem_field])
    consumed = {problem_field}

    if mode == "gsm8k":
        _, marker, answer = str(row["answer"]).rpartition("\n#### ")
        if not marker:
            raise ValueError("GSM8K answer is missing the final #### marker")
        problem_id = f"{split}-{index:06d}"
        solution = str(row["answer"])
        consumed.add("answer")
    elif mode == "minerva":
        answer = last_boxed(str(row["solution"])) or ""
        problem_id = str(row[id_field])
        solution = str(row["solution"])
        consumed.update({id_field, "solution"})
    elif mode == "omni":
        answer = str(row["answer"])
        problem_id = f"{split}-{index:06d}"
        solution = str(row["solution"])
        consumed.update({"answer", "solution"})
    elif mode == "olympiad":
        values = row["final_answer"]
        if not isinstance(values, list) or len(values) != 1:
            raise ValueError("OlympiadBench final_answer must contain exactly one string")
        answer = unwrap_math(values[0])
        problem_id = str(row[id_field])
        solutions = row["solution"]
        solution = (
            str(solutions[0])
            if isinstance(solutions, list) and len(solutions) == 1
            else str(solutions)
        )
        consumed.update({id_field, "final_answer", "solution"})
    else:
        answer = str(row["answer"])
        problem_id = str(row[id_field])
        solution = str(row["solution"]) if "solution" in row else None
        consumed.update({id_field, "answer", "solution"})

    if not problem_id.strip() or not problem.strip() or not answer.strip():
        raise ValueError("canonical id, problem, and answer must be non-empty")
    metadata = {key: value for key, value in row.items() if key not in consumed}
    result = {
        "id": problem_id,
        "problem": problem,
        "answer": answer.strip(),
    }
    if solution is not None:
        result["solution"] = solution
    result["source"] = source_name
    if metadata:
        result["metadata"] = metadata
    return result


def build() -> None:
    manifest = {"schema": "math-eval-canonical-v1", "datasets": [], "issues": []}
    for output_name, spec in SPECS.items():
        parent_name, expected_rows, upstream, *_ = spec
        parent = ROOT / parent_name
        split = Path(output_name).stem
        rows = []
        issues = []
        for line_number, line in enumerate(parent.open(encoding="utf-8"), 1):
            try:
                source_row = json.loads(line)
                if spec[-1] == "omni" and line_number in OMNI_MATH_ISSUES:
                    issues.append(
                        {
                            "id": f"{split}-{line_number - 1:06d}",
                            "source_line": line_number,
                            "issue": OMNI_MATH_ISSUES[line_number],
                            "row": source_row,
                        }
                    )
                    continue
                rows.append(
                    canonical_row(source_row, line_number - 1, split, spec)
                )
            except Exception as exc:
                raise ValueError(f"{parent}:{line_number}: {exc}") from exc
        if len(rows) != expected_rows:
            raise ValueError(f"{parent}: expected {expected_rows} rows, found {len(rows)}")
        ids = [row["id"] for row in rows]
        if len(ids) != len(set(ids)):
            raise ValueError(f"{parent}: canonical IDs are not unique")

        output = HERE / output_name
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("w", encoding="utf-8", newline="\n") as destination:
            for row in rows:
                destination.write(
                    json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n"
                )
        manifest["datasets"].append(
            {
                "path": output_name,
                "rows": len(rows),
                "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
                "source": upstream,
                "parent_path": parent_name,
                "parent_sha256": hashlib.sha256(parent.read_bytes()).hexdigest(),
            }
        )
        print(f"wrote {len(rows):,} rows to {output}")

        if spec[-1] == "omni":
            if len(issues) != len(OMNI_MATH_ISSUES):
                raise ValueError("Omni-MATH issue rows do not match the audit set")
            issue_output = HERE / "omni_math/issues.jsonl"
            with issue_output.open("w", encoding="utf-8", newline="\n") as destination:
                for row in issues:
                    destination.write(
                        json.dumps(row, ensure_ascii=False, separators=(",", ":"))
                        + "\n"
                    )
            manifest["issues"].append(
                {
                    "path": "omni_math/issues.jsonl",
                    "rows": len(issues),
                    "sha256": hashlib.sha256(issue_output.read_bytes()).hexdigest(),
                    "source": upstream,
                    "parent_path": parent_name,
                    "parent_sha256": hashlib.sha256(parent.read_bytes()).hexdigest(),
                    "audit": {"parser_id": "math-v3", "math_verify": "0.9.0"},
                }
            )
            print(f"wrote {len(issues):,} issue rows to {issue_output}")

    (HERE / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    build()

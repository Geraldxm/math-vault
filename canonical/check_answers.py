"""Check every canonical gold with math-eval's installed parser."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


def main() -> int:
    arguments = argparse.ArgumentParser()
    arguments.add_argument("math_eval", type=Path)
    arguments.add_argument(
        "--parser-id",
        choices=("math-v3", "math-v4-dual", "math-v5-dual"),
        default="math-v5-dual",
    )
    args = arguments.parse_args()
    sys.path.insert(0, str(args.math_eval.resolve() / "scripts"))

    from parser import (
        DUAL_PARSER_CONFIG_HASH,
        DUAL_PARSER_ID,
        MATH_VERIFY_VERSION,
        PARSER_CONFIG_HASH,
        PARSER_ID,
        V5_DUAL_PARSER_CONFIG_HASH,
        V5_DUAL_PARSER_ID,
        parse_and_verify,
        parse_dual_and_verify,
        parse_v5_dual_and_verify,
    )

    parser_config_hash = {
        PARSER_ID: PARSER_CONFIG_HASH,
        DUAL_PARSER_ID: DUAL_PARSER_CONFIG_HASH,
        V5_DUAL_PARSER_ID: V5_DUAL_PARSER_CONFIG_HASH,
    }[args.parser_id]

    def check(answer: str) -> tuple[bool, str, str | None]:
        final_text = r"\boxed{" + answer + "}"
        if args.parser_id == PARSER_ID:
            result = parse_and_verify(final_text, answer)
            return result.is_correct, result.status, result.error
        parser = (
            parse_v5_dual_and_verify
            if args.parser_id == V5_DUAL_PARSER_ID
            else parse_dual_and_verify
        )
        result = parser(final_text, answer)
        if result.strict != result.soft:
            return False, "strict_soft_mismatch", None
        return result.strict.is_correct, result.strict.status, result.strict.error

    here = Path(__file__).resolve().parent
    manifest = json.loads((here / "manifest.json").read_text(encoding="utf-8"))
    failed = []
    checked = 0
    for artifact in manifest.get("issues", []):
        path = here / artifact["path"]
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != artifact["sha256"]:
            failed.append(f"{path}: checksum differs from manifest")
        with path.open(encoding="utf-8") as source:
            rows = sum(1 for line in source if json.loads(line))
        if rows != artifact["rows"]:
            failed.append(f"{path}: expected {artifact['rows']} rows, found {rows}")
        print(f"checked {rows:,} issue rows in {artifact['path']}")

    for dataset in manifest["datasets"]:
        path = here / dataset["path"]
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != dataset["sha256"]:
            failed.append(f"{path}: checksum differs from manifest")
            continue
        rows = 0
        with path.open(encoding="utf-8") as source:
            for line_number, line in enumerate(source, 1):
                answer = str(json.loads(line)["answer"])
                try:
                    is_correct, status, error = check(answer)
                except Exception as exc:
                    failed.append(
                        f"{path}:{line_number}: {type(exc).__name__}: {exc}"
                    )
                else:
                    if not is_correct:
                        failed.append(f"{path}:{line_number}: {status}: {error}")
                rows += 1
        if rows != dataset["rows"]:
            failed.append(f"{path}: expected {dataset['rows']} rows, found {rows}")
        checked += rows
        print(f"checked {rows:,} answers in {dataset['path']}")

    print(
        json.dumps(
            {
                "parser_id": args.parser_id,
                "parser_config_hash": parser_config_hash,
                "math_verify": MATH_VERIFY_VERSION,
                "checked": checked,
                "failed": len(failed),
            }
        )
    )
    if failed:
        print("\n".join(failed[:20]), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

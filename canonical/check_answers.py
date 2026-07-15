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
    args = arguments.parse_args()
    sys.path.insert(0, str(args.math_eval.resolve() / "scripts"))

    from parser import MATH_VERIFY_VERSION, PARSER_ID, parse_and_verify

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
                    result = parse_and_verify(r"\boxed{" + answer + "}", answer)
                except Exception as exc:
                    failed.append(
                        f"{path}:{line_number}: {type(exc).__name__}: {exc}"
                    )
                else:
                    if not result.is_correct:
                        failed.append(
                            f"{path}:{line_number}: {result.status}: {result.error}"
                        )
                rows += 1
        if rows != dataset["rows"]:
            failed.append(f"{path}: expected {dataset['rows']} rows, found {rows}")
        checked += rows
        print(f"checked {rows:,} answers in {dataset['path']}")

    print(
        json.dumps(
            {
                "parser_id": PARSER_ID,
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

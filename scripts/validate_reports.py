#!/usr/bin/env python3
"""Validate data/reports/<TICKER>.json against data/schema/report.v1.json
and against the published Markdown (hash, scores, ticker set).

Usage (from the repository root):

    python3 scripts/validate_reports.py
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Allow running as a script from the repo root or from scripts/.
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from extract_reports import (  # noqa: E402
    SECTION_KEYS,
    OUT_DIR,
    SCHEMA_VERSION,
    git_tracked_reports,
    sha256_text,
)

SCHEMA_PATH = ROOT / "data" / "schema" / "report.v1.json"


def load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def type_ok(value, spec: dict, defs: dict) -> tuple[bool, str]:
    if "$ref" in spec:
        ref = spec["$ref"]
        if ref.startswith("#/$defs/"):
            return type_ok(value, defs[ref.split("/")[-1]], defs)
        return False, f"unresolved ref {ref}"
    if "const" in spec:
        if value != spec["const"]:
            return False, f"expected const {spec['const']!r}, got {value!r}"
        return True, ""
    if "enum" in spec and "type" not in spec and "anyOf" not in spec:
        if value not in spec["enum"]:
            return False, f"expected one of {spec['enum']}, got {value!r}"
        return True, ""
    types = spec.get("type")
    if types is None and "enum" in spec:
        if value not in spec["enum"]:
            return False, f"expected one of {spec['enum']}, got {value!r}"
        return True, ""
    if isinstance(types, str):
        types = [types]
    if types:
        ok = False
        for t in types:
            if t == "null" and value is None:
                ok = True
            elif t == "string" and isinstance(value, str):
                ok = True
            elif t == "integer" and isinstance(value, int) and not isinstance(value, bool):
                ok = True
            elif t == "number" and isinstance(value, (int, float)) and not isinstance(value, bool):
                ok = True
            elif t == "boolean" and isinstance(value, bool):
                ok = True
            elif t == "array" and isinstance(value, list):
                ok = True
            elif t == "object" and isinstance(value, dict):
                ok = True
        if not ok:
            return False, f"expected type {types}, got {type(value).__name__}"
    if "enum" in spec and value is not None:
        if value not in spec["enum"]:
            return False, f"expected one of {spec['enum']}, got {value!r}"
    if isinstance(value, str):
        if "minLength" in spec and len(value) < spec["minLength"]:
            return False, "string too short"
        if "pattern" in spec and not re.search(spec["pattern"], value):
            return False, f"pattern {spec['pattern']} failed"
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in spec and value < spec["minimum"]:
            return False, "below minimum"
        if "maximum" in spec and value > spec["maximum"]:
            return False, "above maximum"
    return True, ""


def validate_against_schema(rec: dict, schema: dict, path: str = "$") -> list[str]:
    defs = schema.get("$defs") or schema.get("definitions") or {}
    errors: list[str] = []

    def walk(value, spec, here: str) -> None:
        if "$ref" in spec:
            ref = spec["$ref"]
            if ref.startswith("#/$defs/"):
                walk(value, defs[ref.split("/")[-1]], here)
                return
            errors.append(f"{here}: unresolved ref {ref}")
            return
        if "anyOf" in spec:
            ok_any = False
            for opt in spec["anyOf"]:
                before = len(errors)
                walk(value, opt, here)
                if len(errors) == before:
                    ok_any = True
                    break
                del errors[before:]
            if not ok_any:
                errors.append(f"{here}: no anyOf branch matched")
            return
        ok, msg = type_ok(value, spec, defs)
        if not ok:
            errors.append(f"{here}: {msg}")
            return
        typ = spec.get("type")
        types = typ if isinstance(typ, list) else [typ] if typ else []
        if "object" in types or (isinstance(value, dict) and typ is None and ("properties" in spec or "required" in spec)):
            if not isinstance(value, dict):
                return
            required = spec.get("required") or []
            for key in required:
                if key not in value:
                    errors.append(f"{here}: missing required property {key}")
            props = spec.get("properties") or {}
            additional = spec.get("additionalProperties", True)
            for key, val in value.items():
                if key in props:
                    walk(val, props[key], f"{here}.{key}")
                elif additional is False:
                    errors.append(f"{here}: unexpected property {key}")
                elif isinstance(additional, dict):
                    walk(val, additional, f"{here}.{key}")
        if "array" in types and isinstance(value, list):
            item_spec = spec.get("items")
            if item_spec:
                for i, item in enumerate(value):
                    walk(item, item_spec, f"{here}[{i}]")

    walk(rec, schema, path)
    return errors


def validate_file(path: Path, schema: dict, published: dict[str, Path]) -> list[str]:
    errors: list[str] = []
    try:
        rec = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{path.name}: invalid JSON ({exc})"]
    errors.extend(f"{path.name}{e[1:]}" if e.startswith("$") else f"{path.name}: {e}" for e in validate_against_schema(rec, schema))
    ticker = rec.get("ticker")
    if ticker and path.stem != ticker:
        errors.append(f"{path.name}: filename stem {path.stem} != ticker {ticker}")
    if rec.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"{path.name}: schema_version {rec.get('schema_version')!r}")
    src = rec.get("source_markdown") or {}
    pub = published.get(ticker or "")
    if not pub:
        errors.append(f"{path.name}: ticker {ticker} is not a published (git-tracked) report")
    else:
        text = pub.read_text(encoding="utf-8")
        digest = sha256_text(text)
        if src.get("sha256") != digest:
            errors.append(f"{path.name}: sha256 does not match {src.get('path')}")
        if src.get("bytes") != len(text.encode("utf-8")):
            errors.append(f"{path.name}: byte length does not match the Markdown")
    scores = rec.get("section_scores") or {}
    if set(scores) != set(SECTION_KEYS):
        errors.append(f"{path.name}: section_scores keys mismatch")
    expected_passed = sum(1 for k in SECTION_KEYS if isinstance(scores.get(k), int) and scores[k] >= 6)
    if rec.get("sections_passed") != expected_passed:
        errors.append(f"{path.name}: sections_passed {rec.get('sections_passed')} != {expected_passed}")
    gates = rec.get("hard_gates") or {}
    for key in ("revenue", "selling_behavior"):
        g = gates.get(key) or {}
        if scores.get(key) is not None and g.get("tripped") != (scores[key] <= 3):
            errors.append(f"{path.name}: hard_gates.{key}.tripped inconsistent with the score")
    verdict = rec.get("overall_verdict")
    overall = rec.get("overall_score")
    tripped = any((gates.get(k) or {}).get("tripped") for k in ("revenue", "selling_behavior"))
    if isinstance(overall, (int, float)):
        expect = "FAIL" if tripped or overall < 6.0 else "PASS"
        if verdict != expect:
            errors.append(f"{path.name}: overall_verdict {verdict} inconsistent with score/gates (expected {expect})")
    return errors


def validate_all() -> list[str]:
    schema = load_schema()
    published = {p.stem: p for p in git_tracked_reports()}
    files = sorted(OUT_DIR.glob("*.json"))
    errors: list[str] = []
    json_tickers = {p.stem for p in files}
    missing = sorted(set(published) - json_tickers)
    extra = sorted(json_tickers - set(published))
    for t in missing:
        errors.append(f"missing data/reports/{t}.json for published report")
    for t in extra:
        errors.append(f"data/reports/{t}.json has no published (git-tracked) report — unpublished drafts must not be extracted")
    for path in files:
        errors.extend(validate_file(path, schema, published))
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)
    errors = validate_all()
    if errors:
        print(f"{len(errors)} validation error(s):", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        return 1
    n = len(list(OUT_DIR.glob("*.json")))
    print(f"OK: {n} report JSON files match the schema and the published Markdown.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate the repository's JSONL data and calculation invariants."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_jsonl(relative_path: str) -> list[dict]:
    path = ROOT / relative_path
    records: list[dict] = []
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as error:
                raise ValueError(f"{relative_path}:{line_number}: {error}") from error
    return records


def require(record: dict, fields: set[str], label: str) -> None:
    missing = sorted(fields.difference(record))
    if missing:
        raise ValueError(f"{label}: missing fields: {', '.join(missing)}")


def validate_pilot_texts(records: list[dict]) -> None:
    seen: set[str] = set()
    required = {"text_id", "language", "text", "context", "license_status"}
    for item in records:
        require(item, required, item.get("text_id", "pilot text"))
        text_id = item["text_id"]
        if text_id in seen:
            raise ValueError(f"duplicate text_id: {text_id}")
        seen.add(text_id)


def validate_annotations(records: list[dict], text_ids: set[str]) -> None:
    required = {
        "observation_id",
        "text_id",
        "protocol_version",
        "status",
        "lens",
        "semantic_nodes",
        "N",
        "E",
        "D",
        "P_observed",
    }
    for item in records:
        label = item.get("observation_id", "annotation")
        require(item, required, label)
        if item["text_id"] not in text_ids:
            raise ValueError(f"{label}: unknown text_id: {item['text_id']}")
        if item["N"] != len(item["semantic_nodes"]):
            raise ValueError(f"{label}: N does not equal semantic_nodes length")
        require(
            item["lens"],
            {"lens_id", "lens_type", "language", "domain_familiarity"},
            f"{label}.lens",
        )
        measured = [item.get("E"), item.get("D"), item.get("P_observed")]
        if any(value is not None for value in measured):
            if not all(value is not None for value in measured):
                raise ValueError(f"{label}: E, D, and P_observed must be set together")
            expected = item["N"] * item["E"] / item["D"]
            if not math.isclose(expected, item["P_observed"], rel_tol=1e-6):
                raise ValueError(f"{label}: P_observed does not match N*E/D")


def validate_historical(records: list[dict]) -> None:
    required = {
        "case_id",
        "record_type",
        "source_url",
        "N",
        "E",
        "D",
        "P_reported",
        "calculation_check",
        "calibration_status",
    }
    for item in records:
        label = item.get("case_id", "historical case")
        require(item, required, label)
        expected = item["N"] * item["E"] / item["D"]
        if not math.isclose(expected, item["calculation_check"], rel_tol=1e-6):
            raise ValueError(f"{label}: calculation_check does not match N*E/D")
        if item["calibration_status"] != "requires re-annotation":
            raise ValueError(f"{label}: historical data must not be marked calibrated")


def main() -> int:
    manifest = json.loads((ROOT / "dataset_manifest.json").read_text(encoding="utf-8"))
    texts = load_jsonl(manifest["files"]["pilot_texts"])
    annotations = load_jsonl(manifest["files"]["pilot_annotations"])
    historical = load_jsonl(manifest["files"]["historical_cases"])

    validate_pilot_texts(texts)
    validate_annotations(annotations, {item["text_id"] for item in texts})
    validate_historical(historical)

    actual_counts = {
        "pilot_texts": len(texts),
        "pilot_annotations": len(annotations),
        "historical_cases": len(historical),
    }
    if actual_counts != manifest["counts"]:
        raise ValueError(
            f"manifest counts differ: expected {manifest['counts']}, got {actual_counts}"
        )
    print(json.dumps({"status": "ok", "counts": actual_counts}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

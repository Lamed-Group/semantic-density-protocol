#!/usr/bin/env python3
"""Build a self-contained Hugging Face dataset upload directory."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "dist" / "huggingface"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    if TARGET.exists():
        shutil.rmtree(TARGET)
    (TARGET / "data" / "pilot").mkdir(parents=True)
    (TARGET / "data" / "historical").mkdir(parents=True)
    (TARGET / "schemas").mkdir(parents=True)

    copies = {
        ROOT / "huggingface" / "README.md": TARGET / "README.md",
        ROOT / "data" / "pilot" / "texts.jsonl": TARGET / "data" / "pilot" / "texts.jsonl",
        ROOT / "data" / "pilot" / "annotations.jsonl": TARGET / "data" / "pilot" / "annotations.jsonl",
        ROOT / "data" / "historical" / "site_cases.jsonl": TARGET / "data" / "historical" / "site_cases.jsonl",
        ROOT / "schemas" / "text.schema.json": TARGET / "schemas" / "text.schema.json",
        ROOT / "schemas" / "annotation.schema.json": TARGET / "schemas" / "annotation.schema.json",
        ROOT / "schemas" / "historical-case.schema.json": TARGET / "schemas" / "historical-case.schema.json",
        ROOT / "LICENSE-DATA.md": TARGET / "LICENSE-DATA.md",
        ROOT / "dataset_manifest.json": TARGET / "dataset_manifest.json",
    }
    for source, destination in copies.items():
        shutil.copy2(source, destination)

    payload = {
        "format": "Hugging Face upload scaffold",
        "files": {
            str(path.relative_to(TARGET)): sha256(path)
            for path in sorted(TARGET.rglob("*"))
            if path.is_file()
        },
    }
    (TARGET / "SHA256SUMS.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(TARGET)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

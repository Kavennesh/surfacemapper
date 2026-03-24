"""JSON serialization helpers."""

from __future__ import annotations

import json
from pathlib import Path

from surfacemapper.models import ScanResult


def save_json_report(result: ScanResult, destination: str | Path) -> Path:
    """Write the scan result as JSON."""

    path = Path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result.model_dump(mode="json"), indent=2), encoding="utf-8")
    return path


def load_json_report(source: str | Path) -> ScanResult:
    """Load a previously saved JSON scan result."""

    payload = json.loads(Path(source).read_text(encoding="utf-8"))
    return ScanResult.model_validate(payload)


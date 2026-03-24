"""JSON serialization helpers."""

from __future__ import annotations

import json
from pathlib import Path

from surfacemapper.models import ScanResult


RESULTS_DIR = Path("results")


def resolve_results_path(destination: str | Path) -> Path:
    """Normalize report output paths under the dedicated results directory."""

    raw_path = Path(destination)
    relative_parts = raw_path.parts[1:] if raw_path.parts and raw_path.parts[0] == RESULTS_DIR.name else raw_path.parts
    normalized = RESULTS_DIR.joinpath(*relative_parts) if relative_parts else RESULTS_DIR / raw_path.name
    return normalized


def save_json_report(result: ScanResult, destination: str | Path) -> Path:
    """Write the scan result as JSON."""

    path = resolve_results_path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result.model_dump(mode="json"), indent=2), encoding="utf-8")
    return path


def load_json_report(source: str | Path) -> ScanResult:
    """Load a previously saved JSON scan result."""

    payload = json.loads(Path(source).read_text(encoding="utf-8"))
    return ScanResult.model_validate(payload)

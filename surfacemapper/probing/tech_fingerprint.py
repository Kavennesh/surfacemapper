"""Conservative technology fingerprinting."""

from __future__ import annotations

from surfacemapper.config import AppConfig


def infer_technologies(headers: dict[str, str], html: str, config: AppConfig) -> list[str]:
    """Infer technology hints from headers and response content."""

    haystack = " ".join([*headers.keys(), *headers.values(), html]).lower()
    detections = [
        name
        for name, markers in config.tech_markers.items()
        if any(marker in haystack for marker in markers)
    ]
    return sorted(set(detections))


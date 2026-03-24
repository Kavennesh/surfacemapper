"""Safe exposure path probing."""

from __future__ import annotations

import httpx

from surfacemapper.models import ExposureFinding
from surfacemapper.utils.urls import join_url


PATH_REASON_MAP = {
    "/admin": ("Administrative interface pattern", "medium"),
    "/login": ("Authentication endpoint pattern", "medium"),
    "/dashboard": ("Dashboard-style path pattern", "medium"),
    "/wp-login.php": ("WordPress login endpoint pattern", "high"),
}


def check_exposure_paths(
    client: httpx.Client,
    base_url: str,
    paths: tuple[str, ...],
) -> list[ExposureFinding]:
    """Check a minimal safe-list of common exposure paths."""

    findings: list[ExposureFinding] = []
    for path in paths:
        try:
            response = client.get(join_url(base_url, path))
        except httpx.HTTPError:
            continue
        if response.status_code < 400:
            reason, confidence = PATH_REASON_MAP.get(path, ("Interesting path pattern", "low"))
            findings.append(
                ExposureFinding(
                    path=path,
                    status_code=response.status_code,
                    reason=reason,
                    confidence=confidence,
                )
            )
    return findings


"""Input validators and normalizers."""

from __future__ import annotations

import re


DOMAIN_RE = re.compile(
    r"^(?=.{1,253}$)(?!-)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}$"
)


def validate_root_domain(value: str) -> str:
    """Validate a root domain and return a normalized value."""

    normalized = value.strip().lower().rstrip(".")
    if "://" in normalized or "/" in normalized:
        raise ValueError("Expected a root domain, not a URL or path.")
    if not DOMAIN_RE.fullmatch(normalized):
        raise ValueError("Invalid root domain format.")
    return normalized


def belongs_to_root(hostname: str, root_domain: str) -> bool:
    """Return True when a hostname belongs to the target root domain."""

    candidate = hostname.strip().lower().rstrip(".")
    root = root_domain.strip().lower().rstrip(".")
    return candidate == root or candidate.endswith(f".{root}")


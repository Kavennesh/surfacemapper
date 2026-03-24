"""URL helper functions."""

from __future__ import annotations


def join_url(base: str, path: str) -> str:
    """Safely join a base URL and a relative path."""

    return f"{base.rstrip('/')}/{path.lstrip('/')}"


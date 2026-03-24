"""Text extraction helpers."""

from __future__ import annotations

import re


TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)


def extract_html_title(html: str) -> str | None:
    """Extract the HTML title from a small response body."""

    match = TITLE_RE.search(html)
    if not match:
        return None
    title = re.sub(r"\s+", " ", match.group(1)).strip()
    return title or None


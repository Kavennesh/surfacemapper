"""crt.sh passive subdomain provider."""

from __future__ import annotations

from collections.abc import Iterable

import httpx

from surfacemapper.validators import belongs_to_root


CRT_SH_URL = "https://crt.sh/"


def fetch_crtsh_subdomains(
    root_domain: str,
    *,
    timeout: float,
    user_agent: str,
    limit: int,
) -> list[str]:
    """Fetch passive subdomains from crt.sh JSON output."""

    params = {"q": f"%.{root_domain}", "output": "json"}
    headers = {"User-Agent": user_agent}
    with httpx.Client(timeout=timeout, follow_redirects=True, headers=headers) as client:
        response = client.get(CRT_SH_URL, params=params)
        response.raise_for_status()
        payload = response.json()
    return parse_crtsh_entries(payload, root_domain=root_domain)[:limit]


def parse_crtsh_entries(entries: Iterable[dict], *, root_domain: str) -> list[str]:
    """Normalize and filter crt.sh entries for the requested root domain."""

    results: set[str] = set()
    for entry in entries:
        raw_name = str(entry.get("name_value", "")).strip()
        if not raw_name:
            continue
        for line in raw_name.splitlines():
            candidate = line.strip().lower().lstrip("*.").rstrip(".")
            if candidate and belongs_to_root(candidate, root_domain):
                results.add(candidate)
    return sorted(results)


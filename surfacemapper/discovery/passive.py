"""Passive discovery orchestration."""

from __future__ import annotations

from surfacemapper.config import AppConfig
from surfacemapper.discovery.crtsh import fetch_crtsh_subdomains


def discover_subdomains(root_domain: str, config: AppConfig) -> tuple[list[str], list[str]]:
    """Run passive discovery providers and merge unique results."""

    discovered: set[str] = {root_domain}
    providers: list[str] = []
    try:
        discovered.update(
            fetch_crtsh_subdomains(
                root_domain,
                timeout=config.http_timeout,
                user_agent=config.user_agent,
                limit=config.max_subdomains,
            )
        )
        providers.append("crt.sh")
    except Exception:
        providers.append("crt.sh (error)")
    return sorted(discovered), providers


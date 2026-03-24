"""Top-level scan orchestration."""

from __future__ import annotations

from surfacemapper.config import AUTHORIZED_USE_DISCLAIMER, AppConfig, DEFAULT_CONFIG
from surfacemapper.core.risk import assess_asset_risk
from surfacemapper.discovery.passive import discover_subdomains
from surfacemapper.dns.resolver import resolve_record_set
from surfacemapper.models import ScanResult, SubdomainAsset, Target
from surfacemapper.probing.http_probe import probe_host
from surfacemapper.validators import validate_root_domain


def scan_target(root_domain: str, config: AppConfig | None = None) -> ScanResult:
    """Run the full passive-first scanning workflow."""

    active_config = config or DEFAULT_CONFIG
    normalized = validate_root_domain(root_domain)
    hostnames, providers = discover_subdomains(normalized, active_config)
    assets: list[SubdomainAsset] = []

    for hostname in hostnames:
        dns_records = resolve_record_set(hostname, active_config)
        probes = probe_host(hostname, active_config)
        assets.append(
            SubdomainAsset(
                hostname=hostname,
                dns=dns_records,
                http_services=probes,
                risk=assess_asset_risk(probes),
            )
        )

    return ScanResult(
        target=Target(root_domain=normalized),
        disclaimer=AUTHORIZED_USE_DISCLAIMER,
        subdomains=assets,
        discovery_providers=providers,
        methodology=[
            "Validated the root domain and rejected URL-style input.",
            "Collected passive subdomains from crt.sh.",
            "Resolved A, AAAA, CNAME, MX, and NS records.",
            "Probed HTTP and HTTPS with lightweight metadata collection only.",
            "Assessed security headers, exposure paths, and conservative technology hints.",
            "Assigned transparent rule-based risk labels.",
        ],
    )


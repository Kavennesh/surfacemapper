"""Transparent rule-based risk scoring."""

from __future__ import annotations

from surfacemapper.models import HTTPProbeResult, RiskAssessment


STACK_LEAK_MARKERS = ("apache", "nginx", "php", "asp.net", "iis")


def assess_asset_risk(probes: list[HTTPProbeResult]) -> RiskAssessment:
    """Score an asset using transparent conservative heuristics."""

    score = 0
    reasons: list[str] = []

    for probe in probes:
        if probe.error:
            continue

        admin_paths = [finding for finding in probe.exposures if finding.path in {"/admin", "/login", "/dashboard"}]
        wp_login = [finding for finding in probe.exposures if finding.path == "/wp-login.php"]
        if admin_paths:
            score += 3
            reasons.append(f"Admin or login-style endpoint exposed on {probe.final_url}.")
        if wp_login:
            score += 3
            reasons.append(f"WordPress login endpoint exposed on {probe.final_url}.")
        if probe.security_headers.missing_count >= 4:
            score += 2
            reasons.append(f"Multiple recommended security headers missing on {probe.final_url}.")
        if _reveals_stack_details(probe):
            score += 1
            reasons.append(f"Server or framework headers disclose stack details on {probe.final_url}.")

    label = "High" if score >= 6 else "Medium" if score >= 3 else "Low"
    return RiskAssessment(score=score, label=label, reasons=list(dict.fromkeys(reasons)))


def _reveals_stack_details(probe: HTTPProbeResult) -> bool:
    stack_blob = " ".join(filter(None, [probe.server, probe.x_powered_by])).lower()
    return any(marker in stack_blob for marker in STACK_LEAK_MARKERS)


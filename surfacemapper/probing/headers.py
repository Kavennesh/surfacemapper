"""Security header analysis."""

from __future__ import annotations

from surfacemapper.config import AppConfig
from surfacemapper.models import SecurityHeaderAssessment, SecurityHeaderCheck


HEADER_EXPLANATIONS = {
    "Content-Security-Policy": "Helps restrict script and content execution sources.",
    "Strict-Transport-Security": "Helps enforce HTTPS usage in supporting browsers.",
    "X-Frame-Options": "Helps reduce clickjacking exposure.",
    "X-Content-Type-Options": "Helps prevent MIME type sniffing.",
    "Referrer-Policy": "Controls referrer data shared with other origins.",
    "Permissions-Policy": "Restricts access to selected browser features.",
}


def assess_security_headers(headers: dict[str, str], config: AppConfig) -> SecurityHeaderAssessment:
    """Evaluate the configured set of security headers."""

    normalized = {key.lower(): value for key, value in headers.items()}
    checks: list[SecurityHeaderCheck] = []
    for header in config.security_headers:
        value = normalized.get(header.lower())
        checks.append(
            SecurityHeaderCheck(
                header=header,
                present=value is not None,
                value=value,
                explanation=HEADER_EXPLANATIONS[header],
            )
        )
    return SecurityHeaderAssessment(checks=checks)


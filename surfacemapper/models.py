"""Pydantic models used across the project."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Literal

from pydantic import BaseModel, Field


class Target(BaseModel):
    """Represents a validated root target."""

    root_domain: str


class DNSRecordSet(BaseModel):
    """DNS data collected for a host."""

    a_records: list[str] = Field(default_factory=list)
    aaaa_records: list[str] = Field(default_factory=list)
    cname_records: list[str] = Field(default_factory=list)
    mx_records: list[str] = Field(default_factory=list)
    ns_records: list[str] = Field(default_factory=list)
    resolution_errors: dict[str, str] = Field(default_factory=dict)


class SecurityHeaderCheck(BaseModel):
    """Individual security header finding."""

    header: str
    present: bool
    value: str | None = None
    explanation: str


class SecurityHeaderAssessment(BaseModel):
    """Aggregated header assessment."""

    checks: list[SecurityHeaderCheck] = Field(default_factory=list)

    @property
    def missing_count(self) -> int:
        return sum(1 for check in self.checks if not check.present)


class ExposureFinding(BaseModel):
    """Minimal exposure heuristic result."""

    path: str
    status_code: int
    reason: str
    confidence: Literal["low", "medium", "high"]


class HTTPProbeResult(BaseModel):
    """Result of probing a web service."""

    url: str
    scheme: Literal["http", "https"]
    final_url: str
    status_code: int
    title: str | None = None
    server: str | None = None
    x_powered_by: str | None = None
    content_type: str | None = None
    redirect_chain: list[str] = Field(default_factory=list)
    response_time_ms: float
    headers: dict[str, str] = Field(default_factory=dict)
    technologies: list[str] = Field(default_factory=list)
    security_headers: SecurityHeaderAssessment = Field(default_factory=SecurityHeaderAssessment)
    exposures: list[ExposureFinding] = Field(default_factory=list)
    error: str | None = None


class RiskAssessment(BaseModel):
    """Risk score and rationale."""

    score: int
    label: Literal["Low", "Medium", "High"]
    reasons: list[str] = Field(default_factory=list)


class SubdomainAsset(BaseModel):
    """Full asset view for a discovered subdomain."""

    hostname: str
    dns: DNSRecordSet = Field(default_factory=DNSRecordSet)
    http_services: list[HTTPProbeResult] = Field(default_factory=list)
    risk: RiskAssessment = Field(default_factory=lambda: RiskAssessment(score=0, label="Low", reasons=[]))


class ScanResult(BaseModel):
    """Top-level scan result."""

    target: Target
    disclaimer: str
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    subdomains: list[SubdomainAsset] = Field(default_factory=list)
    discovery_providers: list[str] = Field(default_factory=list)
    methodology: list[str] = Field(default_factory=list)


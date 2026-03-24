from datetime import datetime, timezone
from pathlib import Path

from surfacemapper.models import DNSRecordSet, RiskAssessment, ScanResult, SubdomainAsset, Target
from surfacemapper.reporting.json_report import resolve_results_path
from surfacemapper.reporting.markdown_report import render_markdown_report


def test_render_markdown_report_contains_target_and_disclaimer():
    result = ScanResult(
        target=Target(root_domain="example.com"),
        disclaimer="Authorized targets only.",
        generated_at=datetime(2026, 1, 1, tzinfo=timezone.utc),
        subdomains=[
            SubdomainAsset(
                hostname="example.com",
                dns=DNSRecordSet(a_records=["93.184.216.34"]),
                risk=RiskAssessment(score=1, label="Low", reasons=["Test reason"]),
            )
        ],
        discovery_providers=["crt.sh"],
        methodology=["Passive discovery"],
    )
    markdown = render_markdown_report(result)
    assert "example.com" in markdown
    assert "Authorized targets only." in markdown
    assert "Passive discovery" in markdown


def test_resolve_results_path_places_reports_under_results():
    assert resolve_results_path("custom/report.json") == Path("results/custom/report.json")

"""Markdown report rendering."""

from __future__ import annotations

from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from surfacemapper.models import ScanResult
from surfacemapper.reporting.json_report import resolve_results_path


TEMPLATE_DIR = Path(__file__).parent / "templates"


def render_markdown_report(result: ScanResult) -> str:
    """Render a Markdown report for a scan result."""

    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=select_autoescape(enabled_extensions=(), default_for_string=False),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template("report.md.j2")
    live_assets = sum(
        1
        for asset in result.subdomains
        for probe in asset.http_services
        if probe.status_code and not probe.error
    )
    highest_risk_label = max(
        (asset.risk.label for asset in result.subdomains),
        default="Low",
        key=lambda label: {"Low": 1, "Medium": 2, "High": 3}[label],
    )
    return template.render(result=result, live_assets=live_assets, highest_risk_label=highest_risk_label)


def save_markdown_report(result: ScanResult, destination: str | Path) -> Path:
    """Write a Markdown report to disk."""

    path = resolve_results_path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_markdown_report(result), encoding="utf-8")
    return path

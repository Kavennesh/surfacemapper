"""Typer CLI entrypoint."""

from __future__ import annotations

import sys
from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from surfacemapper import __version__
from surfacemapper.config import AUTHORIZED_USE_DISCLAIMER
from surfacemapper.core.orchestrator import scan_target
from surfacemapper.reporting.json_report import load_json_report, save_json_report
from surfacemapper.reporting.markdown_report import save_markdown_report


app = typer.Typer(
    help=(
        "SurfaceMapper maps externally visible assets for authorized targets only. "
        "It is passive-first, excludes exploitation features, and users are responsible for lawful use."
    )
)
console = Console()


def _supports_unicode_output() -> bool:
    """Return True when the current stdout encoding can safely render Unicode UI."""

    encoding = (sys.stdout.encoding or "").lower()
    return "utf" in encoding


def _render_summary(result) -> None:
    table = Table(title=f"SurfaceMapper Summary: {result.target.root_domain}")
    table.add_column("Asset")
    table.add_column("DNS")
    table.add_column("Live Services")
    table.add_column("Risk")
    for asset in result.subdomains:
        live_services = sum(1 for probe in asset.http_services if probe.status_code and not probe.error)
        dns_count = sum(
            len(records)
            for records in [
                asset.dns.a_records,
                asset.dns.aaaa_records,
                asset.dns.cname_records,
                asset.dns.mx_records,
                asset.dns.ns_records,
            ]
        )
        table.add_row(asset.hostname, str(dns_count), str(live_services), asset.risk.label)
    console.print(table)


@app.command()
def scan(
    domain: str = typer.Argument(..., help="Root domain to scan. Authorized targets only."),
    json_path: Path | None = typer.Option(None, "--json", help="Write a JSON report to this path."),
    md_path: Path | None = typer.Option(None, "--md", help="Write a Markdown report to this path."),
) -> None:
    """Run the full passive-first scan workflow."""

    console.print(f"[bold yellow]Disclaimer:[/bold yellow] {AUTHORIZED_USE_DISCLAIMER}")
    if _supports_unicode_output():
        console.print(f"Scanning [bold]{domain}[/bold]...")
    else:
        print(f"Scanning {domain}...")
    result = scan_target(domain)
    _render_summary(result)
    if json_path:
        saved = save_json_report(result, json_path)
        console.print(f"Saved JSON report to [bold]{saved}[/bold]")
    if md_path:
        saved = save_markdown_report(result, md_path)
        console.print(f"Saved Markdown report to [bold]{saved}[/bold]")


@app.command()
def report(
    json_source: Path = typer.Argument(..., help="Path to a saved JSON report."),
    md_path: Path = typer.Option(..., "--md", help="Destination Markdown file."),
) -> None:
    """Generate Markdown from a previously saved JSON report."""

    console.print(f"[bold yellow]Disclaimer:[/bold yellow] {AUTHORIZED_USE_DISCLAIMER}")
    result = load_json_report(json_source)
    saved = save_markdown_report(result, md_path)
    console.print(f"Saved Markdown report to [bold]{saved}[/bold]")


@app.command()
def version() -> None:
    """Print the package version."""

    console.print(__version__)


if __name__ == "__main__":
    app()

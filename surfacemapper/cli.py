"""Typer CLI entrypoint."""

from __future__ import annotations

import sys
from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from surfacemapper import __version__
from surfacemapper.config import AUTHORIZED_USE_DISCLAIMER
from surfacemapper.core.orchestrator import scan_target
from surfacemapper.reporting.json_report import load_json_report, resolve_results_path, save_json_report
from surfacemapper.reporting.markdown_report import save_markdown_report


app = typer.Typer(
    help=(
        "SurfaceMapper maps externally visible assets for authorized targets only. "
        "It is passive-first, excludes exploitation features, and users are responsible for lawful use."
    )
)
console = Console()

BANNER_ART = r"""
   _____             __                 __  ___
  / ___/__  ________/ /___ _________   /  |/  /___ _____  ____  ___  _____
  \__ \/ / / / ___/ / __ `/ ___/ _ \ / /|_/ / __ `/ __ \/ __ \/ _ \/ ___/
 ___/ / /_/ / /  / / /_/ / /__/  __// /  / / /_/ / /_/ / /_/ /  __/ /
/____/\__,_/_/  /_/\__,_/\___/\___//_/  /_/\__,_/ .___/ .___/\___/_/
                                                /_/   /_/
"""


def _supports_unicode_output() -> bool:
    """Return True when the current stdout encoding can safely render Unicode UI."""

    encoding = (sys.stdout.encoding or "").lower()
    return "utf" in encoding


def _print_banner() -> None:
    """Print the runtime branding banner."""

    if _supports_unicode_output():
        banner = Text.from_ansi(BANNER_ART)
        banner.stylize("bold bright_cyan")
        details = Text()
        details.append("Version: ", style="bold white")
        details.append(__version__, style="bold bright_blue")
        details.append("   ")
        details.append("Author: ", style="bold white")
        details.append("Kavennesh", style="bold bright_magenta")
        details.append("   ")
        details.append("Site: ", style="bold white")
        details.append("https://kavennesh.com", style="underline bright_cyan")
        panel = Panel.fit(
            Text.assemble(banner, "\n", details),
            border_style="bright_blue",
            title="[bold bright_magenta]SurfaceMapper[/bold bright_magenta]",
            subtitle="[bright_cyan]Passive-First Attack Surface Mapping[/bright_cyan]",
            padding=(1, 2),
        )
        console.print(panel)
    else:
        print("SurfaceMapper v0.1.0")
        print("By Kavennesh - https://kavennesh.com")


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


def _default_json_path(domain: str) -> Path:
    """Return the default JSON destination under results/."""

    return resolve_results_path(Path(f"{domain}.json"))


def _default_markdown_path(domain: str) -> Path:
    """Return the default Markdown destination under results/."""

    return resolve_results_path(Path(f"{domain}.md"))


@app.command()
def scan(
    domain: str = typer.Argument(..., help="Root domain to scan. Authorized targets only."),
    json_path: Path | None = typer.Option(None, "--json", help="JSON report filename. Saved under results/."),
    md_path: Path | None = typer.Option(None, "--md", help="Markdown report filename. Saved under results/."),
) -> None:
    """Run the full passive-first scan workflow."""

    _print_banner()
    console.print(f"[bold yellow]Disclaimer:[/bold yellow] {AUTHORIZED_USE_DISCLAIMER}")
    if _supports_unicode_output():
        console.print(f"Scanning [bold]{domain}[/bold]...")
    else:
        print(f"Scanning {domain}...")
    result = scan_target(domain)
    _render_summary(result)
    saved_json = save_json_report(result, json_path or _default_json_path(domain))
    saved_md = save_markdown_report(result, md_path or _default_markdown_path(domain))
    console.print(f"Saved JSON report to [bold]{saved_json}[/bold]")
    console.print(f"Saved Markdown report to [bold]{saved_md}[/bold]")


@app.command()
def report(
    json_source: Path = typer.Argument(..., help="Path to a saved JSON report."),
    md_path: Path | None = typer.Option(None, "--md", help="Markdown filename. Saved under results/."),
) -> None:
    """Generate Markdown from a previously saved JSON report."""

    _print_banner()
    console.print(f"[bold yellow]Disclaimer:[/bold yellow] {AUTHORIZED_USE_DISCLAIMER}")
    result = load_json_report(json_source)
    default_md = Path(f"{json_source.stem}.md")
    saved = save_markdown_report(result, md_path or default_md)
    console.print(f"Saved Markdown report to [bold]{saved}[/bold]")


@app.command()
def version() -> None:
    """Print the package version."""

    _print_banner()
    console.print(f"Version: {__version__}")


if __name__ == "__main__":
    app()

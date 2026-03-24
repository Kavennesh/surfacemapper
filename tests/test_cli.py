from pathlib import Path

from typer.testing import CliRunner

from surfacemapper.cli import app
from surfacemapper.models import ScanResult, Target


runner = CliRunner()


def test_scan_command_writes_json_and_markdown(monkeypatch):
    sample = ScanResult(
        target=Target(root_domain="example.com"),
        disclaimer="Authorized targets only.",
    )

    monkeypatch.setattr("surfacemapper.cli.scan_target", lambda domain: sample)

    with runner.isolated_filesystem():
        result = runner.invoke(app, ["scan", "example.com", "--json", "report.json", "--md", "report.md"])
        assert result.exit_code == 0
        assert Path("results/report.json").exists()
        assert Path("results/report.md").exists()


def test_report_command_regenerates_markdown(monkeypatch):
    payload = ScanResult(
        target=Target(root_domain="example.com"),
        disclaimer="Authorized targets only.",
    )

    with runner.isolated_filesystem():
        from surfacemapper.reporting.json_report import save_json_report

        save_json_report(payload, "report.json")
        result = runner.invoke(app, ["report", "results/report.json", "--md", "regenerated.md"])
        assert result.exit_code == 0
        assert Path("results/regenerated.md").exists()

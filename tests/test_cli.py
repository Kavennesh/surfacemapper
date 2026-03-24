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
        result = runner.invoke(app, ["scan", "example.com", "--json", "out/report.json", "--md", "out/report.md"])
        assert result.exit_code == 0
        assert Path("out/report.json").exists()
        assert Path("out/report.md").exists()


def test_report_command_regenerates_markdown(monkeypatch):
    payload = ScanResult(
        target=Target(root_domain="example.com"),
        disclaimer="Authorized targets only.",
    )

    with runner.isolated_filesystem():
        from surfacemapper.reporting.json_report import save_json_report

        save_json_report(payload, "out/report.json")
        result = runner.invoke(app, ["report", "out/report.json", "--md", "out/regenerated.md"])
        assert result.exit_code == 0
        assert Path("out/regenerated.md").exists()

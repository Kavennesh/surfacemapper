# SurfaceMapper

SurfaceMapper is a production-quality, passive-first attack surface mapping CLI for authorized targets only. It helps defenders, security students, and red teamers map externally visible assets, collect lightweight metadata, and generate structured reports without introducing exploit delivery, brute force, stealth, credential attacks, phishing, or persistence behavior.

Author: Kavennesh  
Website: https://kavennesh.com

## Ethics And Legal Notice

SurfaceMapper is for authorized targets only.

- Passive-first design
- No exploitation features
- No brute forcing, credential attacks, phishing, payloads, persistence, or stealth/evasion
- Users are solely responsible for lawful and ethical use

If you do not have explicit permission to assess a target, do not use this tool against it.

## Project Overview

Given a root domain such as `example.com`, SurfaceMapper:

- Collects subdomains through passive methods
- Resolves common DNS records
- Probes HTTP and HTTPS services conservatively
- Extracts titles, headers, redirects, and simple technology hints
- Checks important security headers
- Flags a small set of common exposure paths
- Assigns transparent rule-based risk labels
- Exports JSON and Markdown reports

## Resume-Friendly Project Description

SurfaceMapper is a Python security engineering project focused on safe external asset discovery and security reporting. It demonstrates modular CLI design, structured data modeling, conservative HTTP and DNS collection, transparent risk scoring, templated report generation, and test-driven quality controls suitable for a public GitHub portfolio.

## Features

- Root-domain validation and normalization
- Passive subdomain discovery via `crt.sh`
- DNS resolution for `A`, `AAAA`, `CNAME`, `MX`, and `NS`
- Lightweight HTTP and HTTPS probing with a custom user agent
- Metadata collection for final URL, status, title, redirects, headers, and response time
- Conservative technology hints from HTML and headers
- Security header checks for six common defensive headers
- Minimal safe-list path checks for `/admin`, `/login`, `/dashboard`, and `/wp-login.php`
- Transparent `Low` / `Medium` / `High` rule-based risk labels
- JSON and Markdown report generation
- Rich terminal summary output
- Pytest coverage for validators, parsing, headers, risk logic, and reporting

## Architecture

```text
surfacemapper/
  surfacemapper/
    cli.py
    config.py
    models.py
    validators.py
    core/
    discovery/
    dns/
    probing/
    reporting/
    utils/
  tests/
```

Design principles:

- Passive-first collection before lightweight probing
- Small, focused modules with clear separation of concerns
- Pydantic models for structured outputs
- Conservative heuristics with visible rationale
- Safe defaults that are reasonable for public open source

## Installation

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e .[dev]
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .[dev]
```

## Usage

```bash
surfacemapper scan example.com
surfacemapper scan example.com --json example.json --md example.md
surfacemapper report results/example.json --md regenerated.md
surfacemapper version
```

CLI help text and generated reports include the authorized-use disclaimer. All saved reports are written under the `results/` directory.

## Sample Terminal Summary

```text
SurfaceMapper Summary: example.com
┏━━━━━━━━━━━━━━━━━━┳━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Asset            ┃ DNS ┃ Live Services ┃ Risk   ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ example.com      │ 3   │ 2             │ Medium │
│ admin.example.com│ 2   │ 1             │ High   │
└──────────────────┴─────┴───────────────┴────────┘
```

## Methodology

1. Validate and normalize the supplied root domain.
2. Query `crt.sh` for passive certificate-transparency subdomain candidates.
3. Resolve common DNS record types safely with graceful error handling.
4. Probe HTTP and HTTPS using modest defaults and lightweight requests.
5. Evaluate security headers and conservative technology hints.
6. Check a short safe-list of common login and admin-style paths.
7. Generate JSON and Markdown output with transparent risk rationales.

## Developer Notes

- Python 3.11+
- CLI built with Typer and Rich
- Networking via `httpx` and `dnspython`
- Structured data via Pydantic
- Reports rendered through Jinja2
- Tests written with `pytest`

## Roadmap

- Additional passive providers behind a common interface
- Optional caching for passive discovery responses
- Customizable exposure path lists and scoring rules
- Differential reports between multiple scan runs
- Optional CSV export

## Future Improvements

- Add more passive sources such as additional certificate-transparency feeds and commercial APIs behind pluggable providers
- Introduce opt-in caching and historical comparison to track asset drift over time
- Expand report views with filtering, severity summaries, and delta reporting

## Resume Bullet Options

- Built a passive-first Python attack surface mapping CLI that discovers subdomains, resolves DNS, probes HTTP metadata, and generates JSON and Markdown security reports with transparent risk scoring.
- Engineered a modular reconnaissance and reporting pipeline using Typer, Rich, httpx, dnspython, Pydantic, Jinja2, and pytest, with explicit safe-by-default constraints for public open-source release.
- Designed a security tooling project that balances defensive utility and responsible scope through conservative fingerprinting, header analysis, exposure heuristics, and structured test coverage.

## GitHub Repo Description Options

- Passive-first attack surface mapping for authorized targets only
- Safe external asset discovery and reporting for defenders and students
- Lightweight domain mapping with transparent security heuristics

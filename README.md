<div align="center">

```
╔══════════════════════════════════════════════════════════╗
║  ███████╗██╗   ██╗██████╗ ███████╗ █████╗  ██████╗███████╗║
║  ██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝║
║  ███████╗██║   ██║██████╔╝█████╗  ███████║██║     █████╗  ║
║  ╚════██║██║   ██║██╔══██╗██╔══╝  ██╔══██║██║     ██╔══╝  ║
║  ███████║╚██████╔╝██║  ██║██║     ██║  ██║╚██████╗███████╗║
║  ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝║
║               M A P P E R                                   ║
╚══════════════════════════════════════════════════════════╝
```

**Passive-first attack surface mapping for authorized targets only**

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Authorized Only](https://img.shields.io/badge/Use-Authorized_Targets_Only-ef4444?style=for-the-badge)](https://kavennesh.com)
[![Author](https://img.shields.io/badge/Author-Kavennesh-8b5cf6?style=for-the-badge)](https://kavennesh.com)

</div>

---

## 🚀 Quick Start

```bash
surfacemapper scan example.com
```

What happens:

- 🎨 Prints the project banner with your name and website
- ✅ Validates the root domain
- 🔍 Gathers passive subdomains from `crt.sh`
- 🌐 Resolves DNS records
- 📡 Probes HTTP/HTTPS metadata
- 📄 Saves JSON and Markdown reports in `results/`

---

## ⚖️ Ethics & Legal Notice

> **SurfaceMapper is for authorized targets only.**

| ✅ What it does | ❌ What it never does |
|---|---|
| Passive-first design | Exploitation features |
| DNS resolution | Brute forcing |
| Header analysis | Credential attacks |
| Risk labeling | Phishing or payload delivery |
| Clean reporting | Persistence or evasion |

**If you do not have explicit permission to assess a target, do not use this tool against it.**

---

## 📖 Usage Guide

### ⚡ Quick Scan

```bash
surfacemapper scan example.com
```

Outputs → `results/example.com.json` · `results/example.com.md`

### 📝 Custom Report Names

```bash
surfacemapper scan example.com --json client-scan.json --md client-scan.md
```

Outputs → `results/client-scan.json` · `results/client-scan.md`

### 🔄 Regenerate Markdown

```bash
surfacemapper report results/example.com.json --md refreshed.md
```

Output → `results/refreshed.md`

### ℹ️ Check Version

```bash
surfacemapper version
```

---

## 🛠️ Installation

### Linux & macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
```

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .[dev]
```

### Verify Installation

```bash
python -m pytest
surfacemapper version
```

You should see the SurfaceMapper banner, **Kavennesh**, **https://kavennesh.com**, and the current version.

---

## ✨ Core Features

| Feature | Description |
|---|---|
| 🔎 **Subdomain Discovery** | Passive collection via `crt.sh` |
| 🌐 **DNS Resolution** | `A`, `AAAA`, `CNAME`, `MX`, `NS` records |
| 📡 **HTTP/HTTPS Probing** | Titles, status codes, redirects, response times |
| 🔒 **Security Headers** | CSP, HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy |
| 🚨 **Exposure Checks** | `/admin`, `/login`, `/dashboard`, `/wp-login.php` |
| 🏷️ **Risk Labels** | Transparent rule-based scoring |
| 📊 **Rich Reports** | JSON + Markdown with terminal summaries |
| 💡 **Tech Hints** | Conservative heuristics from headers and HTML |

---

## 🧠 How SurfaceMapper Thinks

```
1. Validate target domain
       ↓
2. Discover passive subdomains (crt.sh)
       ↓
3. Resolve DNS records safely
       ↓
4. Probe HTTP/HTTPS conservatively
       ↓
5. Check headers & tech hints
       ↓
6. Scan likely admin/login paths
       ↓
7. Score findings with clear rules
       ↓
8. Save results to results/
```

---

## 📋 Example CLI Output

```
SurfaceMapper v0.1.0
By Kavennesh — https://kavennesh.com

Disclaimer: SurfaceMapper is for authorized targets only...

Scanning example.com...

┌─────────────────────────────────────────────┐
│  SurfaceMapper Summary: example.com         │
├──────────────────┬──────────────────────────┤
│  Subdomains      │  12 discovered            │
│  Live Hosts      │  8 responding             │
│  Risk Level      │  Medium                   │
└──────────────────┴──────────────────────────┘

Saved JSON report to results/example.com.json
Saved Markdown report to results/example.com.md
```

---

## 📂 Report Contents

### JSON Report

- Target details & discovery providers
- Discovered subdomains
- DNS records
- HTTP probe results
- Security header assessment
- Exposure findings
- Risk scoring rationale

### Markdown Report

- Target summary & discovered assets
- DNS findings & live web metadata
- Security header results
- Exposure findings
- Risk summary
- Methodology & disclaimer

---

## 🏗️ Project Structure

```
surfacemapper/
├── surfacemapper/
│   ├── cli.py
│   ├── config.py
│   ├── models.py
│   ├── validators.py
│   ├── core/
│   ├── discovery/
│   ├── dns/
│   ├── probing/
│   ├── reporting/
│   └── utils/
├── tests/
└── results/
```

---

## ⚙️ Tech Stack

| Layer | Library |
|---|---|
| CLI | Typer |
| Terminal UI | Rich |
| HTTP Probing | httpx |
| DNS Lookups | dnspython |
| Data Models | Pydantic |
| Templating | Jinja2 |
| Testing | pytest |
| Language | Python 3.11+ |

---

## 🗺️ Roadmap

- [ ] More passive discovery providers behind a shared interface
- [ ] Optional caching for discovery and scan reuse
- [ ] Scan comparisons between historical runs
- [ ] Expanded reporting views and filtering
- [ ] CSV export
- [ ] Asset drift tracking over time

---

## 💬 GitHub Repo Description

> *Passive-first attack surface mapping for authorized targets only*

---

<div align="center">

Made with 🛡️ by **[Kavennesh](https://kavennesh.com)**

*Defenders first. Always authorized. No exploitation.*

</div>

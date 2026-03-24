"""HTTP probing implementation."""

from __future__ import annotations

import time
from urllib.parse import urlsplit

import httpx

from surfacemapper.config import AppConfig
from surfacemapper.models import HTTPProbeResult
from surfacemapper.probing.headers import assess_security_headers
from surfacemapper.probing.paths import check_exposure_paths
from surfacemapper.probing.tech_fingerprint import infer_technologies
from surfacemapper.utils.text import extract_html_title


def probe_host(hostname: str, config: AppConfig) -> list[HTTPProbeResult]:
    """Probe a host over the configured schemes."""

    return [
        probe_url(f"{scheme}://{hostname}", scheme=scheme, config=config)
        for scheme in config.probe_schemes
    ]


def probe_url(url: str, *, scheme: str, config: AppConfig) -> HTTPProbeResult:
    """Perform a lightweight request to collect safe metadata."""

    headers = {"User-Agent": config.user_agent}
    limits = httpx.Limits(
        max_keepalive_connections=config.max_concurrency,
        max_connections=config.max_concurrency,
    )
    timeout = httpx.Timeout(config.http_timeout)

    try:
        with httpx.Client(
            timeout=timeout,
            headers=headers,
            follow_redirects=config.http_follow_redirects,
            max_redirects=config.http_max_redirects,
            limits=limits,
        ) as client:
            started = time.perf_counter()
            response = client.get(url)
            elapsed_ms = round((time.perf_counter() - started) * 1000, 2)
            body = response.text[: config.http_max_body_bytes]
            response_headers = {key: value for key, value in response.headers.items()}
            security_headers = assess_security_headers(response_headers, config)
            exposures = []
            if response.status_code < 500:
                parsed = urlsplit(str(response.url))
                base_url = f"{parsed.scheme}://{parsed.netloc}"
                exposures = check_exposure_paths(client, base_url, config.exposure_paths)
            return HTTPProbeResult(
                url=url,
                scheme=scheme,
                final_url=str(response.url),
                status_code=response.status_code,
                title=extract_html_title(body),
                server=response.headers.get("server"),
                x_powered_by=response.headers.get("x-powered-by"),
                content_type=response.headers.get("content-type"),
                redirect_chain=[str(item.url) for item in response.history] + [str(response.url)],
                response_time_ms=elapsed_ms,
                headers=response_headers,
                technologies=infer_technologies(response_headers, body, config),
                security_headers=security_headers,
                exposures=exposures,
            )
    except httpx.HTTPError as exc:
        return HTTPProbeResult(
            url=url,
            scheme=scheme,
            final_url=url,
            status_code=0,
            response_time_ms=0.0,
            error=str(exc),
        )

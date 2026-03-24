"""Application configuration values."""

from __future__ import annotations

from dataclasses import dataclass, field


AUTHORIZED_USE_DISCLAIMER = (
    "SurfaceMapper is for authorized targets only. It is passive-first, excludes "
    "exploitation features, and users are responsible for lawful use."
)


@dataclass(slots=True)
class AppConfig:
    """Runtime configuration for scanning behavior."""

    user_agent: str = "SurfaceMapper/0.1.0 (+https://github.com/example/surfacemapper)"
    http_timeout: float = 8.0
    http_follow_redirects: bool = True
    http_max_redirects: int = 5
    http_max_body_bytes: int = 65536
    max_subdomains: int = 200
    max_concurrency: int = 5
    probe_schemes: tuple[str, ...] = ("https", "http")
    exposure_paths: tuple[str, ...] = ("/admin", "/login", "/dashboard", "/wp-login.php")
    dns_record_types: tuple[str, ...] = ("A", "AAAA", "CNAME", "MX", "NS")
    security_headers: tuple[str, ...] = (
        "Content-Security-Policy",
        "Strict-Transport-Security",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy",
        "Permissions-Policy",
    )
    tech_markers: dict[str, tuple[str, ...]] = field(
        default_factory=lambda: {
            "Cloudflare": ("cloudflare", "__cf_bm", "cf-ray"),
            "nginx": ("nginx",),
            "Apache": ("apache",),
            "React": ("react", "__next", "data-reactroot"),
            "WordPress": ("wp-content", "wordpress", "wp-json"),
            "PHP": ("php",),
            "ASP.NET": ("asp.net", "x-aspnet-version", "__viewstate"),
        }
    )


DEFAULT_CONFIG = AppConfig()


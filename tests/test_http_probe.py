import httpx
import pytest

from surfacemapper.config import DEFAULT_CONFIG
from surfacemapper.probing.http_probe import probe_url


def test_probe_url_collects_metadata_with_mock_transport(monkeypatch: pytest.MonkeyPatch):
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/login":
            return httpx.Response(200, text="login page", request=request)
        html = "<html><title>Example</title><meta name='generator' content='WordPress'></html>"
        headers = {
            "server": "nginx",
            "x-powered-by": "PHP/8.2",
            "content-type": "text/html",
            "x-frame-options": "DENY",
        }
        return httpx.Response(200, text=html, headers=headers, request=request)

    transport = httpx.MockTransport(handler)

    class MockClient(httpx.Client):
        def __init__(self, *args, **kwargs):
            kwargs["transport"] = transport
            super().__init__(*args, **kwargs)

    monkeypatch.setattr(httpx, "Client", MockClient)
    result = probe_url("https://example.com", scheme="https", config=DEFAULT_CONFIG)

    assert result.status_code == 200
    assert result.title == "Example"
    assert "WordPress" in result.technologies
    assert any(finding.path == "/login" for finding in result.exposures)

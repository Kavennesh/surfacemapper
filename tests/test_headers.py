from surfacemapper.config import DEFAULT_CONFIG
from surfacemapper.probing.headers import assess_security_headers


def test_assess_security_headers_marks_presence_and_missing():
    result = assess_security_headers(
        {
            "Content-Security-Policy": "default-src 'self'",
            "X-Frame-Options": "DENY",
        },
        DEFAULT_CONFIG,
    )
    present = {check.header for check in result.checks if check.present}
    missing = {check.header for check in result.checks if not check.present}
    assert "Content-Security-Policy" in present
    assert "X-Frame-Options" in present
    assert "Strict-Transport-Security" in missing


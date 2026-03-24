from surfacemapper.core.risk import assess_asset_risk
from surfacemapper.models import ExposureFinding, HTTPProbeResult, SecurityHeaderAssessment, SecurityHeaderCheck


def test_assess_asset_risk_scores_combined_findings():
    probe = HTTPProbeResult(
        url="https://admin.example.com",
        scheme="https",
        final_url="https://admin.example.com/login",
        status_code=200,
        response_time_ms=100.0,
        server="nginx",
        security_headers=SecurityHeaderAssessment(
            checks=[SecurityHeaderCheck(header=f"h{i}", present=False, explanation="test") for i in range(4)]
        ),
        exposures=[
            ExposureFinding(
                path="/login",
                status_code=200,
                reason="Authentication endpoint pattern",
                confidence="medium",
            )
        ],
    )
    result = assess_asset_risk([probe])
    assert result.label == "High"
    assert result.score >= 6


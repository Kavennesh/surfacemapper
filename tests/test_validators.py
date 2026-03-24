import pytest

from surfacemapper.validators import belongs_to_root, validate_root_domain


def test_validate_root_domain_normalizes_case_and_whitespace():
    assert validate_root_domain(" Example.COM ") == "example.com"


def test_validate_root_domain_rejects_urls():
    with pytest.raises(ValueError):
        validate_root_domain("https://example.com")


def test_belongs_to_root_accepts_subdomain():
    assert belongs_to_root("api.example.com", "example.com") is True


def test_belongs_to_root_rejects_other_domains():
    assert belongs_to_root("evil-example.com", "example.com") is False


from surfacemapper.discovery.crtsh import parse_crtsh_entries


def test_parse_crtsh_entries_filters_and_deduplicates():
    entries = [
        {"name_value": "*.example.com\napi.example.com"},
        {"name_value": "admin.example.com"},
        {"name_value": "other.org"},
    ]
    assert parse_crtsh_entries(entries, root_domain="example.com") == [
        "admin.example.com",
        "api.example.com",
        "example.com",
    ]


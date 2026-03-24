"""DNS resolution helpers."""

from __future__ import annotations

import dns.exception
import dns.resolver

from surfacemapper.config import AppConfig
from surfacemapper.models import DNSRecordSet


RECORD_FIELD_MAP = {
    "A": "a_records",
    "AAAA": "aaaa_records",
    "CNAME": "cname_records",
    "MX": "mx_records",
    "NS": "ns_records",
}


def resolve_record_set(hostname: str, config: AppConfig) -> DNSRecordSet:
    """Resolve common DNS record types without failing the whole scan."""

    record_set = DNSRecordSet()
    resolver = dns.resolver.Resolver(configure=True)
    resolver.lifetime = config.http_timeout
    resolver.timeout = config.http_timeout

    for record_type in config.dns_record_types:
        try:
            answers = resolver.resolve(hostname, record_type)
            setattr(record_set, RECORD_FIELD_MAP[record_type], [str(answer).rstrip(".") for answer in answers])
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            continue
        except (dns.resolver.NoNameservers, dns.exception.Timeout, dns.resolver.YXDOMAIN) as exc:
            record_set.resolution_errors[record_type] = exc.__class__.__name__
        except Exception as exc:
            record_set.resolution_errors[record_type] = str(exc)
    return record_set

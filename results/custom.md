# SurfaceMapper Report

**Target:** `example.com`
**Generated:** `2026-03-24T16:20:14.224105+00:00`
**Discovery Providers:** crt.sh
**Live Web Assets:** 2

## Disclaimer

SurfaceMapper is for authorized targets only. It is passive-first, excludes exploitation features, and users are responsible for lawful use.

## Summary

- Subdomains discovered: 6
- Highest risk label: Low

## Subdomains

### dev.example.com

- Risk: Low (score 0)
- Risk reasons: None
- A: None
- AAAA: None
- CNAME: None
- MX: None
- NS: None

#### https://dev.example.com

- Status: Unavailable
- Final URL: https://dev.example.com
- Title: None
- Server: None
- X-Powered-By: None
- Content-Type: None
- Response Time: 0.0 ms
- Technologies: None
- Redirect Chain: None
- Error: [Errno 11001] getaddrinfo failed

Security headers:

Exposure findings:
- None

#### http://dev.example.com

- Status: Unavailable
- Final URL: http://dev.example.com
- Title: None
- Server: None
- X-Powered-By: None
- Content-Type: None
- Response Time: 0.0 ms
- Technologies: None
- Redirect Chain: None
- Error: [Errno 11001] getaddrinfo failed

Security headers:

Exposure findings:
- None

### example.com

- Risk: Low (score 2)
- Risk reasons: Multiple recommended security headers missing on http://example.com.
- A: 104.18.26.120, 104.18.27.120
- AAAA: 2606:4700::6812:1b78, 2606:4700::6812:1a78
- CNAME: None
- MX: 0 
- NS: elliott.ns.cloudflare.com, hera.ns.cloudflare.com

#### https://example.com

- Status: Unavailable
- Final URL: https://example.com
- Title: None
- Server: None
- X-Powered-By: None
- Content-Type: None
- Response Time: 0.0 ms
- Technologies: None
- Redirect Chain: None
- Error: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)

Security headers:

Exposure findings:
- None

#### http://example.com

- Status: 200
- Final URL: http://example.com
- Title: Example Domain
- Server: cloudflare
- X-Powered-By: None
- Content-Type: text/html
- Response Time: 68.41 ms
- Technologies: Cloudflare
- Redirect Chain: http://example.com
- Error: None

Security headers:
- Content-Security-Policy: missing - Helps restrict script and content execution sources.
- Strict-Transport-Security: missing - Helps enforce HTTPS usage in supporting browsers.
- X-Frame-Options: missing - Helps reduce clickjacking exposure.
- X-Content-Type-Options: missing - Helps prevent MIME type sniffing.
- Referrer-Policy: missing - Controls referrer data shared with other origins.
- Permissions-Policy: missing - Restricts access to selected browser features.

Exposure findings:
- None

### m.example.com

- Risk: Low (score 0)
- Risk reasons: None
- A: None
- AAAA: None
- CNAME: None
- MX: None
- NS: None

#### https://m.example.com

- Status: Unavailable
- Final URL: https://m.example.com
- Title: None
- Server: None
- X-Powered-By: None
- Content-Type: None
- Response Time: 0.0 ms
- Technologies: None
- Redirect Chain: None
- Error: [Errno 11001] getaddrinfo failed

Security headers:

Exposure findings:
- None

#### http://m.example.com

- Status: Unavailable
- Final URL: http://m.example.com
- Title: None
- Server: None
- X-Powered-By: None
- Content-Type: None
- Response Time: 0.0 ms
- Technologies: None
- Redirect Chain: None
- Error: [Errno 11001] getaddrinfo failed

Security headers:

Exposure findings:
- None

### products.example.com

- Risk: Low (score 0)
- Risk reasons: None
- A: None
- AAAA: None
- CNAME: None
- MX: None
- NS: None

#### https://products.example.com

- Status: Unavailable
- Final URL: https://products.example.com
- Title: None
- Server: None
- X-Powered-By: None
- Content-Type: None
- Response Time: 0.0 ms
- Technologies: None
- Redirect Chain: None
- Error: [Errno 11001] getaddrinfo failed

Security headers:

Exposure findings:
- None

#### http://products.example.com

- Status: Unavailable
- Final URL: http://products.example.com
- Title: None
- Server: None
- X-Powered-By: None
- Content-Type: None
- Response Time: 0.0 ms
- Technologies: None
- Redirect Chain: None
- Error: [Errno 11001] getaddrinfo failed

Security headers:

Exposure findings:
- None

### support.example.com

- Risk: Low (score 0)
- Risk reasons: None
- A: None
- AAAA: None
- CNAME: None
- MX: None
- NS: None

#### https://support.example.com

- Status: Unavailable
- Final URL: https://support.example.com
- Title: None
- Server: None
- X-Powered-By: None
- Content-Type: None
- Response Time: 0.0 ms
- Technologies: None
- Redirect Chain: None
- Error: [Errno 11001] getaddrinfo failed

Security headers:

Exposure findings:
- None

#### http://support.example.com

- Status: Unavailable
- Final URL: http://support.example.com
- Title: None
- Server: None
- X-Powered-By: None
- Content-Type: None
- Response Time: 0.0 ms
- Technologies: None
- Redirect Chain: None
- Error: [Errno 11001] getaddrinfo failed

Security headers:

Exposure findings:
- None

### www.example.com

- Risk: Low (score 2)
- Risk reasons: Multiple recommended security headers missing on http://www.example.com.
- A: 104.18.27.120, 104.18.26.120
- AAAA: 2606:4700::6812:1a78, 2606:4700::6812:1b78
- CNAME: None
- MX: None
- NS: None

#### https://www.example.com

- Status: Unavailable
- Final URL: https://www.example.com
- Title: None
- Server: None
- X-Powered-By: None
- Content-Type: None
- Response Time: 0.0 ms
- Technologies: None
- Redirect Chain: None
- Error: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)

Security headers:

Exposure findings:
- None

#### http://www.example.com

- Status: 200
- Final URL: http://www.example.com
- Title: Example Domain
- Server: cloudflare
- X-Powered-By: None
- Content-Type: text/html
- Response Time: 21.71 ms
- Technologies: Cloudflare
- Redirect Chain: http://www.example.com
- Error: None

Security headers:
- Content-Security-Policy: missing - Helps restrict script and content execution sources.
- Strict-Transport-Security: missing - Helps enforce HTTPS usage in supporting browsers.
- X-Frame-Options: missing - Helps reduce clickjacking exposure.
- X-Content-Type-Options: missing - Helps prevent MIME type sniffing.
- Referrer-Policy: missing - Controls referrer data shared with other origins.
- Permissions-Policy: missing - Restricts access to selected browser features.

Exposure findings:
- None


## Methodology

- Validated the root domain and rejected URL-style input.
- Collected passive subdomains from crt.sh.
- Resolved A, AAAA, CNAME, MX, and NS records.
- Probed HTTP and HTTPS with lightweight metadata collection only.
- Assessed security headers, exposure paths, and conservative technology hints.
- Assigned transparent rule-based risk labels.

# OWASP Top 10:2021 Vulnerability Mapping

This taxonomy matrix indexes all challenges in OWASP Juice Shop by their corresponding **OWASP Top 10:2021** standard category.

---

## 🗂️ Category Mapping Index

### A01:2021 - Broken Access Control
- Insecure Direct Object References (IDOR): Accessing other users' shopping baskets.
- Vertical & Horizontal Privilege Escalation.
- Confidential Document Exposure (`/ftp` directory traversal).
- Unvalidated Redirects & Forwards.

### A02:2021 - Cryptographic Failures
- Weak password hashing algorithms (MD5).
- Exposed private keys & unprotected JWT secrets.
- Insecure direct file downloads of cryptographic keys.

### A03:2021 - Injection
- SQL Injection: Authentication bypass, union-based schema leakage.
- Cross-Site Scripting (XSS): DOM-based, Reflected, and Stored XSS vectors.
- NoSQL Injection: MongoDB parameter manipulation.
- Server-Side Template Injection (SSTI) & Command Injection.

### A04:2021 - Insecure Design
- Bypassing client-side star rating limits (Zero Stars Feedback).
- Repetitive password registration validation bypass.
- Business logic bypass in promo codes and wallet checkout.

### A05:2021 - Security Misconfiguration
- Default administrative credentials.
- Verbose stack traces and debug error message disclosure.
- Unprotected cloud storage buckets and API endpoints.

### A06:2021 - Vulnerable and Outdated Components
- Known CVE exploitation in outdated npm dependencies.
- XML External Entity (XXE) in legacy XML parsing libraries.

### A07:2021 - Identification and Authentication Failures
- Weak password reset security questions.
- Missing rate limiting on login endpoints (Brute-force risk).
- Insecure multi-factor authentication (MFA) implementation.

### A08:2021 - Software and Data Integrity Failures
- Insecure deserialization in user-controlled serialized state.
- Unsigned or self-signed JWT token acceptance (`alg: none`).

### A09:2021 - Security Logging and Monitoring Failures
- Failure to log unauthorized access attempts.
- Inadequate audit trails on financial and administrative transactions.

### A10:2021 - Server-Side Request Forgery (SSRF)
- Bypassing internal whitelist checks to query loopback interfaces.
- Interacting with cloud instance metadata services via profile image uploads.


# Tier 1 Challenges (★☆☆☆☆☆)

Tier 1 challenges focus on **information gathering, client-side application architecture reconnaissance, insecure direct error handling, and basic input validation flaws**.

---

## 📋 Challenge List & Tracking

| Challenge Name | Category | OWASP Top 10 | Status | Link |
| :--- | :--- | :--- | :---: | :---: |
| **Score Board Discovery** | Miscellaneous | A05: Security Misconfig | ✅ Completed | [Read Write-up](score-board.md) |
| **Error Handling Leak** | Security Misconfiguration | A05: Security Misconfig | ⏳ Planned | Planned |
| **Confidential Document Exposure** | Sensitive Data Exposure | A01: Broken Access Control | ⏳ Planned | Planned |
| **DOM XSS** | Cross-Site Scripting (XSS) | A03: Injection | ⏳ Planned | Planned |
| **Repetitive Registration** | Improper Input Validation | A04: Insecure Design | ⏳ Planned | Planned |
| **Zero Stars Feedback** | Improper Input Validation | A04: Insecure Design | ⏳ Planned | Planned |
| **Privacy Policy Inspection** | Miscellaneous | A05: Security Misconfig | ⏳ Planned | Planned |
| **Outdated Whitelist** | Unvalidated Redirects | A01: Broken Access Control | ⏳ Planned | Planned |
| **Mass Assignment (Bonus Payload)** | Vulnerable Components | A06: Vulnerable Components | ⏳ Planned | Planned |
| **Bullshit Code Disclosure** | Sensitive Data Exposure | A01: Broken Access Control | ⏳ Planned | Planned |

---

## 🎯 Primary Learning Objectives for Tier 1
1. **Single Page Application (SPA) Reconnaissance:** How Angular bundles routing tables into client-side JavaScript (`main.js`).
2. **Client-side vs Server-side Controls:** Why frontend form validation is completely untrusted without backend enforcement.
3. **Information Leakage via Unhandled Exceptions:** How verbose stack traces expose internal database technologies and file structures.


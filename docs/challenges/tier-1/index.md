# Tier 1 Challenges (★☆☆☆☆☆)

Tier 1 challenges focus on **information gathering, client-side application architecture reconnaissance, insecure direct error handling, and basic input validation flaws**.

---

## 📋 Challenge List & Tracking

| Challenge Name | Category | OWASP Top 10 | Status | Link |
| :--- | :--- | :--- | :---: | :---: |
| **Score Board Discovery** | Miscellaneous | A05: Security Misconfig | ✅ Completed | [Read Write-up](score-board.md) |
| **Error Handling Leak** | Security Misconfiguration | A05: Security Misconfig | ✅ Completed | [Read Write-up](error-handling.md) |
| **Confidential Document Exposure** | Sensitive Data Exposure | A01: Broken Access Control | ✅ Completed | [Read Write-up](confidential-document.md) |
| **DOM XSS** | Cross-Site Scripting (XSS) | A03: Injection | ✅ Completed | [Read Write-up](dom-xss.md) |
| **Bonus Payload** | Cross-Site Scripting (XSS) | A03: Injection | ✅ Completed | [Read Write-up](bonus-payload.md) |
| **Repetitive Registration** | Improper Input Validation | A04: Insecure Design | ✅ Completed | [Read Write-up](repetitive-registration.md) |
| **Zero Stars Feedback** | Improper Input Validation | A04: Insecure Design | ✅ Completed | [Read Write-up](zero-stars.md) |
| **Privacy Policy Inspection** | Miscellaneous | A05: Security Misconfig | ✅ Completed | [Read Write-up](privacy-policy.md) |
| **Outdated Whitelist** | Unvalidated Redirects | A01: Broken Access Control | ✅ Completed | [Read Write-up](outdated-whitelist.md) |
| **Exposed Metrics** | Security Misconfiguration | A05: Security Misconfig | ✅ Completed | [Read Write-up](exposed-metrics.md) |
| **Bully Chatbot** | Logic Flaw / Prompt Injection | A04: Insecure Design | ⏳ Skipped (API Key) | Skipped |

---

## 🎯 Primary Learning Objectives for Tier 1
1. **Single Page Application (SPA) Reconnaissance:** How Angular bundles routing tables into client-side JavaScript (`main.js`).
2. **Client-side vs Server-side Controls:** Why frontend form validation is completely untrusted without backend enforcement.
3. **Information Leakage via Unhandled Exceptions:** How verbose stack traces expose internal database technologies and file structures.


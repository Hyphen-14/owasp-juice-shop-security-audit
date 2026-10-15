# Secure Coding Guidelines: Node.js, Express & Angular

This guide consolidates defensive engineering principles and remediation patterns identified across the OWASP Juice Shop application security assessment.

---

## 1. Backend Security: Express & Node.js

### 1.1 SQL & NoSQL Injection Defense
- **Sequelize ORM Parameterization:** Never concatenate untrusted strings into raw SQL queries.
  ```typescript
  // ❌ VULNERABLE
  sequelize.query(`SELECT * FROM Products WHERE id = ${req.params.id}`);

  // ✅ SECURE
  sequelize.query('SELECT * FROM Products WHERE id = :id', {
    replacements: { id: req.params.id },
    type: QueryTypes.SELECT
  });
  ```
- **NoSQL Query Sanitization:** Use `mongo-sanitize` to strip `$` and `.` operators from request bodies to prevent operator injection (`{"$gt": ""}`).

### 1.2 Access Control & Authorization (IDOR Defense)
- Always validate that the authenticated user (`req.user.id`) owns the requested object before fetching or mutating records.
  ```typescript
  // ❌ VULNERABLE (IDOR)
  const basket = await BasketModel.findByPk(req.params.basketId);

  // ✅ SECURE
  const basket = await BasketModel.findOne({
    where: {
      id: req.params.basketId,
      UserId: req.user.id
    }
  });
  if (!basket) return res.status(404).json({ error: "Basket not found" });
  ```

### 1.3 Security Headers & Middleware
- Integrate **Helmet.js** to automatically set modern HTTP defense headers:
  ```javascript
  const helmet = require('helmet');
  app.use(helmet({
    contentSecurityPolicy: {
      directives: {
        defaultSrc: ["'self'"],
        scriptSrc: ["'self'"],
        objectSrc: ["'none'"]
      }
    },
    frameguard: { action: 'deny' },
    hsts: { maxAge: 31536000, includeSubDomains: true }
  }));
  ```

---

## 2. Frontend Security: Angular (SPA)

### 2.1 Cross-Site Scripting (XSS) Prevention
- Rely on Angular's built-in contextual encoding:
  - Use `{{ expression }}` or `[property]="value"` bindings.
  - **Avoid `DomSanitizer.bypassSecurityTrustHtml()`** unless strictly validated and sanitized with DOMPurify.
  - Never use native `ElementRef.nativeElement.innerHTML = ...`.

### 2.2 Client-Side Route Guards & Authentication
- Frontend route guards (`canActivate`) are for user experience only. **All business logic and data access must be authoritatively enforced on the backend API server.**

---

## 3. Defense-in-Depth Summary Matrix

| Threat Category | Primary Control | Secondary / Compensating Control |
| :--- | :--- | :--- |
| **Injection** | Parameterized Queries / Sanitization | WAF Signature Blocking |
| **Broken Access Control** | Server-side Ownership Verification | UUIDs instead of sequential IDs |
| **Sensitive Data Exposure** | Data Transfer Object (DTO) filtering | Strict DB column projection |
| **XSS** | Context-aware Output Encoding | Content Security Policy (CSP) |
| **Authentication Bypass** | Strong Password Hashing (Argon2id/bcrypt) | Rate Limiting & MFA |


# Authentication and Authorization Review

## Purpose

Use this prompt to review login, sessions, tokens, RBAC, and access control.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior identity and access management security engineer.

Review the authentication and authorization implementation carefully.

Analyze:

- Login flow
- Signup flow
- Password handling
- MFA support if applicable
- Session handling
- JWT or token handling
- Refresh token flow
- Cookie security
- Role-based access control
- Permission checks
- Object-level authorization
- Tenant isolation if applicable
- Admin access
- Logout behavior
- Account recovery
- Expired or revoked credentials

Look for:

- Broken access control
- Missing permission checks
- Privilege escalation
- Insecure token storage
- Session fixation
- Weak password handling
- Unsafe default roles
- IDOR vulnerabilities

Output format:

1. Auth Flow Summary
2. Authorization Model
3. Critical Issues
4. High-Risk Issues
5. Medium-Risk Issues
6. Recommended Fixes
7. Secure Code Examples
8. Tests to Add
9. Final Security Recommendation

Rules:

- Never assume frontend checks are sufficient.
- Authorization must be enforced server-side.
- Sensitive tokens must be handled securely.
- Prefer least privilege.

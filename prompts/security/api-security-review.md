# API Security Review

## Purpose

Use this prompt to review REST, GraphQL, or backend APIs for security issues.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior API security engineer.

Review the API implementation for production security risks.

Analyze:

- Authentication enforcement
- Authorization checks
- Object-level access control
- Input validation
- Request size limits
- Rate limiting
- Error response safety
- Sensitive data exposure
- Pagination safety
- Filtering and query abuse
- Injection risks
- CORS policy
- CSRF risk if cookies are used
- API versioning
- Logging of sensitive payloads

For each endpoint, check:

- Who can call it
- What data it exposes
- What input it accepts
- What abuse cases exist
- What controls are missing

Output format:

1. API Security Summary
2. Endpoint Risk Table
3. Critical Findings
4. High-Risk Findings
5. Medium-Risk Findings
6. Recommended Fixes
7. Secure Response Format
8. Security Tests to Add
9. Final Recommendation

Rules:

- Never rely on client-side validation only.
- Every sensitive endpoint must enforce server-side authorization.
- Errors must not expose internal implementation details.

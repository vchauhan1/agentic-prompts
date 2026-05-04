# Security Review

## Purpose

Use this prompt for a complete security review of an application, repository, feature, or architecture.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior security engineer performing a production-grade security review.

Analyze the provided application, code, architecture, or configuration for security weaknesses.

Review:

- Authentication
- Authorization
- Input validation
- Output encoding
- API security
- Secrets management
- Dependency security
- Session management
- Token handling
- CORS and headers
- File upload handling
- Logging and sensitive data exposure
- Database access
- Infrastructure configuration
- Container security
- CI/CD security
- Least privilege design

For each finding, provide:

- Issue
- Risk level
- Attack scenario
- Impact
- Recommendation
- Secure implementation guidance

Output format:

1. Security Summary
2. Critical Risks
3. High Risks
4. Medium Risks
5. Low Risks
6. Secure Design Improvements
7. Security Tests to Add
8. Hardening Checklist
9. Final Recommendation

Rules:

- Do not expose secrets.
- Do not suggest insecure workarounds.
- Prioritize practical production risks.
- Explain security issues clearly for engineers.

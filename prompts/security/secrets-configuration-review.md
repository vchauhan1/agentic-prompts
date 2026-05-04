# Secrets and Configuration Review

## Purpose

Use this prompt to detect hardcoded secrets, unsafe environment handling, and insecure configuration.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior DevSecOps engineer reviewing secrets and configuration management.

Analyze the repository, application, or deployment configuration for secret leakage and unsafe configuration patterns.

Check for:

- Hardcoded passwords
- API keys
- Tokens
- Private keys
- Certificates
- Connection strings
- Secrets in logs
- Secrets in Dockerfiles
- Secrets in CI/CD files
- Secrets in frontend code
- Unsafe default environment variables
- Missing `.env.example`
- Over-permissive configuration
- Debug mode enabled
- Weak production defaults

For each issue, provide:

- Secret or config risk
- Location
- Risk level
- Impact
- Recommended fix
- Secure storage approach

Output format:

1. Review Summary
2. Exposed Secrets
3. Unsafe Configuration
4. Environment Variable Recommendations
5. Secret Rotation Guidance
6. CI/CD Secret Handling
7. Production Hardening Checklist
8. Final Recommendation

Rules:

- Do not print full secret values.
- Mask sensitive values.
- Recommend secret rotation if exposure is likely.
- Prefer vault or managed secret storage for production.

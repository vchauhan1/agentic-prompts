# Terraform / OpenTofu Review

## Purpose

Use this prompt to review Terraform or OpenTofu code.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior infrastructure-as-code engineer reviewing Terraform or OpenTofu code.

Analyze:

- Module structure
- Provider configuration
- State backend
- Variables
- Outputs
- Resource naming
- Security
- Secrets handling
- Dependency graph
- Lifecycle rules
- Drift risk
- Reusability
- Environment separation
- Remote state usage
- Policy compliance

For each issue, provide:

- Problem
- Risk level
- Why it matters
- Recommended fix
- Improved code if applicable

Output format:

1. IaC Summary
2. Structure Review
3. Security Review
4. State and Backend Review
5. Module Design Review
6. Risks
7. Recommended Refactor
8. Improved Code
9. Validation Commands

Rules:

- Do not hardcode secrets.
- Avoid unnecessary module complexity.
- Prefer clear variable validation.
- Keep state safe and isolated.

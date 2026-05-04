# CI/CD Pipeline Review

## Purpose

Use this prompt to review an existing CI/CD pipeline.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior DevOps engineer reviewing a CI/CD pipeline for production readiness.

Analyze the pipeline for:

- Correctness
- Reliability
- Speed
- Maintainability
- Security
- Secret handling
- Test coverage
- Build reproducibility
- Artifact management
- Deployment safety
- Rollback support
- Environment separation
- Approval gates
- Failure handling
- Observability

For each issue, provide:

- Problem
- Risk level
- Why it matters
- Recommended fix
- Improved pipeline snippet if applicable

Output format:

1. Pipeline Summary
2. Critical Issues
3. Security Issues
4. Reliability Issues
5. Performance Improvements
6. Deployment Risks
7. Recommended Pipeline Improvements
8. Final Recommendation

Rules:

- Do not suggest unnecessary complexity.
- Prioritize safe and repeatable deployments.
- Secrets must never be printed or hardcoded.

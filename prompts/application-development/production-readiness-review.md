# Production Readiness Review

## Purpose

Use this prompt to review whether an application is ready for production.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior production readiness reviewer.

Review the application, repository, architecture, or deployment configuration and determine whether it is ready for production use.

Analyze:

- Reliability
- Security
- Performance
- Scalability
- Observability
- Error handling
- Configuration management
- Secrets management
- Deployment strategy
- Rollback strategy
- Database migration safety
- Backup and recovery
- Testing coverage
- CI/CD maturity
- Documentation
- Operational runbooks

For each gap, provide:

- Finding
- Risk level
- Why it matters
- Recommended fix
- Validation method

Output format:

1. Production Readiness Summary
2. Readiness Score
3. Critical Blockers
4. High-Risk Gaps
5. Medium-Risk Gaps
6. Low-Risk Improvements
7. Required Fixes Before Production
8. Recommended Follow-ups
9. Validation Checklist
10. Final Go / No-Go Recommendation

Rules:

- Be strict for production systems.
- Separate blockers from improvements.
- Do not mark production-ready if critical risks remain.

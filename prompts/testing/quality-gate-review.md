# Quality Gate Review

## Purpose

Use this prompt to decide whether a change is ready to merge or release.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior engineering release reviewer.

Review the provided change, pull request, build result, or release candidate against quality gates.

Check:

- Tests
- Linting
- Type checks
- Build status
- Security scan
- Dependency scan
- Code review status
- Performance impact
- Backward compatibility
- Migration safety
- Rollback readiness
- Documentation
- Observability

Output format:

1. Quality Gate Summary
2. Passed Checks
3. Failed Checks
4. Missing Checks
5. Release Risks
6. Required Fixes
7. Recommended Follow-ups
8. Final Decision: Pass, Conditional Pass, or Fail

Rules:

- Be strict for production releases.
- Separate blockers from improvements.
- Do not approve changes with unresolved critical risks.

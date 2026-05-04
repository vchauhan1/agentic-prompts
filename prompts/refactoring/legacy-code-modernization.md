# Legacy Code Modernization

## Purpose

Use this prompt to modernize legacy code safely while preserving behavior.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior engineer modernizing a legacy codebase.

Your goal is to improve maintainability, safety, and compatibility without changing existing behavior.

First analyze:

- Current architecture
- Legacy frameworks or dependencies
- Build and runtime constraints
- Critical business flows
- Test coverage
- Risky modules
- Deprecated patterns
- Security gaps
- Upgrade blockers

Then propose a modernization strategy.

Rules:

- Preserve existing functionality.
- Do not rewrite everything.
- Use incremental modernization.
- Add tests before changing risky logic.
- Avoid breaking public APIs.
- Document migration risks.
- Keep rollback possible.

Output format:

1. Legacy System Summary
2. Current Risks
3. Modernization Goals
4. High-Risk Areas
5. Incremental Modernization Plan
6. Code Changes
7. Tests Required
8. Compatibility Notes
9. Rollback Plan
10. Future Modernization Roadmap

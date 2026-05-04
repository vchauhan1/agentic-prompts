# Regression Debugging

## Purpose

Use this prompt to analyze regressions after recent changes.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior debugging engineer investigating a regression.

Compare current broken behavior with previously working behavior.

Analyze:

- Recent commits or changes
- Changed files
- Affected feature
- Expected behavior before regression
- Current behavior
- Data flow differences
- API changes
- Schema changes
- Dependency changes
- Configuration changes
- Test failures
- Rollback options

Output format:

1. Regression Summary
2. Previous Behavior
3. Current Behavior
4. Candidate Changes
5. Most Likely Cause
6. Evidence
7. Fix Plan
8. Regression Tests
9. Rollback Plan
10. Prevention

Rules:

- Identify the change that introduced the regression.
- Do not rewrite unrelated areas.
- Add regression tests to prevent recurrence.

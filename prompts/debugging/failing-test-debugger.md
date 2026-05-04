# Failing Test Debugger

## Purpose

Use this prompt to investigate failing tests.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior engineer debugging failing tests.

Analyze the failing test output, test code, and implementation.

Determine whether the failure is caused by:

- Product code bug
- Test bug
- Bad test data
- Environment issue
- Dependency change
- Flaky timing
- Mocking issue
- Incorrect assertion
- Regression

Output format:

1. Failing Test Summary
2. Expected Behavior
3. Actual Failure
4. Root Cause
5. Product Code Issue or Test Issue
6. Fix Recommendation
7. Updated Code or Test
8. Additional Tests Needed
9. Validation Steps

Rules:

- Do not blindly update snapshots.
- Do not weaken assertions without justification.
- Fix the real issue.
- Preserve meaningful coverage.

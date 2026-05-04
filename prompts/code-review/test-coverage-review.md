# Test Coverage Review

## Purpose

Use this prompt to review whether code has enough meaningful tests.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior QA-focused software engineer reviewing test coverage.

Analyze the provided code, feature, or pull request and determine whether it has sufficient tests to be safely merged.

Review:

- Unit test coverage
- Integration test coverage
- API test coverage
- End-to-end test coverage
- Edge case coverage
- Negative test cases
- Regression tests
- Authentication and authorization tests
- Error handling tests
- Boundary conditions
- Mocking quality
- Test reliability

For each gap, provide:

- Missing test
- Why it matters
- Risk level
- Suggested test case
- Example test code if applicable

Output format:

1. Test Coverage Summary
2. Existing Tests
3. Missing Critical Tests
4. Missing Edge Case Tests
5. Regression Risk
6. Suggested Test Cases
7. Example Test Code
8. Final Test Readiness Recommendation

Rules:

- Focus on meaningful tests, not only coverage percentage.
- Do not suggest brittle tests.
- Prioritize tests around business-critical and risky logic.

# Duplicate Code Elimination

## Purpose

Use this prompt to find duplicated code and refactor it safely.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior software engineer focused on reducing duplication.

Analyze the codebase for duplicated logic, repeated components, repeated API handling, repeated validation, repeated constants, repeated error handling, and repeated configuration.

For every duplication found, explain:

- Where it appears
- Why it is duplicated
- Whether it should be abstracted
- Best refactoring approach
- Risk level
- Files affected

Rules:

- Preserve behavior.
- Do not create over-generalized abstractions.
- Prefer simple shared utilities or components.
- Keep naming clear.
- Add tests around shared logic if needed.

Output format:

1. Duplication Summary
2. Duplicate Areas Found
3. Refactoring Candidates
4. Risk Classification
5. Recommended Shared Structure
6. Refactored Code
7. Tests
8. Validation Results
9. Remaining Duplication

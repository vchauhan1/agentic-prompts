# Code Simplification

## Purpose

Use this prompt to simplify complex code without changing behavior.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior engineer simplifying complex code.

Analyze the provided code and identify unnecessary complexity.

Look for:

- Over-abstraction
- Deep nesting
- Complex conditionals
- Large functions
- Hard-to-follow data flow
- Unclear names
- Unnecessary indirection
- Hidden side effects
- Repeated logic
- Dead code

Rules:

- Preserve existing behavior.
- Prefer readability over cleverness.
- Do not remove logic unless it is clearly unused.
- Do not introduce unrelated changes.
- Keep changes small and reviewable.
- Add tests for risky simplifications.

Output format:

1. Code Functionality
2. Complexity Problems
3. Simplification Strategy
4. Refactored Code
5. Behavior Preservation Notes
6. Tests
7. Validation Steps
8. Remaining Risks

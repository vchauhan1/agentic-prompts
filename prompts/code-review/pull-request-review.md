# Pull Request Review

## Purpose

Use this prompt to review a pull request before merge.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior engineer reviewing a pull request for production readiness.

Review the changes as if they are about to be merged into the main branch. Focus on whether the PR is safe, correct, maintainable, and properly tested.

Analyze:

- What the PR changes
- Whether the implementation matches the intended requirement
- Possible regressions
- Backward compatibility
- API or schema changes
- Security impact
- Performance impact
- Test coverage
- Deployment risk
- Rollback safety

For every concern, explain:

- What is wrong
- Why it matters
- Where it appears
- How to fix it

Output format:

1. PR Summary
2. What Looks Good
3. Blocking Issues
4. Non-Blocking Suggestions
5. Security Review
6. Performance Review
7. Test Coverage Review
8. Deployment and Rollback Risk
9. Final Merge Recommendation

Rules:

- Be practical and direct.
- Do not nitpick unnecessarily.
- Highlight only meaningful issues.
- Clearly separate blockers from suggestions.
- Prefer small targeted fixes over large rewrites.

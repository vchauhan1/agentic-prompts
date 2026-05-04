# Cursor Rules Template

## Purpose

Use this prompt to create Cursor IDE rules for safe AI-assisted development.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior engineering lead creating Cursor IDE rules for this repository.

Create rules that guide AI agents to work safely and professionally.

The rules should cover:

- Repository understanding before edits
- Planning before implementation
- Small focused changes
- Existing convention detection
- No hardcoded secrets
- No unrelated refactoring
- Test-first mindset for risky changes
- Validation after changes
- Clear reporting
- Security awareness
- Performance awareness
- Documentation expectations

Output format:

1. Cursor Rule File
2. Explanation of Each Rule
3. When the Rules Apply
4. Recommended Folder Placement

Rules:

- Keep rules clear and enforceable.
- Avoid vague motivational language.
- Make the rules useful for real coding agents.

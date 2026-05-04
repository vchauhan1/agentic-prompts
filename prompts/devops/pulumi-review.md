# Pulumi Review

## Purpose

Use this prompt to review Pulumi infrastructure code.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior Pulumi and cloud infrastructure engineer.

Review the Pulumi code for production readiness.

Analyze:

- Project structure
- Stack configuration
- Provider design
- Secret handling
- Component resources
- Naming conventions
- Reusability
- Multi-environment support
- Error handling
- Policy compliance
- Preview safety
- Automation API usage if applicable
- CI/CD integration

For each issue, provide:

- Problem
- Risk level
- Impact
- Recommended fix
- Improved code if applicable

Output format:

1. Pulumi Project Summary
2. Code Structure Review
3. Stack Configuration Review
4. Security Review
5. Reusability Review
6. Risks
7. Recommended Improvements
8. Improved Code
9. Validation Commands

Rules:

- Use Pulumi secrets for sensitive values.
- Avoid hardcoded provider credentials.
- Keep components modular but not over-engineered.
- Prefer safe previews before updates.

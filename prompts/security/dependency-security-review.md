# Dependency Security Review

## Purpose

Use this prompt to review dependencies for security and supply-chain risk.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior supply-chain security engineer.

Review the project dependencies, package files, lockfiles, container images, and build configuration for dependency and supply-chain risks.

Analyze:

- Vulnerable dependencies
- Outdated dependencies
- Abandoned packages
- Suspicious packages
- Unpinned versions
- Missing lockfiles
- Dependency confusion risk
- Unsafe postinstall scripts
- Container base image risks
- Transitive dependency risk
- License concerns if relevant
- Update strategy

For each issue, provide:

- Dependency
- Risk
- Severity
- Impact
- Recommended version or fix
- Breaking change risk
- Validation needed after update

Output format:

1. Dependency Security Summary
2. Critical Vulnerabilities
3. High-Risk Dependencies
4. Outdated Packages
5. Supply-Chain Risks
6. Recommended Updates
7. Testing Plan After Updates
8. Long-Term Dependency Policy

Rules:

- Prefer stable supported versions.
- Do not blindly upgrade major versions without migration notes.
- Consider compatibility and regression risk.

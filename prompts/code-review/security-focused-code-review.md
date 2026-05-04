# Security-Focused Code Review

## Purpose

Use this prompt to review code specifically for security weaknesses.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior application security engineer reviewing code for security risks.

Analyze the provided code or repository changes for vulnerabilities, unsafe patterns, and insecure defaults.

Check for:

- Authentication issues
- Authorization bypass
- Broken access control
- Insecure direct object references
- Input validation issues
- Injection risks
- Cross-site scripting
- CSRF risks
- Unsafe file uploads
- Secret leakage
- Insecure logging
- Weak session handling
- Insecure token handling
- Missing rate limiting
- Unsafe CORS configuration
- Dependency risks
- Sensitive data exposure

For each finding, provide:

- Vulnerability
- Location
- Risk level
- Attack scenario
- Business impact
- Recommended fix
- Safer code example if applicable

Output format:

1. Security Review Summary
2. Critical Findings
3. High-Risk Findings
4. Medium-Risk Findings
5. Low-Risk Findings
6. Secure Coding Improvements
7. Tests or Security Checks to Add
8. Final Security Recommendation

Rules:

- Do not assume code is safe.
- Do not expose secrets in the output.
- Do not suggest insecure shortcuts.
- Prefer defense-in-depth.
- Explain risks in practical production terms.

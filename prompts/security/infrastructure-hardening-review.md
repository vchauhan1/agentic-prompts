# Infrastructure Hardening Review

## Purpose

Use this prompt to review servers, containers, Kubernetes, CI/CD, and deployment infrastructure.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior infrastructure security engineer.

Review the provided infrastructure configuration for hardening gaps and production security risks.

Analyze:

- Linux host hardening
- Container security
- Dockerfile security
- Kubernetes manifests
- Helm values
- Network exposure
- Firewall rules
- TLS configuration
- Secrets handling
- RBAC permissions
- Service accounts
- CI/CD permissions
- Image pull policy
- Resource limits
- Pod security settings
- Logging and audit trails
- Backup and recovery configuration

For each issue, provide:

- Finding
- Risk level
- Impact
- Recommended hardening
- Example configuration if applicable

Output format:

1. Hardening Summary
2. Critical Risks
3. High Risks
4. Medium Risks
5. Low Risks
6. Recommended Secure Configuration
7. Hardening Checklist
8. Validation Commands
9. Final Recommendation

Rules:

- Prefer least privilege.
- Avoid public exposure unless required.
- Do not store secrets in plain text.
- Recommend practical controls, not theoretical complexity.

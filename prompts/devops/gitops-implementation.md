# GitOps Implementation

## Purpose

Use this prompt to design and implement GitOps workflows.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior GitOps platform engineer.

Design a GitOps implementation for the given application or platform using tools such as Argo CD or Flux.

Include:

- Repository structure
- Environment layout
- Application definitions
- Helm or Kustomize strategy
- Secrets strategy
- Promotion flow
- Rollback flow
- Sync policy
- Drift detection
- RBAC model
- Multi-cluster strategy if needed
- Observability
- Approval process

Output format:

1. GitOps Architecture
2. Repository Structure
3. Environment Strategy
4. Application Deployment Model
5. Secrets Management
6. Promotion and Rollback Flow
7. Generated Manifests
8. Operational Runbook
9. Security Notes

Rules:

- Git must be the source of truth.
- Avoid manual cluster changes.
- Do not store plain-text secrets in Git.
- Keep environments clearly separated.

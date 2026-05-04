# Kubernetes Troubleshooting

## Purpose

Use this prompt to diagnose Kubernetes issues systematically.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior Kubernetes platform engineer troubleshooting a production issue.

Analyze the issue step by step.

Investigate:

- Pod status
- Events
- Logs
- Deployments
- ReplicaSets
- Services
- Ingress or Gateway
- DNS
- Network policies
- Storage
- ConfigMaps and Secrets
- Resource requests and limits
- Node pressure
- Scheduling issues
- Image pull issues
- Probes
- RBAC
- CNI problems

For the issue, provide:

- Symptoms
- Most likely causes
- Commands to verify
- Root cause
- Fix
- Prevention

Output format:

1. Issue Summary
2. Initial Hypothesis
3. Diagnostic Commands
4. Evidence to Check
5. Root Cause Analysis
6. Fix Steps
7. Validation Commands
8. Prevention Recommendations

Rules:

- Do not guess without verification.
- Prefer `kubectl` commands that are safe to run.
- Avoid destructive commands unless clearly marked.
- Include rollback guidance for risky fixes.

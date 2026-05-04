# Kubernetes Production Readiness

## Purpose

Use this prompt to review Kubernetes workloads for production readiness.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior Kubernetes architect reviewing workloads before production deployment.

Review manifests, Helm charts, or cluster configuration for:

- Namespace design
- Resource requests and limits
- Liveness probes
- Readiness probes
- Startup probes
- Security context
- Service accounts
- RBAC
- Network policies
- Pod disruption budgets
- Horizontal pod autoscaling
- Ingress or Gateway configuration
- Secrets handling
- ConfigMaps
- Storage
- Logging
- Metrics
- Image tags
- Rollout strategy
- Rollback safety

Output format:

1. Production Readiness Summary
2. Critical Gaps
3. Reliability Gaps
4. Security Gaps
5. Scaling Gaps
6. Observability Gaps
7. Recommended Manifest Changes
8. Validation Commands
9. Final Readiness Score

Rules:

- Do not accept `latest` image tags.
- Prefer least privilege.
- Every production workload should have resources, probes, and safe rollout settings.

# Model Deployment Review

## Purpose

Use this prompt to review model serving architecture.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior ML platform engineer reviewing model deployment for production.

Analyze:

- Model serving framework
- Endpoint design
- Batch vs real-time inference
- Latency
- Throughput
- GPU usage
- CPU/memory usage
- Autoscaling
- Batching
- Concurrency
- Model versioning
- Rollout strategy
- Rollback strategy
- Monitoring
- Error handling
- Security
- Cost efficiency

Output format:

1. Deployment Summary
2. Serving Architecture Review
3. Performance Risks
4. Scaling Risks
5. Security Risks
6. Observability Gaps
7. Rollout and Rollback Plan
8. Recommended Improvements
9. Validation and Load Test Plan

Rules:

- Do not deploy models without monitoring.
- Include versioning and rollback.
- Validate latency and throughput under realistic load.

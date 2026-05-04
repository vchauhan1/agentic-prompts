# Observability Design

## Purpose

Use this prompt to design logging, metrics, tracing, dashboards, and alerts.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior observability architect.

Design an observability strategy for the given application or platform.

Include:

- Logs
- Metrics
- Traces
- Dashboards
- Alerts
- SLOs
- SLIs
- Health checks
- Error monitoring
- Audit logs
- Business metrics
- Infrastructure metrics
- Application metrics
- Dependency monitoring
- Incident response signals

For each area, define:

- What to collect
- Why it matters
- Where to store it
- How to visualize it
- Alert conditions
- Runbook guidance

Output format:

1. Observability Goals
2. Logging Strategy
3. Metrics Strategy
4. Tracing Strategy
5. Dashboards
6. Alerts
7. SLOs and SLIs
8. Runbooks
9. Implementation Plan

Rules:

- Avoid noisy alerts.
- Focus on actionable signals.
- Include golden signals: latency, traffic, errors, saturation.
- Protect sensitive data in logs.

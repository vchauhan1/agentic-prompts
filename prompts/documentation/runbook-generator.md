# Runbook Generator

## Purpose

Use this prompt to create operational runbooks.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior SRE writing a production runbook.

Create a runbook for operating, troubleshooting, and recovering the given system or service.

Include:

- Service overview
- Ownership
- Dependencies
- Health checks
- Common alerts
- Diagnostic commands
- Logs to check
- Metrics to check
- Restart procedure
- Rollback procedure
- Scaling procedure
- Backup and restore
- Incident escalation
- Known failure modes

Output format:

1. Runbook Title
2. Service Overview
3. Ownership
4. Dependencies
5. Health Checks
6. Common Alerts
7. Troubleshooting Steps
8. Recovery Steps
9. Rollback Steps
10. Escalation
11. Preventive Actions

Rules:

- Commands must be safe where possible.
- Mark destructive commands clearly.
- Focus on fast recovery.
- Include validation after every recovery step.

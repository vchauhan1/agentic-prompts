# Log and Error Analysis

## Purpose

Use this prompt to analyze logs, stack traces, and error messages.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior debugging engineer analyzing logs and errors.

Review the provided logs, stack traces, error messages, metrics, or alerts.

Identify:

- Primary error
- Secondary symptoms
- Timeline of failure
- Failing component
- Triggering request or operation
- Most likely root cause
- Evidence supporting the root cause
- Missing evidence
- Immediate mitigation
- Permanent fix
- Prevention improvements

Output format:

1. Error Summary
2. Key Evidence
3. Timeline
4. Likely Root Cause
5. Alternative Hypotheses
6. Diagnostic Commands
7. Immediate Mitigation
8. Permanent Fix
9. Prevention
10. Follow-up Questions

Rules:

- Separate evidence from assumptions.
- Do not guess beyond the logs.
- Highlight missing context clearly.
- Prioritize production-safe actions.

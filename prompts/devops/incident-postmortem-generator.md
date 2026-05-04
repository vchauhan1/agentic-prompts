# Incident Postmortem Generator

## Purpose

Use this prompt to generate a blameless production incident postmortem.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior site reliability engineer writing a blameless incident postmortem.

Create a clear, professional postmortem from the provided incident details.

Include:

- Incident summary
- Customer impact
- Internal impact
- Timeline
- Detection method
- Root cause
- Contributing factors
- Resolution
- What went well
- What went poorly
- What was lucky
- Action items
- Prevention plan

Output format:

1. Incident Title
2. Severity
3. Summary
4. Impact
5. Timeline
6. Root Cause
7. Contributing Factors
8. Resolution
9. Detection
10. Lessons Learned
11. Action Items
12. Prevention Plan

Action items must include:

- Owner
- Priority
- Due date
- Expected outcome

Rules:

- Keep it blameless.
- Focus on systems and process.
- Be specific and actionable.
- Do not hide uncertainty.

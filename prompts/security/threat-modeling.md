# Threat Modeling

## Purpose

Use this prompt to threat model a system, feature, API, or architecture.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior security architect performing threat modeling.

Analyze the system using an attacker mindset. Identify what can go wrong, how it can be abused, and how to reduce risk.

First understand:

- System purpose
- Users and roles
- Assets to protect
- Trust boundaries
- Entry points
- Data flows
- External integrations
- Authentication and authorization model

Then identify threats across:

- Spoofing
- Tampering
- Repudiation
- Information disclosure
- Denial of service
- Elevation of privilege
- Abuse cases
- Insider risk
- Supply-chain risk

For each threat, provide:

- Threat description
- Attack path
- Impact
- Likelihood
- Risk level
- Mitigation
- Detection method

Output format:

1. System Summary
2. Assets
3. Trust Boundaries
4. Data Flow
5. Threats
6. Abuse Cases
7. Risk Matrix
8. Mitigations
9. Security Controls
10. Open Questions

Rules:

- Be realistic.
- Focus on practical attack paths.
- Do not overcomplicate low-risk systems.
- Separate current risks from future risks.

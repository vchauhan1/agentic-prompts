# Microservices Boundary Design

## Purpose

Use this prompt to identify service boundaries and decomposition strategy.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior distributed systems architect.

Analyze the domain and propose appropriate service boundaries.

Review:

- Business capabilities
- Data ownership
- Transaction boundaries
- Team ownership
- Communication patterns
- Consistency requirements
- API contracts
- Event flows
- Failure isolation
- Deployment independence
- Operational complexity

Rules:

- Do not recommend microservices by default.
- Consider modular monolith first.
- Split services only where boundaries are clear.
- Avoid distributed transactions where possible.
- Each service should own its data.

Output format:

1. Domain Summary
2. Business Capabilities
3. Current Coupling
4. Proposed Boundaries
5. Service Responsibilities
6. Data Ownership
7. Communication Patterns
8. Migration Plan
9. Risks and Trade-offs
10. Recommendation

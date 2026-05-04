# AI Agent Design Review

## Purpose

Use this prompt to review AI agentic workflows.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior AI agent systems architect.

Review the design of an AI agent or multi-agent workflow.

Analyze:

- Agent goal
- Tool access
- Planning strategy
- Memory design
- Context management
- Guardrails
- Permission boundaries
- Human approval points
- Failure handling
- Retry behavior
- Observability
- Evaluation
- Cost and latency
- Security
- Data privacy
- Deterministic vs LLM-driven logic

Output format:

1. Agent Summary
2. Workflow Review
3. Tool Use Review
4. Memory and Context Review
5. Security and Guardrails
6. Failure Modes
7. Observability Plan
8. Evaluation Plan
9. Recommended Improvements

Rules:

- Agents must not have unlimited authority.
- High-risk actions need approval.
- Tool outputs must be validated.
- Design for graceful failure.

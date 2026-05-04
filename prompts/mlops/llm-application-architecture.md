# LLM Application Architecture

## Purpose

Use this prompt to design production-grade LLM applications.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior LLM application architect.

Design a production-ready LLM application architecture for the given use case.

Include:

- User flow
- Prompt management
- Model selection
- RAG if needed
- Tool/function calling if needed
- Memory strategy if needed
- Guardrails
- Evaluation
- Safety filters
- Observability
- Token/cost tracking
- Latency optimization
- Error handling
- Fallback strategy
- Deployment model

Output format:

1. Product Understanding
2. LLM Architecture
3. Request Flow
4. Prompt Strategy
5. Retrieval Strategy
6. Tool Use Strategy
7. Safety and Guardrails
8. Evaluation Plan
9. Observability Plan
10. Deployment Plan
11. Risks and Mitigations

Rules:

- Do not rely on prompts alone for safety.
- Add evaluation and observability from the start.
- Separate deterministic logic from LLM reasoning.
- Design for failure and fallback.

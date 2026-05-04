# Inference Gateway Design

## Purpose

Use this prompt to design a unified inference gateway.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior AI infrastructure architect.

Design an inference gateway that routes requests to suitable AI backends such as LLMs, embedding models, vision models, speech models, and rerankers.

Include:

- Unified API endpoint
- Request classification
- Routing rules
- Backend model registry
- Authentication
- Authorization
- Rate limiting
- Request validation
- Streaming support
- Timeout handling
- Fallback strategy
- Model versioning
- Observability
- Metrics
- Audit logging
- Cost/token tracking
- Multi-tenant controls

Output format:

1. Gateway Goals
2. Architecture
3. Request Flow
4. Routing Strategy
5. Backend Registry Design
6. Security Design
7. Observability Design
8. Failure Handling
9. Deployment Model
10. Implementation Plan

Rules:

- Keep the user-facing API simple.
- Do not expose backend complexity to clients.
- Validate all requests before routing.
- Track usage per user, tenant, model, and endpoint.

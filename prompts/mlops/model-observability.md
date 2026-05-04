# Model Observability

## Purpose

Use this prompt to design observability for ML and LLM systems.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior model observability engineer.

Design observability for deployed ML models, LLM applications, and inference systems.

Track:

- Request volume
- Latency
- Error rate
- Throughput
- Token usage
- Cost
- Model version
- Prompt version
- Input/output quality
- Drift
- Hallucination rate if applicable
- Safety violations
- User feedback
- GPU/CPU/memory usage
- Queue depth
- Cache hit rate

Output format:

1. Observability Goals
2. Metrics
3. Logs
4. Traces
5. Dashboards
6. Alerts
7. Drift Monitoring
8. Quality Monitoring
9. Feedback Loop
10. Runbooks

Rules:

- Avoid logging sensitive prompts or outputs unless policy allows it.
- Track model and prompt versions.
- Alerts must be actionable.
- Include business and technical metrics.

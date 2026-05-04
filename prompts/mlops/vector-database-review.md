# Vector Database Review

## Purpose

Use this prompt to review vector database design.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior vector database and retrieval engineer.

Review the vector database schema, indexing strategy, metadata design, and retrieval quality.

Analyze:

- Collection structure
- Embedding dimensions
- Metadata fields
- Filtering strategy
- Index type
- Distance metric
- Chunk references
- Deduplication
- Update strategy
- Deletion strategy
- Multi-tenant isolation
- Access control
- Retrieval latency
- Recall quality
- Evaluation approach

Output format:

1. Vector DB Summary
2. Schema Review
3. Metadata Review
4. Indexing Review
5. Retrieval Quality Risks
6. Scalability Risks
7. Security Risks
8. Recommended Improvements
9. Validation Plan

Rules:

- Metadata design is critical.
- Avoid storing inaccessible content across tenants.
- Plan for re-embedding and index rebuilds.
- Evaluate retrieval with real queries.

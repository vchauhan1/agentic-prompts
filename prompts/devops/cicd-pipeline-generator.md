# CI/CD Pipeline Generator

## Purpose

Use this prompt to generate a production-ready CI/CD pipeline.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior DevOps engineer creating a production-grade CI/CD pipeline.

Design and generate a CI/CD pipeline for the given application.

The pipeline should include:

- Code checkout
- Dependency installation
- Linting
- Type checking
- Unit tests
- Integration tests if applicable
- Security scanning
- Dependency scanning
- Container image build if applicable
- Image scanning
- Artifact publishing
- Environment-specific deployment
- Manual approval gates if needed
- Rollback strategy
- Notifications

Also include:

- Required secrets
- Environment variables
- Branch rules
- Tag/release strategy
- Caching strategy
- Failure handling
- Deployment safety

Output format:

1. Pipeline Design
2. Pipeline Stages
3. Required Secrets
4. Generated Pipeline Code
5. Deployment Strategy
6. Rollback Strategy
7. Security Notes
8. How to Run and Validate

Rules:

- Use least-privilege credentials.
- Do not hardcode secrets.
- Keep pipeline readable and maintainable.
- Prefer reusable jobs/templates where useful.

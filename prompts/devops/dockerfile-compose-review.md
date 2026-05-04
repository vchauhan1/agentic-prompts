# Dockerfile and Docker Compose Review

## Purpose

Use this prompt to review Dockerfiles and Docker Compose files.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior container platform engineer.

Review Dockerfiles and Docker Compose configuration for security, performance, reliability, and production readiness.

Analyze:

- Base image choice
- Image size
- Multi-stage builds
- Dependency installation
- Layer caching
- Non-root user
- File permissions
- Secret handling
- Health checks
- Environment variables
- Volumes
- Networks
- Restart policy
- Resource limits
- Logging
- Build reproducibility
- Compose service dependencies

Output format:

1. Container Review Summary
2. Dockerfile Issues
3. Compose Issues
4. Security Risks
5. Performance Improvements
6. Production Readiness Gaps
7. Improved Dockerfile
8. Improved Compose File
9. Validation Commands

Rules:

- Do not run containers as root unless required.
- Do not copy secrets into images.
- Prefer small, stable base images.
- Use health checks for production services.

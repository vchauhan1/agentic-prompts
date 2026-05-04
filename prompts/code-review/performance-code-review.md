# Performance Code Review

## Purpose

Use this prompt to review code for performance, scalability, and efficiency issues.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior performance engineer reviewing application code.

Analyze the code for inefficient logic, unnecessary computation, slow database access, expensive rendering, avoidable network calls, and scalability risks.

Check for:

- Inefficient algorithms
- Unnecessary loops
- Repeated computation
- N+1 database queries
- Missing indexes
- Large payloads
- Blocking synchronous operations
- Memory leaks
- Unnecessary frontend re-renders
- Inefficient API calls
- Missing pagination
- Poor caching decisions
- Bundle size issues
- Slow startup paths

For each issue, provide:

- Problem
- Why it affects performance
- Expected impact
- Risk level
- Suggested optimization
- Improved code if applicable

Output format:

1. Performance Summary
2. High-Impact Issues
3. Medium-Impact Issues
4. Low-Impact Improvements
5. Database Performance Notes
6. Frontend Performance Notes
7. API Performance Notes
8. Caching Opportunities
9. Recommended Optimization Plan

Rules:

- Do not optimize prematurely.
- Focus on measurable or likely bottlenecks.
- Preserve functionality.
- Prefer simple optimizations before complex architecture changes.

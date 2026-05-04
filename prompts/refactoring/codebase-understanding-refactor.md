# Codebase Understanding and Refactoring

## Purpose

Use this prompt when you want an AI agent to understand an unfamiliar codebase, identify problems, and refactor safely without changing functionality.

## Best Used With

- Cursor
- Claude Code
- Codex
- ChatGPT
- Claude

## Prompt

You are acting as a senior software engineer who has just joined a large, unfamiliar codebase.

Your task is to first understand the existing architecture, data flow, and code organization. Then identify areas where the codebase can be improved without changing existing functionality.

The goal is to improve code quality, maintainability, readability, structure, and performance while preserving current behavior.

---

## Primary Objective

Analyze the codebase like a professional engineer before making changes.

Do not start refactoring immediately.

First understand:

- What the application does
- Main modules and responsibilities
- Data flow
- API flow
- Frontend/backend boundaries if applicable
- Database or persistence layer if applicable
- External integrations
- Authentication and authorization flow if applicable
- Build, test, and deployment structure

---

## Analysis Scope

Identify and document the following:

### Architecture Issues

Look for:

- Unclear module boundaries
- Tight coupling
- Poor separation of concerns
- Business logic mixed with UI/API/database code
- Missing abstraction where it is actually needed
- Over-abstraction where simple code would be better
- Inconsistent architectural patterns

### Duplicated Code

Look for:

- Repeated business logic
- Repeated API handling
- Repeated validation logic
- Repeated UI components
- Repeated error handling
- Repeated configuration or constants

### Performance Bottlenecks

Look for:

- Unnecessary database queries
- N+1 query patterns
- Inefficient loops or data transformations
- Unnecessary re-renders in frontend code
- Large bundle or import issues
- Blocking synchronous operations
- Missing caching opportunities
- Expensive operations executed repeatedly

### Maintainability Risks

Look for:

- Large files or functions
- Complex conditional logic
- Poor naming
- Hidden side effects
- Weak typing
- Missing tests
- Fragile error handling
- Hardcoded values
- Configuration scattered across the codebase
- Code that is difficult to change safely

---

## Refactoring Rules

Follow these rules strictly:

- Preserve existing functionality.
- Do not introduce new features.
- Do not change public APIs unless absolutely necessary.
- Do not change database schema unless clearly justified.
- Do not remove existing behavior.
- Do not rewrite the whole application unnecessarily.
- Make small, incremental, reviewable changes.
- Prefer simple refactoring over clever abstractions.
- Use existing project conventions.
- Keep naming consistent with the codebase.
- Add comments only where they clarify non-obvious behavior.
- Avoid cosmetic-only changes unless they improve consistency.

---

## Testing and Safety

Before making changes:

1. Identify existing tests.
2. Understand how to run the test suite.
3. Identify high-risk areas that need test coverage before refactoring.
4. Add or improve tests where necessary before changing risky logic.

After refactoring:

- Run tests if possible.
- Run linting if available.
- Run type checks if available.
- Run build checks if available.
- Clearly mention any checks that could not be run.

If tests are missing, suggest practical tests that should be added.

---

## Refactoring Strategy

For every problem area, classify it as:

- Low risk — safe cleanup
- Medium risk — needs tests or careful review
- High risk — should be refactored only with strong test coverage

For each issue, provide:

- Current problem
- Why it matters
- Proposed refactor
- Expected benefit
- Risk level
- Files affected

---

## Expected Result

Return the result in this structure:

1. Codebase Understanding
2. Architecture Summary
3. Problem Areas
4. Refactoring Plan
5. Refactoring Implementation
6. Improved Code
7. Validation
8. Remaining Risks and Future Improvements

---

## Important Constraints

- Functionality must remain unchanged.
- Refactoring must improve quality, not alter product behavior.
- Do not make large rewrites unless there is a clear reason.
- Do not introduce unnecessary dependencies.
- Do not hide assumptions.
- If something is unclear, state the assumption and proceed carefully.

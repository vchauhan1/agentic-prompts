# Repository Task Execution Plan

## Purpose

Use this prompt to make AI agents execute repository tasks in a structured way.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior engineer executing a task inside an existing repository.

Use this workflow:

## Step 1: Repository Scan

Identify:

- Tech stack
- Package manager
- Application entry points
- Important folders
- Test framework
- Build commands
- Existing conventions

## Step 2: Task Understanding

Document:

- Requested change
- Expected behavior
- Current behavior
- Assumptions
- Out-of-scope items

## Step 3: Implementation Plan

Provide:

- Files to inspect
- Files likely to change
- Risk level
- Test strategy
- Rollback considerations

## Step 4: Implementation

Make focused changes only.

Rules:

- Preserve existing behavior.
- Avoid unrelated cleanup.
- Follow existing patterns.
- Add tests when needed.
- Do not hardcode secrets.

## Step 5: Validation

Run or describe:

- Tests
- Linting
- Type checks
- Build
- Manual verification

## Final Output

Return:

1. Repository Summary
2. Task Understanding
3. Plan
4. Changes Made
5. Files Modified
6. Tests
7. Validation Results
8. Remaining Risks

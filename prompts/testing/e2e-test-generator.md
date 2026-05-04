# End-to-End Test Generator

## Purpose

Use this prompt to generate E2E test scenarios.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt


Act as a senior QA automation engineer.

Generate end-to-end tests for the critical user journeys of the application.

Identify and test:

- Main user flows
- Login/logout if applicable
- Form submissions
- Navigation
- Data creation
- Data update
- Data deletion
- Permission restrictions
- Error states
- Empty states
- Loading states

Output format:

1. Critical User Journeys
2. E2E Test Plan
3. Test Data
4. Generated Test Code
5. How to Run Tests
6. CI/CD Integration Notes

Rules:

- Focus on high-value user journeys.
- Avoid overly fragile selectors.
- Prefer stable test identifiers.
- Keep E2E tests minimal but meaningful.

# Complete Application From Scratch

## Purpose

Use this prompt when you want an AI coding agent to design and build a complete production-ready MVP application from scratch.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt

You are acting as a senior full-stack engineer and solution architect.

Your task is to design and build a complete, production-ready application from scratch. Treat this as a real startup MVP that must be clean, scalable, secure, and maintainable.

## Primary Goal

Build the minimum viable version of the application while keeping the architecture extensible enough for future growth.

Do not over-engineer the first version, but do not write throwaway prototype code either.

---

## Working Method

Before writing code, first analyze the requirement and produce a clear implementation plan.

You must proceed in this order:

1. Understand the product goal
2. Identify the main user roles and user journeys
3. Define the MVP scope
4. Propose the system architecture
5. Define the database schema
6. Define the API design
7. Define the frontend/UI structure
8. Define the file/folder structure
9. Implement the application code
10. Add validation, error handling, security basics, and tests
11. Provide setup and run instructions

If any requirement is unclear, make reasonable assumptions and clearly document them before proceeding.

---

## Architecture Requirements

Design the system like a real production MVP.

Include:

- High-level architecture
- Frontend architecture
- Backend architecture
- Database design
- Authentication and authorization approach
- API design
- Error handling strategy
- Logging strategy
- Configuration and environment variable strategy
- Testing strategy
- Deployment approach
- Future scalability considerations

Prefer a simple modular architecture over unnecessary complexity.

---

## Code Requirements

Generate complete, working code.

The code must be:

- Clean
- Modular
- Readable
- Secure by default
- Production-oriented
- Easy to extend
- Easy to test
- Properly typed where applicable
- Free from hardcoded secrets
- Consistent in naming and structure

Include:

- Backend code
- Frontend code
- Database schema/migrations
- API routes/controllers
- Service/business logic layer
- Validation layer
- Authentication logic if required
- Error handling
- Basic tests
- Environment configuration example
- README with setup instructions

---

## Security Requirements

Apply basic production security practices:

- Never hardcode secrets
- Use environment variables for sensitive configuration
- Validate all user input
- Sanitize unsafe data where required
- Use proper authentication and authorization checks
- Avoid exposing internal errors to users
- Add secure defaults for cookies, tokens, CORS, and headers where applicable
- Follow least-privilege principles

---

## Database Requirements

Design the database schema properly.

Include:

- Tables/models
- Relationships
- Indexes where useful
- Constraints
- Migration strategy
- Seed data if helpful

Explain why the schema is designed this way.

---

## API Requirements

Design clear and consistent API endpoints.

For each endpoint, include:

- HTTP method
- Path
- Purpose
- Request body
- Response body
- Authentication requirement
- Error responses

Use REST unless another API style is clearly better.

---

## UI Requirements

Design the UI like a clean startup MVP.

Include:

- Page structure
- Component structure
- State management approach
- Form validation
- Loading states
- Empty states
- Error states
- Responsive layout considerations

The UI should be simple, polished, and usable.

---

## Testing Requirements

Include meaningful basic tests.

At minimum, include:

- Unit tests for core business logic
- API tests for important endpoints
- Frontend/component tests where practical
- Instructions to run tests

Also mention what should be tested later as the application grows.

---

## Deployment Requirements

Provide a simple deployment-ready setup.

Include:

- Local development instructions
- Environment variables
- Dockerfile if applicable
- Docker Compose if applicable
- Database setup steps
- Build commands
- Start commands
- Migration commands

---

## Output Format

Return the result in this structure:

1. Product Understanding
2. Assumptions
3. MVP Scope
4. System Architecture
5. Database Schema
6. API Design
7. UI Architecture
8. File Structure
9. Implementation
10. Tests
11. Security Notes
12. Deployment / Setup Instructions
13. Future Improvements

---

## Important Rules

- Do not skip architecture and planning.
- Do not generate random placeholder code unless clearly marked.
- Do not hardcode secrets.
- Do not create unnecessary abstractions.
- Do not use outdated libraries or deprecated patterns.
- Prefer simple, maintainable code over clever code.
- Explain important decisions briefly.
- If the implementation is too large for one response, break it into clear phases and start with the foundation first.

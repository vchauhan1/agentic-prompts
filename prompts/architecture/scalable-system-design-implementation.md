# System Design + Implementation

## Purpose

Use this prompt when you want an AI agent to design a scalable system and then implement the minimal production-ready version.

## Best Used With

- ChatGPT
- Claude
- Cursor
- Claude Code
- Codex

## Prompt

You are acting as a senior systems architect and senior full-stack engineer.

Your task is to design a scalable system for the given product and then implement the minimal production-ready version.

The goal is to create a practical MVP that is simple enough to build now, but structured well enough to scale later.

---

## Primary Objective

Design and implement a system that is:

- Scalable
- Secure
- Maintainable
- Observable
- Testable
- Production-oriented
- Simple enough for an MVP
- Extensible for future growth

Do not over-engineer.
Do not create unnecessary distributed complexity unless the product clearly requires it.

---

## Working Method

Before writing code, first produce a proper system design.

Follow this sequence:

1. Understand the product requirements
2. Define users, roles, and main workflows
3. Define functional requirements
4. Define non-functional requirements
5. Design the high-level architecture
6. Define the core components
7. Define data flow
8. Design the API layer
9. Design the database schema
10. Define caching strategy
11. Define security approach
12. Define observability approach
13. Define deployment approach
14. Implement the minimal production-ready version
15. Add validation, error handling, tests, and setup instructions

If any requirement is unclear, make reasonable assumptions and document them clearly.

---

## System Design Requirements

Provide a clear system design including:

### High-Level Architecture

Explain:

- Main services/components
- Responsibilities of each component
- How components communicate
- Frontend/backend/database boundaries
- External integrations if any
- Deployment model

### Component Structure

Define the major components such as:

- Frontend application
- Backend API
- Authentication module
- Business logic/services
- Database layer
- Cache layer
- Background workers if needed
- External integrations
- Observability/logging layer

For each component, explain:

- Purpose
- Responsibilities
- Inputs
- Outputs
- Dependencies

### Data Flow

Describe the main data flows.

Include:

- User request flow
- Authentication flow
- Read flow
- Write flow
- Error flow
- Cache flow if applicable
- Background job flow if applicable

### API Design

Design clean and consistent APIs.

For each API endpoint, include:

| Method | Endpoint | Purpose | Auth Required | Request | Response |
|---|---|---|---|---|---|

Also define:

- Error response format
- Validation rules
- Pagination approach if needed
- Filtering/search approach if needed
- Versioning strategy if needed

Prefer REST unless GraphQL, gRPC, or event-driven APIs are clearly better.

### Database Schema

Design a normalized and practical database schema.

Include:

- Tables/models
- Fields
- Data types
- Relationships
- Constraints
- Indexes
- Migration strategy
- Seed data if useful

Explain why the schema is designed this way.

### Caching Strategy

Define caching only where it is useful.

Include:

- What should be cached
- What should not be cached
- Cache key design
- TTL strategy
- Cache invalidation strategy
- Risks of stale data
- Whether cache is needed in MVP or future phase

Do not add caching unnecessarily if the MVP does not need it.

### Security Design

Include basic production security:

- Authentication
- Authorization
- Input validation
- Rate limiting where needed
- Secure headers
- CORS policy
- Secret management
- Password/token handling if applicable
- Least privilege access
- Safe error messages
- Audit logging if required

### Observability Design

Define how the system should be monitored and debugged.

Include:

- Application logs
- Error logs
- Request logs
- Metrics
- Health checks
- Readiness checks
- Tracing if useful
- Important alerts for production

---

## Implementation Requirements

After completing the design, implement the minimal production-ready version.

The implementation must include:

- Clean file/folder structure
- Backend API
- Frontend or client layer if applicable
- Database schema/migrations
- Validation
- Error handling
- Authentication if required
- Caching if justified
- Basic tests
- Environment variable configuration
- Local development setup
- Production build instructions
- README documentation

---

## Output Format

Return the result in this structure:

1. Product Understanding
2. Assumptions
3. Functional Requirements
4. Non-Functional Requirements
5. High-Level Architecture
6. Component Design
7. Data Flow
8. API Design
9. Database Schema
10. Caching Strategy
11. Security Design
12. Observability Design
13. File Structure
14. Implementation Code
15. Tests
16. Deployment and Setup Instructions
17. Scalability Roadmap
18. Known Limitations

---

## Important Rules

- Design first, then implement.
- Keep MVP simple but production-oriented.
- Do not over-engineer.
- Do not introduce microservices unless clearly justified.
- Do not add caching unless there is a real reason.
- Do not hardcode secrets.
- Use environment variables.
- Validate all user input.
- Handle errors consistently.
- Explain important technical decisions.
- Separate current MVP implementation from future scalability plans.

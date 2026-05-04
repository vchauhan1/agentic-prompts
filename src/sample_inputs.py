SAMPLE_INPUTS = {
    "application-development": """Build a simple internal ticket management MVP.

Requirements:
- Users can create tickets.
- Admins can assign and update tickets.
- Users can comment on tickets.
- Include API design, database schema, UI structure, and implementation plan.
""",
    "architecture": """Design a scalable architecture for a self-hosted developer portal.

The portal should support:
- Team/project management
- Kubernetes cluster registration
- GitOps application visibility
- Helm chart app catalog
- OIDC login
""",
    "refactoring": """Analyze this codebase conceptually and propose a safe refactoring plan.

Current issues:
- Large service files
- Repeated validation logic
- UI components duplicated across pages
- API error handling is inconsistent
""",
    "code-review": """Review this sample pull request:

Change:
- Adds a new /api/users/:id endpoint
- Returns full user object from database
- Frontend hides admin-only fields
- No new tests were added

Give senior code review feedback.
""",
    "debugging": """Production issue:

Users sometimes see duplicate orders after clicking checkout once.

Symptoms:
- Duplicate records appear within 1-2 seconds.
- Payment provider receives two calls.
- Frontend button has loading state but users can double-click quickly.

Find root cause and production-ready fix.
""",
    "security": """Review this design for security:

A web app stores JWT in localStorage.
Admin routes are hidden in the frontend menu.
API checks if user is logged in but does not check role on every endpoint.
Uploads are stored with original filenames.

Find risks and fixes.
""",
    "devops": """Review this deployment approach:

- Docker image uses python:latest
- No health check
- Kubernetes deployment has no resource limits
- Secrets are stored in ConfigMap
- CI/CD deploys directly to production after build

Give production readiness recommendations.
""",
    "mlops": """Design an offline RAG platform for internal documents.

Constraints:
- No internet in production
- Local LLM endpoint
- Internal PDFs and Word docs
- Need citation support
- Need access control by department
""",
    "documentation": """Generate a README for a Python FastAPI application with PostgreSQL, Docker Compose, tests, and deployment notes.""",
    "testing": """Create a test strategy for an e-commerce checkout flow with payments, inventory reservation, discounts, and order creation.""",
    "agents": """Create AI coding agent rules for a repository that uses Next.js, Prisma, PostgreSQL, and Kubernetes deployment manifests.""",
}

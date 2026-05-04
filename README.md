# Agentic Prompts

> Curated production-grade prompts, agent instructions and workflow templates for Claude, ChatGPT, Cursor, Codex, Claude Code and other AI coding agents.

---

## What is Agentic Prompts?

**Agentic Prompts** is a curated collection of professional prompts designed to help AI agents work like experienced engineers, architects, reviewers, DevOps engineers, security analysts, SREs, MLOps engineers and product builders.

These prompts are designed for real-world software engineering workflows, not toy examples.

They are useful for:

- Building production-ready applications
- Understanding large codebases
- Refactoring existing projects
- Performing code reviews
- Debugging production issues
- Performing security reviews
- Designing architecture
- Writing documentation
- Creating tests
- Building DevOps, MLOps and platform engineering workflows
- Guiding AI agents inside Cursor, Claude Code, Codex and ChatGPT

---

## Prompt Catalog

### Application Development

| Prompt | Description |
|---|---|
| [Complete Application From Scratch](prompts/application-development/complete-application-from-scratch.md) | Build a production-ready MVP application from architecture to complete implementation. |
| [Feature Development From Requirement](prompts/application-development/feature-development-from-requirement.md) | Convert a product requirement into a planned, implemented, tested and documented feature. |
| [Production Readiness Review](prompts/application-development/production-readiness-review.md) | Review an application for production readiness across reliability, security, performance and maintainability. |
| [MVP Scope Planner](prompts/application-development/mvp-scope-planner.md) | Define a realistic MVP scope, user journeys, feature boundaries and implementation roadmap. |

---

### Codebase Understanding & Refactoring

| Prompt | Description |
|---|---|
| [Codebase Understanding and Refactoring](prompts/refactoring/codebase-understanding-refactor.md) | Understand an unfamiliar codebase, identify quality issues and refactor without changing functionality. |
| [Legacy Code Modernization](prompts/refactoring/legacy-code-modernization.md) | Modernize legacy code safely while preserving existing behavior and minimizing regression risk. |
| [Duplicate Code Elimination](prompts/refactoring/duplicate-code-elimination.md) | Detect repeated logic, components, utilities and patterns, then refactor them into clean reusable structures. |
| [Code Simplification](prompts/refactoring/code-simplification.md) | Simplify complex code, reduce unnecessary abstractions and improve readability without changing behavior. |

---

### Architecture

| Prompt | Description |
|---|---|
| [System Design + Implementation](prompts/architecture/scalable-system-design-implementation.md) | Design scalable architecture and implement a minimal production-ready version. |
| [Architecture Review](prompts/architecture/architecture-review.md) | Review an existing architecture for scalability, reliability, security, maintainability and cost efficiency. |
| [Technical Design Document Generator](prompts/architecture/technical-design-document-generator.md) | Generate a structured technical design document from product or engineering requirements. |
| [Architecture Decision Record Generator](prompts/architecture/architecture-decision-record-generator.md) | Create clear ADRs documenting technical decisions, trade-offs, alternatives and consequences. |
| [Microservices Boundary Design](prompts/architecture/microservices-boundary-design.md) | Identify service boundaries, communication patterns, data ownership and decomposition strategy. |

---

### Code Review

| Prompt | Description |
|---|---|
| [Senior Code Review](prompts/code-review/senior-code-review.md) | Review code like a senior engineer with focus on correctness, maintainability, security and performance. |
| [Pull Request Review](prompts/code-review/pull-request-review.md) | Review a pull request for bugs, regressions, design issues, test coverage and production risk. |
| [Security-Focused Code Review](prompts/code-review/security-focused-code-review.md) | Review code specifically for authentication, authorization, input validation, secrets and unsafe patterns. |
| [Performance Code Review](prompts/code-review/performance-code-review.md) | Analyze code for inefficient algorithms, expensive queries, unnecessary renders and scalability issues. |
| [Test Coverage Review](prompts/code-review/test-coverage-review.md) | Review whether the code has meaningful test coverage and suggest missing unit, integration and regression tests. |

---

### Debugging

| Prompt | Description |
|---|---|
| [Senior Debugging Engineer](prompts/debugging/senior-debugging-engineer.md) | Investigate production bugs systematically, identify root cause, cover edge cases and propose production-ready fixes. |
| [Log and Error Analysis](prompts/debugging/log-and-error-analysis.md) | Analyze logs, stack traces and error messages to identify root cause and recommend fixes. |
| [Production Incident Debugging](prompts/debugging/production-incident-debugging.md) | Debug production incidents with focus on impact, timeline, root cause, mitigation, rollback and prevention. |
| [Failing Test Debugger](prompts/debugging/failing-test-debugger.md) | Investigate failing tests and identify whether the issue is code, test, data, environment, or dependency related. |
| [Regression Debugging](prompts/debugging/regression-debugging.md) | Analyze a regression after recent changes and identify the change that likely introduced the issue. |

---

### Security

| Prompt | Description |
|---|---|
| [Security Review](prompts/security/security-review.md) | Perform secure code review, threat modeling, secret scanning, dependency review and hardening guidance. |
| [Threat Modeling](prompts/security/threat-modeling.md) | Analyze a system using attacker mindset and identify threats, trust boundaries, abuse cases and mitigations. |
| [Authentication and Authorization Review](prompts/security/authentication-authorization-review.md) | Review login, session, token, RBAC, permission and access-control flows for security weaknesses. |
| [Secrets and Configuration Review](prompts/security/secrets-configuration-review.md) | Detect hardcoded secrets, unsafe environment handling, insecure defaults and configuration risks. |
| [Dependency Security Review](prompts/security/dependency-security-review.md) | Review package dependencies, vulnerable libraries, supply-chain risks and update strategy. |
| [API Security Review](prompts/security/api-security-review.md) | Review API endpoints for validation, authorization, rate limiting, error handling and data exposure risks. |
| [Infrastructure Hardening Review](prompts/security/infrastructure-hardening-review.md) | Review infrastructure, containers, Kubernetes, Linux hosts and deployment configs for hardening gaps. |

---

### DevOps & Platform Engineering

| Prompt | Description |
|---|---|
| [DevOps Platform Review](prompts/devops/devops-platform-review.md) | Review DevOps architecture, CI/CD, environments, deployment strategy, reliability and operational maturity. |
| [CI/CD Pipeline Generator](prompts/devops/cicd-pipeline-generator.md) | Generate production-ready CI/CD pipelines with build, test, scan, package, deploy, rollback and approval stages. |
| [CI/CD Pipeline Review](prompts/devops/cicd-pipeline-review.md) | Review existing pipelines for reliability, security, speed, maintainability and rollback safety. |
| [Kubernetes Troubleshooting](prompts/devops/kubernetes-troubleshooting.md) | Diagnose Kubernetes issues across pods, services, ingress, DNS, networking, storage, scheduling and resources. |
| [Kubernetes Production Readiness](prompts/devops/kubernetes-production-readiness.md) | Review Kubernetes workloads for security, reliability, scaling, probes, resources and operational readiness. |
| [GitOps Implementation](prompts/devops/gitops-implementation.md) | Design and implement GitOps workflows using tools like Argo CD or Flux with environment promotion and rollback. |
| [Terraform Review](prompts/devops/terraform-review.md) | Review Terraform or OpenTofu code for structure, state handling, modules, security, drift and maintainability. |
| [Pulumi Review](prompts/devops/pulumi-review.md) | Review Pulumi infrastructure code for provider structure, configuration, security, modularity and automation readiness. |
| [Ansible Role Review](prompts/devops/ansible-role-review.md) | Review Ansible roles for idempotency, variable structure, handlers, security, testing and reuse. |
| [Dockerfile and Compose Review](prompts/devops/dockerfile-compose-review.md) | Review Dockerfiles and Docker Compose files for security, size, performance, environment handling and production readiness. |
| [Observability Design](prompts/devops/observability-design.md) | Design logging, metrics, tracing, dashboards, alerts and SLO-based monitoring for production systems. |
| [Incident Postmortem Generator](prompts/devops/incident-postmortem-generator.md) | Generate a blameless incident postmortem with timeline, root cause, impact, mitigation and action items. |

---

### MLOps & AI Engineering

| Prompt | Description |
|---|---|
| [MLOps Platform Design](prompts/mlops/mlops-platform-design.md) | Design an end-to-end MLOps platform for data ingestion, training, model registry, deployment, monitoring and governance. |
| [LLM Application Architecture](prompts/mlops/llm-application-architecture.md) | Design production-grade LLM applications with prompt management, RAG, evaluation, safety, observability and deployment. |
| [RAG Pipeline Design](prompts/mlops/rag-pipeline-design.md) | Design a Retrieval-Augmented Generation pipeline with ingestion, chunking, embeddings, vector database, retrieval and evaluation. |
| [Vector Database Review](prompts/mlops/vector-database-review.md) | Review vector database schema, indexing strategy, metadata filters, retrieval quality and scaling approach. |
| [Model Deployment Review](prompts/mlops/model-deployment-review.md) | Review model serving architecture for latency, throughput, GPU usage, autoscaling, batching and rollback strategy. |
| [LLM Evaluation Framework](prompts/mlops/llm-evaluation-framework.md) | Design an evaluation framework for LLM output quality, hallucination, safety, regression testing and prompt/version tracking. |
| [AI Agent Design Review](prompts/mlops/ai-agent-design-review.md) | Review agentic workflows, tool usage, memory, planning, guardrails, observability and failure handling. |
| [Inference Gateway Design](prompts/mlops/inference-gateway-design.md) | Design a unified gateway for routing text, vision, speech and embedding requests to suitable inference backends. |
| [Model Observability](prompts/mlops/model-observability.md) | Design monitoring for model latency, errors, token usage, drift, quality, cost and user feedback. |
| [Offline AI Deployment](prompts/mlops/offline-ai-deployment.md) | Plan secure offline or air-gapped AI deployment with local models, registries, vector stores, observability and update strategy. |

---

### Documentation

| Prompt | Description |
|---|---|
| [README Generator](prompts/documentation/readme-generator.md) | Generate a professional README with setup, architecture, usage, development, testing and deployment instructions. |
| [Developer Documentation](prompts/documentation/developer-documentation.md) | Create developer-focused documentation for local setup, project structure, contribution flow and troubleshooting. |
| [API Documentation](prompts/documentation/api-documentation.md) | Generate clear API documentation with endpoints, request/response examples, authentication and error formats. |
| [Runbook Generator](prompts/documentation/runbook-generator.md) | Create operational runbooks for deployment, incident response, troubleshooting, rollback and maintenance. |
| [Architecture Documentation](prompts/documentation/architecture-documentation.md) | Generate architecture documentation covering system overview, components, data flow, security and deployment model. |

---

### Testing & Quality Assurance

| Prompt | Description |
|---|---|
| [Test Strategy Generator](prompts/testing/test-strategy-generator.md) | Design a complete testing strategy including unit, integration, E2E, performance, security and regression tests. |
| [Unit Test Generator](prompts/testing/unit-test-generator.md) | Generate meaningful unit tests for business logic, utilities, validation and edge cases. |
| [Integration Test Generator](prompts/testing/integration-test-generator.md) | Generate integration tests for APIs, databases, services, queues and external dependencies. |
| [End-to-End Test Generator](prompts/testing/e2e-test-generator.md) | Generate end-to-end test scenarios for critical user journeys and production workflows. |
| [Quality Gate Review](prompts/testing/quality-gate-review.md) | Review whether a change is ready to merge based on tests, linting, type checks, security and build status. |

---

### Agent Instructions

| Prompt | Description |
|---|---|
| [Cursor Rules Template](prompts/agents/cursor-rules-template.md) | Create reusable Cursor IDE rules for safe, structured, production-grade AI-assisted development. |
| [Claude Code Instructions](prompts/agents/claude-code-instructions.md) | Create Claude Code instructions for repository inspection, planning, implementation, testing and reporting. |
| [Codex Task Template](prompts/agents/codex-task-template.md) | Create Codex-ready task instructions for controlled code generation, editing, debugging and verification. |
| [AI Coding Agent Behavior Rules](prompts/agents/ai-coding-agent-behavior-rules.md) | Define behavioral rules for coding agents to avoid guessing, overengineering, unsafe edits and unverified changes. |
| [Repository Task Execution Plan](prompts/agents/repository-task-execution-plan.md) | Guide AI agents to analyze a repository, plan work, modify files safely and report validation results. |

---

## Prompt Design Principles

Every prompt in this repository follows these principles:

1. Understand before acting
2. Preserve existing functionality
3. Prefer production-ready output
4. Avoid over-engineering
5. Make changes reviewable
6. State assumptions clearly
7. Validate the work

---

## Contribution Guidelines

Contributions are welcome.

You can contribute:

- New prompts
- Improved prompt versions
- Tool-specific adaptations
- Cursor rules
- Claude Code workflows
- Codex task templates
- Real-world usage examples

Before contributing, make sure your prompt is:

- Practical
- Clear
- Safe
- Structured
- Production-oriented
- Reusable



## Final Note

Good prompts are not magic.

They are engineering instructions.

The better the instruction, the better the agent.

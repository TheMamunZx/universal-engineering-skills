---
name: backend-engineer
description: "Build reliable server-side application logic and services."
---

# backend-engineer

## Purpose
Implement business logic, persistence, integrations, and operational behavior behind an application.

## Use this skill when
Use this skill when the task materially requires: service boundaries, request lifecycle, validation, authorization, transactions, jobs, observability, and resilience.

## Scope
Service boundaries, request lifecycle, validation, authorization, transactions, jobs, observability, and resilience.

## Out of scope
Do not bypass authorization or put secrets in source/config committed to version control.

## Required inputs
API contract, data model, business rules, runtime, security requirements, traffic expectations.

## Workflow
1. Inspect current architecture and establish service ownership.
2. Validate inputs at boundaries and enforce authorization in server-side code.
3. Keep business logic separate from transport and persistence concerns.
4. Use transactions, idempotency, and bounded background jobs where appropriate.
5. Add structured logs, metrics, tracing, and safe error handling.
6. Test normal, edge, permission, concurrency, and failure cases.

## Expected outputs
Backend services, migrations if needed, tests, API docs, operational configuration.

## Quality gates
Behavior is tested; authorization is server-enforced; logs contain no secrets or sensitive payloads.

## Handoffs and collaboration
Coordinate with: api-engineer, database-engineer, authentication-engineer, application-security-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

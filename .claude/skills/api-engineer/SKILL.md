---
name: api-engineer
description: "Design and implement clear, versioned application APIs."
---

# api-engineer

## Purpose
Create stable, documented interfaces for application and service integration.

## Use this skill when
Use this skill when the task materially requires: rEST or RPC resource design, schemas, validation, pagination, versioning, error formats, idempotency, and contract tests.

## Scope
REST or RPC resource design, schemas, validation, pagination, versioning, error formats, idempotency, and contract tests.

## Out of scope
Do not assume authentication alone grants access to every resource; do not expose internal fields by default.

## Required inputs
Consumer use cases, domain model, auth model, compatibility needs, expected traffic.

## Workflow
1. Model resources and operations around use cases, not database tables alone.
2. Define schemas, constraints, pagination, sorting, filtering, and error responses.
3. Specify authentication, authorization, rate limits, and idempotency semantics.
4. Choose compatible versioning and deprecation rules.
5. Implement validation and avoid leaking stack traces or internal data.
6. Generate and run contract tests against consumer expectations.

## Expected outputs
API specification, endpoint implementation, examples, contract tests, versioning plan.

## Quality gates
API behavior is documented, validated, version-safe, and authorization-tested.

## Handoffs and collaboration
Coordinate with: backend-engineer, authentication-engineer, api-security-engineer, documentation-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

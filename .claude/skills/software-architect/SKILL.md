---
name: software-architect
description: "Design software architecture for new products and major changes."
---

# software-architect

## Purpose
Turn requirements and constraints into a coherent, evolvable software architecture.

## Use this skill when
Use this skill when the task materially requires: define system boundaries, modules, interfaces, data ownership, deployment shape, quality attributes, and architecture decision records.

## Scope
Define system boundaries, modules, interfaces, data ownership, deployment shape, quality attributes, and architecture decision records.

## Out of scope
Do not implement every module or choose technologies without project constraints; delegate detailed subsystem design to specialists.

## Required inputs
Product brief, users, functional requirements, constraints, existing stack, scale and reliability expectations.

## Workflow
1. Extract functional and non-functional requirements; mark assumptions explicitly.
2. Identify bounded contexts, trust boundaries, external dependencies, and critical data flows.
3. Compare at least two viable architecture options against the stated constraints.
4. Choose the simplest option that meets requirements; record trade-offs and reversibility.
5. Define module ownership, API contracts, data model boundaries, deployment topology, and observability.
6. Create migration and rollout steps for changes to existing systems.

## Expected outputs
Architecture overview, component diagram (Mermaid), interface contracts, decision records, risk list, phased implementation plan.

## Quality gates
Every major requirement maps to a component or an explicit non-goal; decisions and risks are reviewable.

## Handoffs and collaboration
Coordinate with: system-design-engineer, requirements-analyst, backend-engineer, database-engineer, application-security-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

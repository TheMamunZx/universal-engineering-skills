---
name: android-architecture-engineer
description: "Design maintainable Android application architecture."
---

# android-architecture-engineer

## Purpose
Define Android layers, state ownership, navigation, data flow, and lifecycle behavior.

## Use this skill when
Use this skill when the task materially requires: kotlin/Compose or existing UI stack, ViewModel/state, repositories, offline data, dependency injection, modularization.

## Scope
Kotlin/Compose or existing UI stack, ViewModel/state, repositories, offline data, dependency injection, modularization.

## Out of scope
Do not rewrite an established architecture without a migration case; do not duplicate general Android feature implementation.

## Required inputs
App size, min SDK, team constraints, state/data sources, offline and navigation needs.

## Workflow
1. Inspect current app patterns and platform targets.
2. Choose a pragmatic architecture matching app complexity.
3. Define UI state, domain logic, repositories, persistence, and dependency boundaries.
4. Plan navigation, lifecycle, saved state, and background work.
5. Define test seams and module ownership.
6. Document migration steps and architectural constraints.

## Expected outputs
Architecture diagram, module boundaries, state/data contracts, migration plan.

## Quality gates
State ownership and dependency direction are clear; architecture is testable and lifecycle-safe.

## Handoffs and collaboration
Coordinate with: android-app-engineer, android-performance-engineer, database-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

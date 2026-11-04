---
name: frontend-engineer
description: "Implement accessible, responsive, maintainable frontend applications."
---

# frontend-engineer

## Purpose
Turn product designs and API contracts into robust user interfaces.

## Use this skill when
Use this skill when the task materially requires: component architecture, state, routing, forms, responsive layout, accessibility, performance, and frontend tests.

## Scope
Component architecture, state, routing, forms, responsive layout, accessibility, performance, and frontend tests.

## Out of scope
Do not invent backend behavior or trade accessibility for visual effects.

## Required inputs
Design references, routes, API schemas, supported browsers, brand tokens, accessibility targets.

## Workflow
1. Inspect existing framework, design system, routes, and conventions.
2. Translate flows into semantic components and explicit states.
3. Implement responsive layout, loading/empty/error/success states, and keyboard access.
4. Integrate typed API contracts and validate user input.
5. Test key breakpoints, interactions, accessibility, and performance.
6. Document changed routes, components, and known limitations.

## Expected outputs
Frontend components/pages, state model, responsive behavior, tests, implementation notes.

## Quality gates
Core flows work across supported viewports; keyboard and screen-reader basics are addressed.

## Handoffs and collaboration
Coordinate with: ui-ux-engineer, backend-engineer, api-engineer, test-automation-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

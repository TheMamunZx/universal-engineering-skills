---
name: requirements-analyst
description: "Elicit, clarify, and validate software requirements."
---

# requirements-analyst

## Purpose
Convert an ambiguous idea into testable requirements and explicit acceptance criteria.

## Use this skill when
Use this skill when the task materially requires: stakeholder questions, user journeys, functional requirements, non-functional requirements, constraints, assumptions, and acceptance tests.

## Scope
Stakeholder questions, user journeys, functional requirements, non-functional requirements, constraints, assumptions, and acceptance tests.

## Out of scope
Do not invent stakeholder intent, silently expand scope, or make architecture decisions on behalf of the owner.

## Required inputs
Problem statement, target users, existing workflow, constraints, examples, and known pain points.

## Workflow
1. Restate the problem and identify users, actors, and outcomes.
2. Separate must-have, should-have, could-have, and out-of-scope items.
3. Write user journeys and edge cases, including failure and recovery states.
4. Make non-functional requirements measurable where possible.
5. Turn requirements into observable acceptance criteria and test scenarios.
6. Resolve contradictions; keep unresolved questions visible rather than guessing.

## Expected outputs
Requirements specification, user stories, acceptance criteria, glossary, assumptions and open-questions log.

## Quality gates
Each requirement is unambiguous, testable, prioritized, and traceable to a user or business need.

## Handoffs and collaboration
Coordinate with: project-planner, software-architect, ui-ux-engineer, test-automation-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

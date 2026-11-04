---
name: skill-builder
description: "Create, improve, and validate portable AI agent skills."
---

# skill-builder

## Purpose
Turn a repeatable task into a focused, reusable SKILL.md package.

## Use this skill when
Use this skill when the task materially requires: skill discovery description, scope boundaries, inputs/outputs, progressive disclosure, references, scripts, and tests.

## Scope
Skill discovery description, scope boundaries, inputs/outputs, progressive disclosure, references, scripts, and tests.

## Out of scope
Do not create a skill that only renames another skill, claims unavailable tools, or embeds secrets.

## Required inputs
Task examples, target agent platforms, existing skills, reference materials, expected outcomes.

## Workflow
1. Confirm the task is repeatable and distinct from existing skills.
2. Write a concise trigger description and precise scope/out-of-scope boundaries.
3. Define inputs, outputs, staged workflow, safety gates, and handoffs.
4. Put deep material in references; keep SKILL.md focused and composable.
5. Add scripts only when deterministic local automation materially helps.
6. Validate frontmatter, naming, file links, and test with representative prompts.

## Expected outputs
Skill folder, SKILL.md, optional references/scripts/examples, validation report, catalog entry.

## Quality gates
Skill has a unique purpose, valid portable metadata, and testable outputs.

## Handoffs and collaboration
Coordinate with: skill-orchestrator, documentation-engineer, engineering-researcher. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

---
name: skill-orchestrator
description: "Select and coordinate relevant skills for a multi-step user task."
---

# skill-orchestrator

## Purpose
Load only the smallest useful set of specialist skills and coordinate handoffs.

## Use this skill when
Use this skill when the task materially requires: task classification, dependency order, parallelization, conflict resolution, and outcome tracking.

## Scope
Task classification, dependency order, parallelization, conflict resolution, and outcome tracking.

## Out of scope
Do not load every skill by default or replace the documentary-specific ai-documentary-studio skill.

## Required inputs
User goal, constraints, project context, skill catalog and available tools.

## Workflow
1. Clarify the outcome and identify task domain, risk, and constraints.
2. Search the skill catalog by responsibility and select only relevant specialists.
3. Check each selected skill’s boundaries and resolve overlaps before work starts.
4. Sequence prerequisites; parallelize only independent research or review.
5. Track artifacts, blockers, decisions, and approvals across handoffs.
6. Verify outputs and report what was not completed or tested.

## Expected outputs
Selected skill sequence, rationale, handoff checklist, final completion summary.

## Quality gates
No redundant skill loading; handoffs are explicit; claims of completion match verified artifacts.

## Handoffs and collaboration
Coordinate with: project-planner, engineering-researcher. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

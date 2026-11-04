---
name: ai-agent-architect
description: "Design tool-using AI agents with controlled autonomy."
---

# ai-agent-architect

## Purpose
Translate a task into bounded agent loops, tool permissions, state, and approval gates.

## Use this skill when
Use this skill when the task materially requires: agent roles, planning, tool registry, state, checkpoints, budgets, safety, observability, and stop conditions.

## Scope
Agent roles, planning, tool registry, state, checkpoints, budgets, safety, observability, and stop conditions.

## Out of scope
Do not create agents with unrestricted filesystem/network/account access or uncontrolled self-replication.

## Required inputs
Task class, environment, available tools, permission model, approval needs, failure cost.

## Workflow
1. Define task boundaries, success conditions, and prohibited actions.
2. Choose deterministic workflows before introducing open-ended planning.
3. Specify tools with schemas, validation, least privilege, and explicit side effects.
4. Add step/time/token budgets, cancellation, checkpoints, and approval gates.
5. Persist only necessary state and make actions auditable.
6. Test prompt injection, tool failure, ambiguity, loops, and partial completion.

## Expected outputs
Agent architecture, state machine, tool contracts, permission matrix, test scenarios.

## Quality gates
Agent actions are bounded, reversible where possible, permission-checked, and auditable.

## Handoffs and collaboration
Coordinate with: coding-agent-engineer, function-calling-engineer, multi-agent-engineer, application-security-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

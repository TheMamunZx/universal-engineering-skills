---
name: multi-agent-engineer
description: "Coordinate specialized AI agents with explicit responsibilities."
---

# multi-agent-engineer

## Purpose
Build multi-agent workflows where collaboration improves quality without uncontrolled complexity.

## Use this skill when
Use this skill when the task materially requires: role decomposition, message contracts, shared state, delegation, consensus, budgets, and conflict resolution.

## Scope
Role decomposition, message contracts, shared state, delegation, consensus, budgets, and conflict resolution.

## Out of scope
Do not add agents for tasks a single deterministic workflow can handle; avoid recursive unbounded delegation.

## Required inputs
Task decomposition, agent capabilities, shared tools, concurrency limits, budget, success metrics.

## Workflow
1. Determine whether parallel specialists offer measurable value.
2. Define each agent role, input/output schema, and forbidden responsibilities.
3. Design a coordinator and bounded delegation graph.
4. Manage shared artifacts with versioning and conflict rules.
5. Set budgets, timeouts, retries, and escalation to a human.
6. Evaluate coordination overhead, disagreement handling, and end-to-end correctness.

## Expected outputs
Agent roster, communication protocol, orchestration graph, failure policy, evaluation plan.

## Quality gates
Agent roles do not overlap ambiguously; the workflow terminates and produces auditable results.

## Handoffs and collaboration
Coordinate with: ai-agent-architect, skill-orchestrator, engineering-researcher. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

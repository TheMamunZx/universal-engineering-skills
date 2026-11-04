---
name: agent-memory-engineer
description: "Design useful, privacy-conscious memory and context systems for agents."
---

# agent-memory-engineer

## Purpose
Persist only relevant information and retrieve it accurately across tasks.

## Use this skill when
Use this skill when the task materially requires: short-term state, long-term memory, summaries, retrieval, expiry, provenance, user controls, and privacy.

## Scope
Short-term state, long-term memory, summaries, retrieval, expiry, provenance, user controls, and privacy.

## Out of scope
Do not store secrets, sensitive personal data, or assumptions as facts; do not make memory irreversible.

## Required inputs
Memory use cases, data types, retention needs, privacy requirements, storage options.

## Workflow
1. Separate working context, project state, preferences, and durable facts.
2. Define what may be stored, for how long, and with what provenance.
3. Exclude credentials and unnecessary sensitive information by default.
4. Implement user-visible review, correction, expiry, and deletion controls.
5. Retrieve memories with relevance and freshness checks.
6. Test stale, contradictory, missing, and cross-user isolation cases.

## Expected outputs
Memory schema, lifecycle policy, retrieval strategy, deletion/update behavior, evaluations.

## Quality gates
Stored facts are sourced, editable, scoped, and deletable; secrets are excluded.

## Handoffs and collaboration
Coordinate with: ai-agent-architect, rag-engineer, database-engineer, application-security-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

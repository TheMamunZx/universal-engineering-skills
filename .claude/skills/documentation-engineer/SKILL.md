---
name: documentation-engineer
description: "Create and maintain accurate developer and user documentation."
---

# documentation-engineer

## Purpose
Make software behavior, setup, interfaces, and operational procedures understandable.

## Use this skill when
Use this skill when the task materially requires: rEADME files, architecture docs, API docs, runbooks, onboarding, changelogs, and examples.

## Scope
README files, architecture docs, API docs, runbooks, onboarding, changelogs, and examples.

## Out of scope
Do not document behavior that has not been verified in source, tests, or a running system.

## Required inputs
Source code, CLI help, API schemas, configuration examples, architecture decisions, target audience.

## Workflow
1. Inspect implementation and tests to establish current truth.
2. Identify audience and choose task-oriented structure.
3. Document prerequisites, setup, configuration, workflows, examples, and failure recovery.
4. Keep examples minimal, valid, and free of real credentials.
5. Cross-check commands and links against the repository.
6. Add ownership/version notes for documentation likely to drift.

## Expected outputs
README, setup guide, API reference, runbook, troubleshooting section, change summary.

## Quality gates
A new user can follow the documented critical path; no stale or fabricated commands.

## Handoffs and collaboration
Coordinate with: software-architect, api-engineer, devops-engineer, skill-builder. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

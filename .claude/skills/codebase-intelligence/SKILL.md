---
name: codebase-intelligence
description: "Help agents understand repositories and select relevant code context."
---

# codebase-intelligence

## Purpose
Build reliable repository maps and context retrieval for engineering tasks.

## Use this skill when
Use this skill when the task materially requires: file inventory, symbols, dependency graphs, call paths, documentation indexing, and change impact.

## Scope
File inventory, symbols, dependency graphs, call paths, documentation indexing, and change impact.

## Out of scope
Do not index secrets or assume generated/vendor folders represent first-party behavior.

## Required inputs
Repository, languages, ignore rules, task description, indexing constraints.

## Workflow
1. Respect .gitignore and project-specific exclusions; scan for secrets before persistence.
2. Detect languages, build systems, entry points, and generated files.
3. Index symbols, references, tests, configs, and architecture docs.
4. Retrieve relevant context using task intent and dependency/call relationships.
5. Include file paths and line anchors for traceability.
6. Refresh incrementally and detect stale index state.

## Expected outputs
Repository map, symbol/dependency index, relevant-file set, impact summary.

## Quality gates
Retrieved context is traceable, scoped to the repository, and excludes secret material.

## Handoffs and collaboration
Coordinate with: coding-agent-engineer, software-architect, debugging-engineer, test-automation-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

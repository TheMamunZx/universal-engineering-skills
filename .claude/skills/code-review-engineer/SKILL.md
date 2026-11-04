---
name: code-review-engineer
description: "Review code for correctness, maintainability, and design quality."
---

# code-review-engineer

## Purpose
Find actionable defects and maintainability risks in a proposed change.

## Use this skill when
Use this skill when the task materially requires: behavioral correctness, edge cases, readability, duplication, complexity, API compatibility, and test coverage.

## Scope
Behavioral correctness, edge cases, readability, duplication, complexity, API compatibility, and test coverage.

## Out of scope
Do not perform a full security audit unless explicitly asked; use secure-code-reviewer for that distinct scope.

## Required inputs
Diff or changed files, project conventions, requirements, tests, and runtime context.

## Workflow
1. Read project instructions and understand the intended behavior before reviewing.
2. Inspect the entire diff and relevant call sites, not isolated lines only.
3. Trace inputs, state changes, error paths, and backward compatibility.
4. Check tests against behavior and identify missing edge cases.
5. Report only reproducible or well-grounded findings, ranked by impact.
6. Separate blocking defects from suggestions; do not rewrite code unless asked.

## Expected outputs
Prioritized review findings with file/line references, rationale, severity, and suggested fixes.

## Quality gates
Findings are specific, actionable, evidence-backed, and avoid style-only noise.

## Handoffs and collaboration
Coordinate with: secure-code-reviewer, test-automation-engineer, debugging-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

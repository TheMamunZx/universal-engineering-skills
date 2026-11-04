---
name: debugging-engineer
description: "Diagnose and fix software defects systematically."
---

# debugging-engineer

## Purpose
Find the root cause of a reproducible failure and verify the smallest safe correction.

## Use this skill when
Use this skill when the task materially requires: reproduction, logs, traces, state inspection, bisecting, hypotheses, and regression tests.

## Scope
Reproduction, logs, traces, state inspection, bisecting, hypotheses, and regression tests.

## Out of scope
Do not change unrelated code or conceal symptoms without identifying the root cause.

## Required inputs
Observed failure, steps to reproduce, logs, environment, expected behavior, recent changes.

## Workflow
1. Reproduce the issue and record exact environment and conditions.
2. Form competing hypotheses and collect evidence to eliminate them.
3. Narrow the failure to a minimal path or recent change.
4. Fix the root cause with the smallest maintainable change.
5. Add a regression test that fails before and passes after the fix.
6. Run relevant tests and describe any remaining uncertainty.

## Expected outputs
Root-cause analysis, minimal patch, regression test, verification summary.

## Quality gates
Fix is tied to evidence and protected by a regression test.

## Handoffs and collaboration
Coordinate with: test-automation-engineer, codebase-intelligence, reliability-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

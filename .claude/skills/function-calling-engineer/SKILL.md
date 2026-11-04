---
name: function-calling-engineer
description: "Design reliable function and tool calling interfaces for AI systems."
---

# function-calling-engineer

## Purpose
Make model-selected actions structured, validated, and safe to execute.

## Use this skill when
Use this skill when the task materially requires: jSON schemas, tool descriptions, argument validation, dispatch, authorization, idempotency, and result formatting.

## Scope
JSON schemas, tool descriptions, argument validation, dispatch, authorization, idempotency, and result formatting.

## Out of scope
Do not execute model output directly as shell/code or treat model intent as user authorization.

## Required inputs
Tool list, model/provider, side-effect classification, auth model, expected result types.

## Workflow
1. Describe each tool using concise purpose, inputs, outputs, and side effects.
2. Define strict schemas, enums, bounds, and required fields.
3. Validate and authorize arguments independently of the model.
4. Use allowlisted dispatch; never eval arbitrary generated code.
5. Add idempotency and confirmation for consequential mutations.
6. Return structured success/error results and test adversarial arguments.

## Expected outputs
Tool schema registry, dispatcher, validation layer, permission rules, test cases.

## Quality gates
No unvalidated model arguments reach privileged functions; mutations require proper authorization.

## Handoffs and collaboration
Coordinate with: ai-agent-architect, mcp-server-engineer, coding-agent-engineer, application-security-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

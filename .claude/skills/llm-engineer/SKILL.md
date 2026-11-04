---
name: llm-engineer
description: "Design and integrate large language model systems."
---

# llm-engineer

## Purpose
Build reliable LLM-backed capabilities with explicit model, prompt, context, and evaluation choices.

## Use this skill when
Use this skill when the task materially requires: model selection criteria, prompting, context assembly, structured output, streaming, inference, and provider abstraction.

## Scope
Model selection criteria, prompting, context assembly, structured output, streaming, inference, and provider abstraction.

## Out of scope
Do not claim a model is free, unlimited, or available without current provider verification; do not train or deploy models without authorization.

## Required inputs
Use case, quality target, latency/cost constraints, model/provider options, data sensitivity, runtime environment.

## Workflow
1. Define tasks and evaluation criteria before comparing models.
2. Verify provider documentation, supported modalities, limits, pricing, and data handling at implementation time.
3. Design provider-neutral request/response interfaces where useful.
4. Create prompts with explicit output schemas, refusal/fallback behavior, and context limits.
5. Add retries with bounded backoff, timeouts, streaming handling, and rate-limit awareness.
6. Evaluate accuracy, hallucinations, latency, cost, robustness, and privacy on representative cases.

## Expected outputs
LLM architecture, provider adapter contract, prompt strategy, evaluation set, observability and fallback plan.

## Quality gates
Model claims are sourced; outputs are schema-validated; failures and costs are observable.

## Handoffs and collaboration
Coordinate with: ai-model-integration, ai-inference-optimizer, ai-evaluation-engineer, application-security-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

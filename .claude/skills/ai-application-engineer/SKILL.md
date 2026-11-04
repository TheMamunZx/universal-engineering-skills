---
name: ai-application-engineer
description: "Design complete consumer or enterprise AI applications."
---

# ai-application-engineer

## Purpose
Build a reliable AI product experience around chat, files, tools, multimodal input, and user data.

## Use this skill when
Use this skill when the task materially requires: conversation UX, model/provider routing, streaming, history, files, memory, safety, quotas, and observability.

## Scope
Conversation UX, model/provider routing, streaming, history, files, memory, safety, quotas, and observability.

## Out of scope
Do not equate app features with model capability or claim parity with a commercial product without verification.

## Required inputs
Product brief, platforms, model providers, privacy requirements, user flows, budget/latency constraints.

## Workflow
1. Define product capabilities separately from provider/model capabilities.
2. Design conversation lifecycle, context window handling, history and user controls.
3. Implement provider abstraction, streaming, cancellations, and graceful fallbacks.
4. Handle file/media ingestion with validation, privacy, and size limits.
5. Add reporting, usage visibility, rate limits, and evaluation hooks.
6. Test hallucination handling, data isolation, provider failure, and accessibility.

## Expected outputs
AI app architecture, feature map, provider matrix, UX states, tests, rollout plan.

## Quality gates
User controls and privacy are explicit; model limitations are surfaced honestly.

## Handoffs and collaboration
Coordinate with: llm-engineer, ai-model-integration, ai-agent-architect, rag-engineer, ui-ux-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

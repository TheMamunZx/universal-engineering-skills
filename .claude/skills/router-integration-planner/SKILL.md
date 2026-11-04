---
name: router-integration-planner
description: "Plan safe integration with a configured API router"
---

# router-integration-planner

## Purpose
Describe which configured routes actually support text, image, video, TTS, and STT tasks.

## Scope
Config inspection, capability matrix, schemas, auth method, quotas, async polling, retries, and redacted logging.

## Boundaries
Do not infer a route from a provider category or reveal API keys; do not claim free/unlimited service without verification.

## Required inputs
Local router config, official docs, provider IDs, approved test access, media requirements.

## Original workflow guidance (preserved from the supplied UNVELL DECODE pack)

## Objective
Describe how a configured router can serve text, image, video, TTS and STT tasks without assuming unsupported routes.

## Workflow
1. Read the router's current local configuration and official documentation supplied by the operator.
2. List only providers/models actually configured and enabled.
3. For each route record endpoint, model ID, auth method (env var only), request schema, response schema, rate limits, max duration/resolution, async polling pattern, quota/cost and license notes.
4. Test with a small, non-billable or explicitly approved request before production.
5. Handle timeouts, retries, job IDs and provider errors without duplicate charges.
6. Redact tokens and personal data in logs.
7. If video generation is not supported by a configured provider, say so and offer a local editing/animation fallback.

## Deliverable
`router_capability_matrix.md` and a provider adapter plan.

## Outputs
router_capability_matrix.md and provider adapter plan.

## Handoff
Coordinate with: ai-model-integration, documentary-media-generator, ai-voice-generation-engineer, engineering-researcher. Do not duplicate their responsibilities; provide the named artifacts and a concise handoff note.

## Completion checks
- Deliverables exist at the stated paths; do not claim a file was created unless it is present.
- Separate verified facts, supported interpretations, hypotheses, and unknowns.
- Record blockers and missing inputs explicitly.
- Never expose credentials or start paid/bulk actions without explicit approval.

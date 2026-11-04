---
name: documentary-media-generator
description: "Generate and manage documentary image/video assets from an approved storyboard."
---

# documentary-media-generator

## Purpose
Turn approved shot specifications into traceable visual media using actually configured providers or local tools.

## Use this skill when
Use this skill when the task materially requires: provider discovery, prompt dispatch, async jobs, asset naming, metadata, continuity references, and generation review.

## Scope
Provider discovery, prompt dispatch, async jobs, asset naming, metadata, continuity references, and generation review.

## Out of scope
Do not assume an image/video API exists, start paid batches without approval, or label generated reconstructions as archival footage.

## Required inputs
Approved storyboard, visual prompts, provider capability matrix, asset style guide, budget and permission.

## Workflow
1. Read router-integration-planner output and inspect real configured providers/tools.
2. Map each approved shot to a supported image/video workflow and flag unsupported shots.
3. Estimate generation count, duration, cost/quota, and storage before any paid/bulk operation.
4. Request approval before paid or large-batch generation.
5. Generate in small batches; capture job IDs, provider/model, prompt, parameters, and output paths.
6. Review continuity, artifacts, factual depiction, aspect ratio, and provenance; mark failed or missing assets.

## Expected outputs
Generated media files when tools are available, asset manifest, failed-job list, generation parameters, review notes.

## Quality gates
Only verified files are marked complete; provider capability, usage rights, and generation costs are recorded.

## Handoffs and collaboration
Coordinate with: visual-prompt-engineer, character-continuity, router-integration-planner, copyright-license-auditor. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

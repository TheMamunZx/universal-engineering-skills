---
name: computer-vision-engineer
description: "Build computer-vision pipelines for images and video."
---

# computer-vision-engineer

## Purpose
Extract visual information from approved images or video with measurable quality.

## Use this skill when
Use this skill when the task materially requires: image preprocessing, detection, segmentation, tracking, OCR integration, datasets, evaluation, and privacy.

## Scope
Image preprocessing, detection, segmentation, tracking, OCR integration, datasets, evaluation, and privacy.

## Out of scope
Do not identify private people or infer sensitive personal traits; do not process imagery beyond its authorized purpose.

## Required inputs
Image/video source, task definition, labels, privacy requirements, target platform, evaluation metric.

## Workflow
1. Clarify the visual task and what conclusions are not permitted.
2. Verify image rights and minimize personal data.
3. Prepare representative, correctly labeled datasets.
4. Select model or deterministic technique and define baseline metrics.
5. Evaluate false positives/negatives and subgroup or environment variation.
6. Add confidence thresholds, human review, and retention controls.

## Expected outputs
Vision pipeline, data preparation, model integration, evaluation report, privacy notes.

## Quality gates
Performance is measured on representative data and privacy boundaries are respected.

## Handoffs and collaboration
Coordinate with: multimodal-ai-engineer, ai-model-integration, video-processing-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

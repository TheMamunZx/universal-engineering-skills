---
name: 3d-rendering-engineer
description: "Implement 3D rendering pipelines and rendering techniques."
---

# 3d-rendering-engineer

## Purpose
Produce predictable 3D images from scene data and defined rendering requirements.

## Use this skill when
Use this skill when the task materially requires: geometry, transforms, cameras, materials, lighting, rasterization/ray tracing, shaders, and color management.

## Scope
Geometry, transforms, cameras, materials, lighting, rasterization/ray tracing, shaders, and color management.

## Out of scope
Do not conflate a rendering engine with general UI/graphics programming or promise physical accuracy without validation.

## Required inputs
Scene format, target API, quality/performance targets, platform, sample reference renders.

## Workflow
1. Define scene representation, coordinate conventions, and color pipeline.
2. Implement camera, transforms, geometry, and material models incrementally.
3. Choose rasterization or ray tracing based on target and workload.
4. Add lighting/shadow and shader features with controlled test scenes.
5. Compare output against reference images and profile frame/render time.
6. Document supported formats, precision, and visual limitations.

## Expected outputs
Renderer architecture, scene pipeline, shader plan, test scenes, image comparisons.

## Quality gates
Rendering output is deterministic enough for tests and performance is measured.

## Handoffs and collaboration
Coordinate with: graphics-engineer, game-engine-engineer, performance-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

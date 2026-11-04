---
name: game-engine-engineer
description: "Build reusable game engine systems and runtime architecture."
---

# game-engine-engineer

## Purpose
Design a maintainable real-time engine loop and supporting subsystems.

## Use this skill when
Use this skill when the task materially requires: entity/component model, scene graph, input, physics integration, rendering, audio, asset pipeline, and tools.

## Scope
Entity/component model, scene graph, input, physics integration, rendering, audio, asset pipeline, and tools.

## Out of scope
Do not duplicate specialized renderer or physics implementation without a clear engine requirement.

## Required inputs
Target platforms, game genre, rendering API, input devices, performance budget.

## Workflow
1. Define engine scope and target frame/update model.
2. Separate platform layer, core runtime, editor/tools, and game-specific logic.
3. Design entity and resource lifecycles with deterministic ownership.
4. Integrate rendering, physics, audio, input, and asset loading through clear interfaces.
5. Add profiling, debug visualization, and content validation.
6. Build a small sample game to validate the architecture.

## Expected outputs
Engine architecture, subsystem interfaces, sample project, tooling and test plan.

## Quality gates
Subsystem boundaries are clear and a sample project exercises the engine end-to-end.

## Handoffs and collaboration
Coordinate with: 3d-rendering-engineer, graphics-engineer, audio-engineer, performance-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

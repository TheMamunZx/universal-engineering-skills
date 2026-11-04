---
name: android-performance-engineer
description: "Profile and optimize Android app performance."
---

# android-performance-engineer

## Purpose
Improve startup, rendering, memory, battery, and network behavior using measurements.

## Use this skill when
Use this skill when the task materially requires: startup tracing, Compose recomposition, frame timing, memory, battery, app size, and network efficiency.

## Scope
Startup tracing, Compose recomposition, frame timing, memory, battery, app size, and network efficiency.

## Out of scope
Do not optimize from emulator-only assumptions or remove needed functionality to improve a single metric.

## Required inputs
Devices/API levels, app build, target metrics, baseline traces, representative workflows.

## Workflow
1. Define user-visible performance targets and a repeatable device/workflow.
2. Measure startup, jank/frame times, memory, CPU, battery, and network baseline.
3. Use Android profiling tools to locate actual bottlenecks.
4. Change one issue at a time and preserve accessibility/correctness.
5. Compare on representative devices and API levels.
6. Document trade-offs and regression benchmarks.

## Expected outputs
Benchmark report, profiling evidence, prioritized fixes, before/after results.

## Quality gates
Every optimization includes measurements and no unexplained functional regression.

## Handoffs and collaboration
Coordinate with: android-app-engineer, performance-engineer, test-automation-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

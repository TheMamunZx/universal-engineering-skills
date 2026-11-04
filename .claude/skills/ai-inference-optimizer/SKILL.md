---
name: ai-inference-optimizer
description: "Improve AI inference latency, throughput, and resource use."
---

# ai-inference-optimizer

## Purpose
Measure and optimize inference without sacrificing required quality.

## Use this skill when
Use this skill when the task materially requires: profiling, batching, caching, quantization assessment, concurrency, streaming, and cost/performance trade-offs.

## Scope
Profiling, batching, caching, quantization assessment, concurrency, streaming, and cost/performance trade-offs.

## Out of scope
Do not optimize from guesses or apply quantization/caching without measuring quality impact and data isolation.

## Required inputs
Model, hardware, workload distribution, latency/throughput target, baseline measurements.

## Workflow
1. Establish reproducible baseline on representative workloads.
2. Profile preprocessing, model execution, networking, and postprocessing separately.
3. Identify the dominant bottleneck before changing configuration.
4. Test batching, caching, concurrency, quantization, or smaller models one at a time.
5. Measure quality, p50/p95 latency, throughput, memory, and cost.
6. Keep only changes with measured benefit and a rollback path.

## Expected outputs
Benchmark report, optimization plan, measured before/after results, rollback plan.

## Quality gates
Before/after metrics are comparable and quality regressions are reported.

## Handoffs and collaboration
Coordinate with: llm-engineer, ai-model-integration, performance-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

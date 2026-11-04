---
name: performance-engineer
description: "Measure and improve end-to-end software performance."
---

# performance-engineer

## Purpose
Find bottlenecks and validate optimizations using representative workloads.

## Use this skill when
Use this skill when the task materially requires: profiling, latency distributions, throughput, memory, CPU, I/O, rendering, and performance budgets.

## Scope
Profiling, latency distributions, throughput, memory, CPU, I/O, rendering, and performance budgets.

## Out of scope
Do not optimize based on anecdotal impressions or hide performance regressions behind averages.

## Required inputs
Workload, baseline, performance targets, environment, profiling access.

## Workflow
1. Define user-visible metrics and reproducible workload.
2. Capture baseline p50/p95/p99 latency, throughput, and resource use.
3. Profile hot paths across client, network, storage, and compute.
4. Change one bottleneck at a time and preserve correctness.
5. Repeat benchmarks under comparable conditions.
6. Document trade-offs, hardware/environment, and regression thresholds.

## Expected outputs
Benchmark plan, profiling findings, prioritized changes, before/after measurements.

## Quality gates
Every optimization has reproducible before/after evidence and no untested correctness regression.

## Handoffs and collaboration
Coordinate with: ai-inference-optimizer, database-engineer, frontend-engineer, reliability-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

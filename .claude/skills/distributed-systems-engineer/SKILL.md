---
name: distributed-systems-engineer
description: "Design systems composed of multiple communicating processes or services."
---

# distributed-systems-engineer

## Purpose
Handle partial failure, concurrency, consistency, and communication across nodes.

## Use this skill when
Use this skill when the task materially requires: message delivery, consensus concepts, partition tolerance, replication, idempotency, ordering, and observability.

## Scope
Message delivery, consensus concepts, partition tolerance, replication, idempotency, ordering, and observability.

## Out of scope
Do not introduce distributed components where a simpler single-process design meets requirements.

## Required inputs
System boundary, consistency needs, failure assumptions, workload, infrastructure constraints.

## Workflow
1. Identify which data and operations cross process/network boundaries.
2. Define consistency and delivery guarantees explicitly.
3. Design idempotency, deduplication, ordering, retries, and dead-letter handling.
4. Model partitions, clock skew, duplicate messages, and node failure.
5. Use bounded queues and backpressure to prevent overload.
6. Test with fault injection in a controlled environment.

## Expected outputs
Distributed topology, protocol contracts, failure matrix, recovery behavior, test strategy.

## Quality gates
Partial failures have defined behavior and recovery is tested.

## Handoffs and collaboration
Coordinate with: system-design-engineer, database-engineer, network-protocol-engineer, reliability-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

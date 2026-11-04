---
name: database-engineer
description: "Design and operate application data models and queries."
---

# database-engineer

## Purpose
Provide correct, efficient, maintainable persistence for product requirements.

## Use this skill when
Use this skill when the task materially requires: schema design, migrations, indexes, transactions, query plans, backups, retention, and data access patterns.

## Scope
Schema design, migrations, indexes, transactions, query plans, backups, retention, and data access patterns.

## Out of scope
Do not handle database engine internals or tune without query/workload evidence; delegate those to database-internals-engineer.

## Required inputs
Entities, query patterns, consistency needs, data volume, retention, DB engine, uptime needs.

## Workflow
1. Identify entities, ownership, relationships, constraints, and lifecycle.
2. Choose normalization/denormalization based on access patterns.
3. Design safe, reversible migrations and data backfills.
4. Inspect query plans and add indexes based on measured workload.
5. Define transaction boundaries, isolation, backups, restore tests, and retention.
6. Test concurrent writes, constraints, migration rollback, and recovery.

## Expected outputs
ER diagram, schema/migrations, index strategy, query tests, backup/restore notes.

## Quality gates
Data integrity constraints are enforced and recovery is demonstrably testable.

## Handoffs and collaboration
Coordinate with: backend-engineer, database-internals-engineer, distributed-systems-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

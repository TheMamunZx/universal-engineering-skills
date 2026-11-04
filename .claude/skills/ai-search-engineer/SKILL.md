---
name: ai-search-engineer
description: "Build AI-assisted search and research systems."
---

# ai-search-engineer

## Purpose
Combine retrieval, ranking, filtering, and grounded synthesis for useful search results.

## Use this skill when
Use this skill when the task materially requires: query understanding, hybrid retrieval, ranking, citations, freshness, indexing, and evaluation.

## Scope
Query understanding, hybrid retrieval, ranking, citations, freshness, indexing, and evaluation.

## Out of scope
Do not claim exhaustive web coverage or use retrieved snippets as proof without reading sources.

## Required inputs
Corpus or allowed web sources, query types, freshness target, ranking objective, citation policy.

## Workflow
1. Define the searchable corpus and access/freshness boundaries.
2. Implement keyword and semantic retrieval as appropriate.
3. Use metadata filters, deduplication, and ranking/reranking.
4. Require source-level citations for generated synthesis.
5. Measure recall, precision, freshness, and source diversity.
6. Handle missing evidence and conflicting sources transparently.

## Expected outputs
Search architecture, indexing plan, ranking model, citation strategy, evaluation set.

## Quality gates
Search results are traceable, permission-filtered, and freshness-aware.

## Handoffs and collaboration
Coordinate with: rag-engineer, engineering-researcher, llm-engineer, ai-evaluation-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

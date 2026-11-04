---
name: programming-language-engineer
description: "Design a small programming language and its developer experience."
---

# programming-language-engineer

## Purpose
Specify syntax and semantics for a bounded language or DSL.

## Use this skill when
Use this skill when the task materially requires: grammar, types, expressions, control flow, runtime model, standard library, and language ergonomics.

## Scope
Grammar, types, expressions, control flow, runtime model, standard library, and language ergonomics.

## Out of scope
Do not build a full general-purpose language when a constrained DSL solves the problem.

## Required inputs
Language purpose, example programs, host runtime, safety model, target users.

## Workflow
1. Define the language use case and non-goals.
2. Write representative programs before finalizing syntax.
3. Specify lexical rules, grammar, evaluation order, and error behavior.
4. Choose static/dynamic typing and runtime semantics intentionally.
5. Define sandbox and resource limits if executing user-authored programs.
6. Create parser/runtime tests and a conformance corpus.

## Expected outputs
Language specification, grammar, semantics, examples, conformance tests.

## Quality gates
Syntax and semantics are unambiguous; errors and resource limits are defined.

## Handoffs and collaboration
Coordinate with: compiler-engineer, operating-system-engineer, test-automation-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

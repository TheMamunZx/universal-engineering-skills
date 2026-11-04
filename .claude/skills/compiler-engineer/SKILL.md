---
name: compiler-engineer
description: "Build or extend compilers, interpreters, and language toolchains."
---

# compiler-engineer

## Purpose
Translate source programs through parsing, analysis, and code generation.

## Use this skill when
Use this skill when the task materially requires: lexer/parser, AST, semantic analysis, IR, optimization, code generation, diagnostics, and tests.

## Scope
Lexer/parser, AST, semantic analysis, IR, optimization, code generation, diagnostics, and tests.

## Out of scope
Do not assume optimization preserves semantics; do not execute generated code without a defined trust model.

## Required inputs
Language grammar, target platform, runtime, sample programs, error requirements.

## Workflow
1. Define source grammar and representative accepted/rejected inputs.
2. Build lexer/parser with precise source locations.
3. Implement symbol resolution and semantic checks.
4. Choose an intermediate representation suited to the target.
5. Add optimizations only with semantic equivalence tests.
6. Generate code or interpret safely; test diagnostics and edge cases.

## Expected outputs
Compiler pipeline, AST/IR specification, implementation, diagnostics, test corpus.

## Quality gates
Compiler stages are testable and invalid programs produce useful diagnostics.

## Handoffs and collaboration
Coordinate with: programming-language-engineer, test-automation-engineer, operating-system-engineer. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

---
name: machine-learning-engineer
description: "Build end-to-end machine learning workflows."
---

# machine-learning-engineer

## Purpose
Develop a repeatable data-to-model pipeline and measure generalization.

## Use this skill when
Use this skill when the task materially requires: data preparation, feature engineering, train/validation/test splits, baselines, metrics, deployment considerations.

## Scope
Data preparation, feature engineering, train/validation/test splits, baselines, metrics, deployment considerations.

## Out of scope
Do not use evaluation data for tuning or claim model quality from a single unrepresentative metric.

## Required inputs
Problem, dataset provenance, labels, target metric, deployment constraints, fairness requirements.

## Workflow
1. Audit data provenance, schema, missingness, leakage, and label quality.
2. Create a simple baseline and define an appropriate split strategy.
3. Build feature processing fitted only on training data.
4. Train candidate models with controlled experiments.
5. Evaluate overall and subgroup performance with uncertainty where practical.
6. Document limitations, monitoring needs, and retraining triggers.

## Expected outputs
ML pipeline, baseline, evaluation report, model card, reproducibility instructions.

## Quality gates
No leakage; evaluation reflects deployment; limitations and data rights are recorded.

## Handoffs and collaboration
Coordinate with: neural-network-engineer, model-training-engineer, ai-evaluation-engineer, data governance owner. Load another skill only when its distinct responsibility is needed. Keep the boundary between this skill and collaborators explicit.

## Operating rules
- Inspect the existing project instructions, code, configuration, and conventions before proposing changes.
- Do not invent tools, APIs, model IDs, capabilities, test results, citations, or completed artifacts. Verify them.
- Prefer the smallest maintainable implementation that satisfies the stated requirements.
- Preserve existing working behavior; identify breaking changes and migration needs before making them.
- Protect credentials and personal data. Use environment variables or a secret manager; never put secrets in source files, prompts, logs, or generated examples.
- Ask for approval before paid services, production changes, external publication, destructive actions, or large batch jobs.
- Report exactly what changed, what was tested, test results, and what remains unverified.

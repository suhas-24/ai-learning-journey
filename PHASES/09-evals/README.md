# Phase 09 - Evals, Observability, and Regression Control

This module teaches how to measure an AI system honestly. You will learn how to define success, build useful datasets, score outputs and trajectories, instrument traces, and convert production failures into permanent tests.

Recommended order:

1. [Evaluation Design and Golden Datasets](./chapters/01-evaluation-design-and-golden-datasets.md)
2. [Metrics, Rubrics, and Score Interpretation](./chapters/02-metrics-rubrics-and-score-interpretation.md)
3. [Observability, Traces, and Runtime Signals](./chapters/03-observability-traces-and-runtime-signals.md)
4. [Regression Management and Failure Loops](./chapters/04-regression-management-and-failure-loops.md)
5. [Labs](./labs/01-build-a-golden-dataset.md)
6. [Checkpoints](./checkpoints.md)
7. [Troubleshooting](./troubleshooting.md)

Supporting references:

- [Metrics Catalog](./snippets/metrics-catalog.md)
- [Trace Schema](./snippets/trace-schema.md)

## What you will learn

- how to define "good" before changing prompts, models, or workflows
- how to separate answer quality, retrieval quality, and tool behavior
- what to log so an incident can be debugged after the fact
- how to stop regressions by turning failures into repeatable checks

## Completion standard

You are done with this phase when you can build a small golden dataset, choose metrics that match a task, instrument the key runtime signals, and explain which failures should block a merge.

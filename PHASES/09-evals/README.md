# Phase 09 - Evals, Observability, and Regression Control

This module teaches how to measure an AI system honestly.

An `eval` is a structured check that asks whether the system is doing its job. `Observability` means being able to see what happened during a real run. A `regression` is when a change accidentally makes something worse that used to work. We begin with those simple ideas and then build toward datasets, metrics, traces, and safety gates.

If those words are unfamiliar, start with a school test. Evals are the test, observability is the ability to watch how the student solved the problem, and regression control is the habit of noticing when a new lesson accidentally makes the student worse.

Recommended order:

1. [Evaluation Design and Golden Datasets](./chapters/01-evaluation-design-and-golden-datasets.md)
2. [Metrics, Rubrics, and Score Interpretation](./chapters/02-metrics-rubrics-and-score-interpretation.md)
3. [Observability, Traces, and Runtime Signals](./chapters/03-observability-traces-and-runtime-signals.md)
4. [Regression Management and Failure Loops](./chapters/04-regression-management-and-failure-loops.md)
5. [Labs](./labs/lab-01-build-a-golden-dataset.md)
6. [Checkpoints](./checkpoints.md)
7. [Troubleshooting](./troubleshooting.md)

Supporting references:

- [Metrics Catalog](./snippets/metrics-catalog.md)
- [Trace Schema](./snippets/trace-schema.md)

## What you will learn

- what evaluation, observability, and regression mean in plain language
- how to define "good" before changing prompts, models, or workflows
- how to separate answer quality, retrieval quality, and tool behavior
- what to log so an incident can be debugged after the fact
- how to stop regressions by turning failures into repeatable checks

## Why this matters

Without evals, teams often ship changes that look fine in a demo but fail on real work. Without observability, you can see that something broke but not why. Without regression control, the same bug comes back again and again.

## Completion standard

You are done with this phase when you can build a small golden dataset, choose metrics that match a task, instrument the key runtime signals, and explain which failures should block a merge.

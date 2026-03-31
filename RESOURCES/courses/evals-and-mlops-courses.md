# Evals And MLOps Courses

This guide covers the resources that teach how to measure model systems, compare experiments, and build confidence that a change actually improved the product.

An `eval` is just a test with a purpose. It tells you whether a change made the system better, worse, or different in a way that matters.

## How To Use This Guide

- Start here when opinions are not enough and you need a repeatable way to compare versions.
- Build the habit of measuring before you change.
- Always ask what the metric can miss, not just what it can show.

## Weights & Biases AI Academy: MLOps And Evals

### What it teaches

This course explains evaluation as an operating system for improvement. It helps you think in terms of datasets, metrics, experiment logs, regressions, and repeatable comparisons instead of gut feeling.

### Core topics and subtopics

- Experiment tracking: recording prompts, runs, metrics, and artifacts.
- Dataset thinking: creating evaluation sets that represent real tasks.
- Metric design: choosing what to measure and what each metric misses.
- Regression control: comparing changes against a baseline.
- Operational loops: turning evaluation results into development priorities.

### When to use it

- Best in Phase 9.
- Useful in Phase 7 if you are already building a harness and need measurement attached to it.

### Watch for

- A number is only useful if you understand what it leaves out.

## How To Practice Evals After The Course

- Build a tiny evaluation set before changing prompts or retrieval.
- Compare at least two system versions against the same dataset.
- Write down what a metric failed to capture. That keeps you from worshipping a number.

## Companion Guides

- [../tools/evals-observability-tools.md](../tools/evals-observability-tools.md)
- [../books/ml-foundations-and-thinking.md](../books/ml-foundations-and-thinking.md)
- [../newsletters/technical-analysis-and-research-interpretation.md](../newsletters/technical-analysis-and-research-interpretation.md)

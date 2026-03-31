# Evals And Observability Tools

This guide covers the tools that teach how to see inside an LLM system, compare versions, and measure whether changes are actually improving quality.

`Observability` means being able to see what the system did, not just what answer it produced. `Tracing` is one way to follow the path step by step.

The tools below are not model providers. They are support tools that help you inspect runs, compare experiments, and measure quality.

## How To Use This Guide

- Start here when a system seems to work, but you cannot explain why.
- Learn to inspect the path, not just the final answer.
- Use the same test set when comparing versions.

## Langfuse

Langfuse is an observability platform for LLM applications.

### What it teaches

Langfuse teaches trace-based visibility. It helps you inspect prompt versions, request paths, costs, and failures across a workflow instead of staring at one final answer.

### Core topics and subtopics

- End-to-end traces.
- Prompt versioning.
- Cost and usage visibility.
- Debugging multi-step workflows.

### Best phases

- Phase 9.

### Watch for

- A trace only helps if you use it to understand a decision, not just to collect more data.

## LangSmith

LangSmith is a platform for evaluation, prompt testing, and experiment comparison.

### What it teaches

LangSmith teaches dataset-driven evaluation and experiment comparison. It is useful for learning how to record system versions and compare prompt or workflow changes systematically.

### Core topics and subtopics

- Datasets for repeatable evaluation.
- Run comparison and experiment tracking.
- Prompt testing and workflow inspection.
- Regression detection.

### Best phases

- Phase 9.

### Watch for

- Comparing runs is only meaningful if the dataset reflects the real job the system must do.

## RAGAS

RAGAS is a library for scoring retrieval-augmented generation systems.

### What it teaches

RAGAS teaches task-specific RAG evaluation. It is especially helpful for separating retrieval quality from answer quality.

Quick meanings for the metrics below:

- `faithfulness` asks whether the answer stays supported by the evidence
- `context precision` asks whether the retrieved text is mostly useful
- `context recall` asks whether the system found the important evidence

### Core topics and subtopics

- Faithfulness.
- Answer relevance.
- Context precision and recall.
- Metric-based comparison of retrieval systems.

### Best phases

- Phase 9.
- Useful in Phase 5 once you already have a working RAG pipeline.

### Watch for

- Retrieval metrics and answer quality are related, but they are not the same thing.

## Companion Guides

- [../courses/evals-and-mlops-courses.md](../courses/evals-and-mlops-courses.md)
- [retrieval-data-tools.md](./retrieval-data-tools.md)
- [../books/ml-foundations-and-thinking.md](../books/ml-foundations-and-thinking.md)

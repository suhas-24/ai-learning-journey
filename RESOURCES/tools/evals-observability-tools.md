# Evals And Observability Tools

This guide covers the tools that teach how to see inside an LLM system, compare versions, and measure whether changes are actually improving quality.

## Langfuse

### What it teaches

Langfuse teaches trace-based visibility. It helps you inspect prompt versions, request paths, costs, and failures across a workflow instead of staring at one final answer.

### Major topics and subtopics

- End-to-end traces.
- Prompt versioning.
- Cost and usage visibility.
- Debugging multi-step workflows.

### Best phases

- Phase 9.

## LangSmith

### What it teaches

LangSmith teaches dataset-driven evaluation and experiment comparison. It is useful for learning how to record system versions and compare prompt or chain changes systematically.

### Major topics and subtopics

- Datasets for repeatable evaluation.
- Run comparison and experiment tracking.
- Prompt testing and workflow inspection.
- Regression detection.

### Best phases

- Phase 9.

## RAGAS

### What it teaches

RAGAS teaches task-specific RAG evaluation. It is especially helpful for separating retrieval quality from answer quality.

### Major topics and subtopics

- Faithfulness.
- Answer relevance.
- Context precision and recall.
- Metric-based comparison of retrieval systems.

### Best phases

- Phase 9.
- Useful in Phase 5 once you already have a working RAG pipeline.

## Companion Guides

- [../courses/evals-and-mlops-courses.md](../courses/evals-and-mlops-courses.md)
- [retrieval-data-tools.md](./retrieval-data-tools.md)
- [../books/ml-foundations-and-thinking.md](../books/ml-foundations-and-thinking.md)

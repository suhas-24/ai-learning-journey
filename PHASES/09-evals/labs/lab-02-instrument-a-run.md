# Lab 02 - Instrument a Run

This lab teaches the minimum observability layer for a multi-step workflow.

## Scenario

You have a run with these nodes:

- retrieve_docs
- summarize
- validate_answer
- approval_gate

## Task 1: define required fields

For each node event, record:

- run id
- node
- start and end time
- token usage, meaning how many small pieces of text the model read or wrote
- model or tool name
- validator result if any
- next action

## Task 2: choose dashboard signals

Pick five signals and define their warning thresholds.

Example:

| Signal | Threshold |
| --- | --- |
| P95 latency | warn above 8s |
| Dead-letter rate | warn above 2% |
| Cost per run | warn above $1.20 |

## Task 3: simulate a regression

Invent a failure such as:

- schema validator suddenly fails on 15% of runs
- retrieval precision falls after index changes

Write how the trace data would reveal it.

## Stretch task

Describe which of your signals should block a merge and which should only trigger investigation.

Use [Observability, Traces, and Runtime Signals](../chapters/03-observability-traces-and-runtime-signals.md) for examples.

# Lab 1 - Baseline Versus Tuned Model

This lab teaches the core discipline of the phase: never judge a tuned model in isolation.

## Goal

Build a prompt-only baseline for a narrow classification task, then compare it with a tuned model using the same held-out set.

## Lab Setup

Pick one task:

- support ticket routing
- contract clause classification
- issue triage
- structured summary type prediction

Keep the label set below 8 classes for the first run.

## Steps

### 1. Define The Task

Write:

- input shape
- output schema
- label policy
- business metric

### 2. Build The Baseline

Create a simple prompt:

```text
You are a routing assistant.
Classify each ticket into exactly one label:
- billing
- product_bug
- account_access
- feature_request
- other

Return JSON with keys label and reason.
```

Run it on 30 to 50 held-out examples and log the outputs.

### 3. Prepare Train And Validation Data

Use the JSONL style shown in [snippets/support-routing-train.jsonl](../snippets/support-routing-train.jsonl). Keep the test set separate.

### 4. Run A Small Tuning Job

You can use a managed provider workflow or an open-source PEFT stack. Keep the first run intentionally small.

### 5. Compare Results

Record:

- accuracy or macro F1
- schema validity
- cost
- inference latency
- recurring error types

### 6. Write A Decision Memo

Answer:

- Did the tuned model improve enough to matter?
- Which failures remain?
- Would better prompts or more data likely help more than another training run?

## Deliverable

One markdown note with:

- task definition
- baseline prompt
- dataset size and split
- score table
- recommendation

## Reflection Questions

- Did the tuned model improve the exact failure mode you targeted?
- Did it introduce any new failures?
- If you only had one more day, would you collect better data or run another training job?

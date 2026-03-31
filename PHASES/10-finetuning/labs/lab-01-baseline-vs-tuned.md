# Lab 1 - Baseline Versus Tuned Model

This lab teaches the main discipline of the phase: never judge a tuned model by itself.

Before we begin, one simple definition:

- a `baseline` is the simplest version you compare against

## Goal

Build a prompt-only baseline for one narrow classification task, then compare it with a tuned model on the same held-out examples.

## Pick One Task

Choose one task:

- support ticket routing
- contract clause classification
- issue triage
- structured summary type prediction

Keep the label set small for the first run.

## Steps

### 1. Define The Task

Write:

- what comes in
- what comes out
- what each label means
- why the task matters

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

Run it on 30 to 50 held-out examples and save the outputs.

### 3. Prepare Train And Validation Data

Use the JSONL style shown in [snippets/support-routing-train.jsonl](../snippets/support-routing-train.jsonl).
Keep the test set separate.

### 4. Run A Small Tuning Job

Use either a managed provider workflow or an open-source LoRA setup.
Keep the first run small so mistakes are cheap.

### 5. Compare Results

Record:

- accuracy or macro F1
- schema validity
- cost
- latency
- recurring error types

### 6. Write A Decision Memo

Answer:

- Did the tuned model improve enough to matter?
- Which failures remain?
- Would better prompts or better data help more?

The goal is to make a fair comparison, not to chase the fanciest training setup.

## Deliverable

One markdown note with:

- task definition
- baseline prompt
- dataset size and split
- score table
- recommendation

## Reflection Questions

- Did the tuned model improve the exact problem you targeted?
- Did it introduce any new problems?
- If you had one more day, would you collect better data or run another training job?

# Lab 01 - Design an Orchestrator

This lab takes you from a vague agent idea to a concrete execution graph.

An `orchestrator` is the part that decides which step happens next. A `graph` is a map of boxes and arrows that shows the allowed next steps.

If those words are new, that is okay:

- `orchestrator` means the control layer that chooses the next step
- a `graph` is a picture of allowed next steps
- a `node` is one box in that picture
- `state` is the memory the workflow carries forward
- a `checkpoint` is a safe place to resume from later

## Goal

Design a small orchestrator for this task:

> Read a product launch brief, gather supporting evidence from notes, draft a launch summary, and require approval before publication.

## Step 1: define nodes

Write down at least five nodes. A strong answer usually includes:

- intake
- retrieval
- synthesis
- validation
- approval
- publish or stop

A `node` is one box in the workflow. It should do one clear job.

## Step 2: define state

Create a state shape with:

- current node
- completed nodes
- artifact paths
- retry counters
- approval status
- budget state

`State` is the memory the workflow needs to keep going after a pause or crash.

Use [State Schema](../snippets/state-schema.md) as a template.

## Step 3: draw transitions

Create a small graph:

```text
intake -> retrieval -> synthesis -> validation -> approval -> publish
                             \-> retry validation -> dead_letter
```

## Step 4: add stop conditions

Document when the run should stop immediately:

- budget exceeded
- approval denied
- repeated schema failure
- required source count not met

## Step 5: answer the reflection questions

1. Which node is most expensive?
2. Which node is most likely to fail?
3. Where should the latest checkpoint live?
4. Which node needs idempotency protection?

## Deliverable

Produce a one-page design note with:

- node list
- state schema
- transition map
- three failure rules

Check yourself against [Checkpoints](../checkpoints.md).

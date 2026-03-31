# Lab 01 - Design an Orchestrator

This lab takes you from a vague agent idea to a concrete execution graph.

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

## Step 2: define state

Create a state shape with:

- current node
- completed nodes
- artifact paths
- retry counters
- approval status
- budget state

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

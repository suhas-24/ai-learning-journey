# Phase 07 - Orchestration and Harness Engineering

This phase teaches how to turn one model call into a dependable workflow.

Before we go further, here are the core words in plain language:

- a `workflow` is a sequence of steps that work toward one goal
- a `node` is one step in that workflow
- `orchestration` means deciding what happens next
- a `harness` is the system around the model that keeps work organized, safe, and observable
- `state` is the information the system remembers while it works
- a `checkpoint` is a saved point that lets the system continue later
- a `budget` is a limit on time, money, or effort
- an `approval gate` is a point where a person must say yes before the system continues

If those words are new, that is normal. We start with ordinary ideas like step order, memory, and recovery, then name the technical version after the idea is clear.

## What This Phase Is Really About

The main lesson is simple: a model can suggest the next move, but a larger system must decide whether that move should happen, how much it may cost, and what to do if something breaks.

If you can explain the workflow in terms of steps, memory, retries, and stops, you already understand the heart of orchestration.

## What You Will Learn

- what orchestration means in everyday language
- why a workflow needs a controller instead of only a model
- when a task needs a loop, a pipeline, a graph, a queue, or multiple agents
- how to model durable state instead of hiding everything inside chat history
- where retries, budgets, approvals, and logs belong in a production harness
- how to reason about failure paths before they happen in production

## How To Use This Phase

1. Read the chapters in order.
2. Use the snippets as examples of shape and structure.
3. Work through the labs with a small task you understand.
4. Use the checkpoints to explain the ideas in plain words.
5. Use troubleshooting when the system feels confusing or brittle.

## Module Map

1. [Control Flow and Topologies](./chapters/01-control-flow-and-topologies.md)
2. [State, Checkpoints, and Resumability](./chapters/02-state-checkpoints-and-resumability.md)
3. [Harness Components and Runtime Policies](./chapters/03-harness-components-and-runtime-policies.md)
4. [Failure Walkthroughs](./chapters/04-failure-walkthroughs.md)
5. [Labs](./labs/lab-01-design-an-orchestrator.md)
6. [Checkpoints](./checkpoints.md)
7. [Troubleshooting](./troubleshooting.md)

Use the supporting snippets while you read:

- [State Schema](./snippets/state-schema.md)
- [Runtime Commands](./snippets/runtime-commands.md)

## Completion Standard

You are done with this phase when you can design a small orchestrated system, explain its state transitions, and walk through how it behaves under timeout, bad tool output, budget pressure, and human approval.

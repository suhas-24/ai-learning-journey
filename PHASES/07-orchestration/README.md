# Phase 07 - Orchestration and Harness Engineering

This module teaches how to turn a simple model call into a dependable workflow.

A `model` is the part that generates text or chooses an action. An `orchestration harness` is everything around it that decides what happens next, keeps track of progress, enforces limits, and handles failure. If the model is the worker, the harness is the supervisor, clipboard, and safety rail.

This module stays on the plain-language side on purpose. We start with simple ideas like "what happens next" and "what should happen if something fails," then build toward control flow, checkpoints, approvals, and recovery.

Start here, then move in order:

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

## What you will learn

- what orchestration means in everyday language
- why a workflow needs a controller instead of only a model
- when a task needs a loop, a graph, a queue, or multiple agents
- how to model durable state instead of hiding everything inside chat history
- where retries, budgets, approvals, and logs belong in a production harness
- how to reason about failure paths before they happen in production

## Completion standard

You are done with this phase when you can design a small orchestrated system, explain its state transitions, and walk through how it behaves under timeout, bad tool output, budget pressure, and human approval.

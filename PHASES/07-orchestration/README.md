# Phase 07 - Orchestration and Harness Engineering

This module teaches how to turn a prompt-driven prototype into a durable system with explicit control flow, persistent state, failure handling, and operator visibility.

Start here, then move in order:

1. [Control Flow and Topologies](./chapters/01-control-flow-and-topologies.md)
2. [State, Checkpoints, and Resumability](./chapters/02-state-checkpoints-and-resumability.md)
3. [Harness Components and Runtime Policies](./chapters/03-harness-components-and-runtime-policies.md)
4. [Failure Walkthroughs](./chapters/04-failure-walkthroughs.md)
5. [Labs](./labs/01-design-an-orchestrator.md)
6. [Checkpoints](./checkpoints.md)
7. [Troubleshooting](./troubleshooting.md)

Use the supporting snippets while you read:

- [State Schema](./snippets/state-schema.md)
- [Runtime Commands](./snippets/runtime-commands.md)

## What you will learn

- when a task needs a loop, a graph, a queue, or multiple agents
- how to model durable state instead of hiding everything inside chat history
- where retries, budgets, approvals, and logs belong in a production harness
- how to reason about failure paths before they happen in production

## Completion standard

You are done with this phase when you can design a small orchestrated system, explain its state transitions, and walk through how it behaves under timeout, bad tool output, budget pressure, and human approval.

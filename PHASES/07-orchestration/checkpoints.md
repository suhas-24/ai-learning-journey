# Checkpoints

Use this list to verify actual understanding, not just familiarity.

## Knowledge checks

- I can explain the difference between a single loop, a pipeline, and a graph.
- I can name which data belongs in orchestration state and which does not.
- I can explain why checkpoints and idempotency are different.
- I can define at least one dead-letter condition.

## Design checks

- I can design a node graph for a real task in under 20 minutes.
- I can specify retry and do-not-retry rules with reasons.
- I can place approval gates only at irreversible or high-risk boundaries.
- I can explain what should happen after a process crash.

## Failure checks

- I can walk through a budget spiral and show how to stop it.
- I can walk through a crash after approval without creating duplicate side effects.
- I can walk through tool schema drift and show where validation belongs.

If any item feels fuzzy, revisit [Failure Walkthroughs](./chapters/04-failure-walkthroughs.md) and [Lab 02](./labs/lab-02-add-retries-budgets-and-approvals.md).

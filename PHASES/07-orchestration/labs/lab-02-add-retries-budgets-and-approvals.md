# Lab 02 - Add Retries, Budgets, and Approvals

This lab upgrades a fragile orchestrator into a safer runtime.

`Retry` means trying again after a temporary failure. `Approval` means a person must say yes before a risky step happens.

If those ideas are new, think of them like this:

- `retry` is a second chance after a temporary problem
- a `budget` is a cap on cost, time, or effort
- an `approval` is a human pause before a risky action

## Starting point

Assume you already have these nodes:

```yaml
nodes:
  - retrieve
  - draft
  - validate
  - send_email
```

## Task 1: add a retry table

Fill in a table like this:

| Error | Retry? | Why |
| --- | --- | --- |
| HTTP 429 | yes | transient provider pressure |
| schema validation failed | no | design bug or incompatible payload |
| timeout during retrieval | yes | often transient |
| approval denied | no | policy decision |

`Transient` means "temporary and likely to go away on its own."

## Task 2: define a budget policy

Set explicit limits:

```yaml
budget:
  max_usd: 1.00
  max_runtime_seconds: 90
  max_search_calls: 4
  downgrade_model_when_remaining_budget_below: 0.25
```

Explain what the runtime does when each limit is reached.

## Task 3: gate the email step

Write approval criteria for `send_email`:

- who can approve
- how long approval stays valid
- what audit fields must be stored
- how duplicate sends are prevented

Treat email like a real-world action, because it is. Once it leaves the system, you cannot pretend it never happened.

## Task 4: design the dead-letter record

Include:

- run id
- last safe checkpoint
- failing node
- error signature
- suggested operator action

## Stretch task

Add a rule that prevents more than one model escalation per run.

When finished, compare your design to the examples in [Harness Components and Runtime Policies](../chapters/03-harness-components-and-runtime-policies.md).

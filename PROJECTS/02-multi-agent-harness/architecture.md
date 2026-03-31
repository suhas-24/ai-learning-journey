# Architecture - Multi-Agent Research Harness

This page explains how the harness is built and why each piece exists.

## Key Words

- `state` is the shared record of what the run knows so far
- a `handoff` means one role passes work to the next role
- an `approval gate` means a human must review before a risky step continues
- `observability` means the ability to inspect what happened during a run

## System Shape

```text
task intake -> planner/state initializer -> Researcher -> Analyst -> Reporter -> approval gate -> final artifact
                           |                    |            |            |
                           +---- persistence ---+---- traces +---- audit -+
```

## Component Guide

### 1. Task State

Task state is the notebook the harness carries from step to step.

It usually stores:

- task id
- user goal
- current stage
- evidence list
- pending questions
- approval status
- budget or timeout counters

Why it exists:

- the run needs memory if it is going to continue after interruptions

### 2. Agent Roles

Each role has a job description.

- `Researcher` gathers sources and records where they came from
- `Analyst` checks whether the evidence is strong enough
- `Reporter` turns the collected work into the final artifact

Why it exists:

- role separation makes the system easier to inspect and debug

### 3. Tooling Layer

The tools layer is the set of actions each role is allowed to use.

Possible tools include:

- search
- file system access
- GitHub
- structured document parsing

Why it exists:

- the harness should control tool access, not only the prompt text

### 4. Persistence And Recovery

Persistence means saving the run so it can continue later.

Persist:

- state snapshots
- run events
- partial artifacts
- approval requests

Why it exists:

- without persistence, a restart destroys the work

### 5. Policy Layer

The policy layer sets the guardrails.

It enforces:

- max iterations
- budget caps
- timeout boundaries
- disallowed actions
- approval requirements

Why it exists:

- the system should stay bounded even when the task is messy

### 6. Observability

Observability means the run leaves a trail you can inspect.

Log:

- step start and end
- tool invocations
- retries
- approvals
- terminal status

Why it exists:

- if a run fails, you need evidence to explain why

## Decisions To Document

- why each role exists
- what state is shared across roles
- what is intentionally isolated
- how loops are prevented
- how the system pauses and resumes safely

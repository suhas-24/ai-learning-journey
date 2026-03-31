# Architecture - Multi-Agent Research Harness

Before the diagram, here are the important terms:

- state is the shared record of what the run knows so far
- handoff means one role passes work to the next role
- approval gate means a human must review before a risky step continues
- observability means the ability to inspect what happened during a run

## System Overview

```text
task intake -> planner/state initializer -> Researcher -> Analyst -> Reporter -> approval gate -> final artifact
                           |                    |            |            |
                           +---- persistence ---+---- traces +---- audit -+
```

## Core Components

### 1. Task State

Store a structured state object containing:

- task id
- user goal
- current stage
- evidence list
- pending questions
- approval status
- budget or timeout counters

If the Python type syntax looks unfamiliar, treat it as a labeled note about what information the run keeps. A `TypedDict` is just a dictionary shape with named fields.

Suggested interface:

```python
class TaskState(TypedDict):
    task_id: str
    goal: str
    stage: str
    evidence: list[dict]
    decisions: list[dict]
    approval_required: bool
```

### 2. Agent Roles

Researcher:

- queries tools
- gathers sources
- records confidence and provenance

Analyst:

- inspects evidence quality
- requests more research when gaps remain
- identifies contradictions

Reporter:

- formats the output
- summarizes decisions and assumptions
- prepares the artifact for approval

### 3. Tooling Layer

Possible tools:

- search
- file system
- GitHub
- structured document parsing

The harness, not the agent prompt alone, should decide which tools are available per role.

### 4. Persistence And Recovery

Persist:

- state snapshots
- run events
- partial artifacts
- approval requests

This is what makes the system resumable.

If state feels abstract, think of it as the notebook the harness carries from step to step.

### 5. Policy Layer

The policy layer enforces:

- max iterations
- budget caps
- timeout boundaries
- disallowed actions
- approval requirements

### 6. Observability

Log:

- agent step start and end
- tool invocations
- retries
- approvals
- terminal run status

## Architecture Decisions To Document

- why each role exists
- what state is shared across roles
- what is intentionally isolated
- how you prevent endless loops
- how you pause or resume safely

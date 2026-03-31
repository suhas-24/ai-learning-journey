# Architecture - Multi-Agent Research Harness

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

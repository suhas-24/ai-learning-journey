# Build Plan - Multi-Agent Research Harness

This build plan starts small on purpose: first one worker with memory, then more roles, then safety and visibility.

## Milestone 1 - Single-Agent Baseline

Deliverables:

- one stateful worker
- persisted state store
- simple task intake

Definition of done:

- a run can survive a process restart

## Milestone 2 - Role Split

Deliverables:

- Researcher role
- Analyst role
- Reporter role
- handoff contract between roles

Definition of done:

- each role has a clear responsibility and output artifact

## Milestone 3 - Controls

Deliverables:

- approval gate
- timeout budget
- retry policy
- stop conditions

Definition of done:

- unsafe or irreversible actions cannot happen without review

## Milestone 4 - Observability

Deliverables:

- traces
- structured logs
- run summary report

Definition of done:

- you can debug a failed run after it finishes

## Milestone 5 - Scenario Evaluation

Deliverables:

- scenario catalog
- pass or fail results
- intervention notes
- improvement backlog

Definition of done:

- the harness is evaluated on repeatable tasks, not anecdotes

## Milestone 6 - Packaging

Deliverables:

- polished README
- architecture writeup
- demo showing pause, resume, and approval

Definition of done:

- another engineer can understand both the autonomy and the constraints

# Build Plan - Multi-Agent Research Harness

This plan starts with one worker and slowly adds control.

Quick meanings:

- a `stateful worker` is a worker that remembers what happened earlier in the run
- a `persisted state store` is the saved location where that memory lives
- a `handoff contract` is the clear agreement about what one role passes to the next role
- a `timeout budget` is the maximum time you allow a step to use
- `structured logs` are logs written in a consistent field-based format so they are easier to search later
- an `artifact` is any saved output you can inspect, such as a report, trace, or summary file

The point is to prove that the harness stays understandable while it becomes more capable.

## Milestone 1 - Single-Agent Baseline

Deliverables:

- one stateful worker
- persisted state store
- simple task intake

Why this step exists:

- you need a working memory before you split the work into roles

Definition of done:

- a run can survive a process restart

## Milestone 2 - Role Split

Deliverables:

- `Researcher` role
- `Analyst` role
- `Reporter` role
- handoff contract between roles

Why this step exists:

- each role should have one clear job

Definition of done:

- each role has a clear responsibility and output artifact

## Milestone 3 - Controls

Deliverables:

- approval gate
- timeout budget
- retry policy
- stop conditions

Why this step exists:

- autonomy should have a ceiling

Definition of done:

- unsafe or irreversible actions cannot happen without review

## Milestone 4 - Observability

Deliverables:

- traces
- structured logs
- run summary report

Why this step exists:

- a failed run should still teach you something

Definition of done:

- you can debug a failed run after it finishes

## Milestone 5 - Scenario Evaluation

Deliverables:

- scenario catalog
- pass or fail results
- intervention notes
- improvement backlog

Why this step exists:

- the harness should be tested on repeatable tasks, not anecdotes

Definition of done:

- the system is evaluated on scenarios you can run again later

## Milestone 6 - Packaging

Deliverables:

- polished README
- architecture writeup
- demo showing pause, resume, and approval

Why this step exists:

- another engineer should be able to understand the system quickly

Definition of done:

- the project is easy to explain and easy to inspect

# Project 2 - Multi-Agent Research Harness

This project teaches how to coordinate multiple agents safely.

If those words are new:

- an `agent` is a program that can take steps toward a goal
- a `harness` is the system around the agents that keeps them organized and inspectable
- `state` is the information the system remembers while it is working
- `checkpointing` means saving progress so a run can continue later
- an `approval gate` is a human pause before a risky action continues
- `observability` means you can see what the system did
- `traceability` means you can connect each step back to the run that produced it
- a `trace` is the step-by-step record of that run

The main idea is simple: many agents are useful only if the system around them is disciplined. Think of the harness as the control room around a team, not the team itself.

## What You Will Build

You will build a research workflow that can:

- keep state across steps
- hand work from one role to another
- pause safely when approval is needed
- resume after interruption
- show traces and logs for debugging

## Why This Project Matters

This is not about making the biggest swarm.

It is about showing that you can:

- control a multi-step system
- make handoffs visible
- recover from failure
- explain what happened after the run

## Core Roles

- `Researcher`: gathers evidence and records sources
- `Analyst`: checks quality, gaps, and contradictions
- `Reporter`: packages the findings for the final output

If the word `swarm` is new, it just means many agents working together. Bigger is not better unless the handoffs, memory, and safety rules stay clear.

## How To Use This Folder

- `README.md` explains the project in plain language
- `architecture.md` shows the moving parts
- `build-plan.md` gives the order of work
- `eval-plan.md` shows how to test reliability
- `rubric.md` checks whether the project is actually controlled

## Suggested Repo Layout

```text
02-multi-agent-harness/
├── README.md
├── architecture.md
├── build-plan.md
├── eval-plan.md
└── rubric.md
```

When implemented as code, the project often looks like this:

```text
src/
  agents/
  state/
  tools/
  policies/
  observability/
tests/
reports/
```

## Milestones

1. Build one stateful worker first.
2. Split the work into Researcher, Analyst, and Reporter.
3. Add checkpointing and resume support.
4. Add approval gates and stop conditions.
5. Add traces, logs, and run reports.
6. Test scenarios and package the result.

## Required Artifacts

- task state schema
- run event log
- approval policy
- trace examples
- scenario-based eval report

Here, a `task state schema` is the simple field list for what the system needs to remember, such as current step, evidence collected, and approval status.

## Success Looks Like

A strong version of this project should prove that:

- the harness can pause and resume safely
- handoffs are visible
- risky actions are gated
- failures can be debugged after the run

## Demo Guidance

Show:

- a multi-step task
- one pause/resume cycle
- one approval request
- one trace or event log
- one failure path and recovery behavior

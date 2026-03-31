# Project 2 - Multi-Agent Research Harness

Build a stateful research harness with multiple agent roles, explicit handoffs, checkpointing, approval gates, and observability. The project is about reliability and control, not agent count for its own sake.

An agent is a program that can take steps toward a goal by using tools or making decisions in stages. A harness is the system around the agents that keeps them organized, safe, and inspectable. Checkpointing means saving progress so the run can continue later instead of starting over. Observability means being able to see what happened during a run. Traceability means being able to connect each step back to the run that produced it. Approval gates are pauses where a human must approve a risky action before it continues.

## Project Goal

Demonstrate that you can design bounded autonomy around a multi-step task that survives interruptions, exposes traceability, and asks for human approval before risky actions.

In plain English, the system should keep working even when things go wrong, and it should always be able to explain what it did.

## Core Roles

- Researcher: gathers evidence and records sources
- Analyst: checks quality, gaps, and contradictions
- Reporter: packages findings and prepares the final artifact

## Recommended Folder Layout

```text
02-multi-agent-harness/
├── README.md
├── architecture.md
├── build-plan.md
├── eval-plan.md
└── rubric.md
```

When implemented as a code repo, target:

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

1. Single-agent baseline with persistent state
2. Split roles into Researcher, Analyst, Reporter
3. Add checkpointing and resume
4. Add approval gates and stop conditions
5. Add traces, logs, and run reports
6. Run eval scenarios and publish a demo

## Required Artifacts

- task state schema
- run event log
- approval policy
- trace screenshots or examples
- scenario-based eval report

## Success Criteria

- the harness can pause and resume safely
- agent handoffs are inspectable
- risky actions are gated
- failures are debuggable after the run

## Demo Guidance

Show:

- a multi-step task
- one pause/resume cycle
- one approval request
- one trace view or event log
- one failure path and recovery behavior

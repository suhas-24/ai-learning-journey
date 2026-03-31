# Project 3 - Enterprise Workflow Agent

This project teaches how to build a narrow business workflow with safety, visibility, and careful deployment.

If those words are new:

- a `workflow` is a repeatable sequence of steps that turns input into output
- `intake` is the part that accepts the request
- `policy` is the rule set that decides what the system is allowed to do
- `telemetry` is the system data that helps people watching the system understand behavior
- an `audit trail` is a record of important actions and decisions
- `schema validation` checks that data has the shape you expect
- `monitoring` means watching the system over time so problems are noticed quickly
- `bounded` means intentionally limited to a narrow job
- an `operator` is the person responsible for watching, checking, or running the system

The point of this project is not to make an “AI does everything” assistant.
It is to make a bounded system that can do one job well, explain itself, and stop when a human needs to step in.

## What You Will Build

You will build a workflow agent that can:

- accept a narrow business request
- validate the request
- execute a bounded action plan
- ask for approval when needed
- record logs and audit data
- show how it would be deployed and monitored

## Why This Project Matters

This project shows that you can build something useful without pretending it is magic.

It demonstrates:

- clear scope
- safe decision making
- operator visibility
- deployment thinking

## Suitable Use Cases

- support workflow triage
- document intake and classification
- policy-compliant research summaries
- internal operations assistance for a bounded process

## How To Use This Folder

- `README.md` explains the project in plain language
- `architecture.md` shows how the system is organized
- `build-plan.md` gives the order of work
- `eval-plan.md` shows how to test safety and reliability
- `rubric.md` checks whether the project is production-minded

## Suggested Repo Layout

```text
03-enterprise-agent/
├── README.md
├── architecture.md
├── build-plan.md
├── eval-plan.md
└── rubric.md
```

When implemented as code, a clean layout often looks like this:

```text
app/
src/
  agent/
  policies/
  tools/
  telemetry/
  auth/
infra/
tests/
reports/
```

## Milestones

1. Pick one narrow workflow with real business rules.
2. Build task intake, status visibility, and agent execution.
3. Add schema validation, approval gates, and audit logging.
4. Add deployment, secrets handling, and monitoring.
5. Evaluate safety, reliability, and usability.
6. Produce a portfolio-grade demo and retrospective.

## Required Artifacts

- use-case boundary statement
- policy and escalation rules
- system architecture
- deployment checklist
- metrics report
- retrospective

Here, an `artifact` means a saved item another person can inspect, such as a checklist, report, README, or demo.

## Success Looks Like

A strong version of this project should prove that:

- the agent solves a bounded task well
- risky actions are controlled
- behavior is observable, which means another person can see what the system did
- the README clearly states both capability and limits

## Demo Guidance

Show:

- a real workflow request
- validation and approval behavior
- task status visibility
- one metric dashboard or report
- one limitation or escalation path

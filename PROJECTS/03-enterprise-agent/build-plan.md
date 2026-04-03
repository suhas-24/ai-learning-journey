# Build Plan - Enterprise Workflow Agent

This plan begins with scope because a safe workflow agent is only useful if everyone agrees on what it is allowed to do.

Two terms to pin down before the milestones:

- a `boundary statement` is a short note explaining what the system will do and what it will refuse to do
- a `risk register` is a list of important risks and how you plan to reduce them

Quick meanings:

- a `request schema` is the expected shape of the incoming request
- a `status model` is the small set of labels that describe where a task currently is
- `schema validation` checks that the request or output matches the expected shape
- an `audit log` is the written record of key actions and approvals
- a `rubric` is a scoring guide used to judge quality consistently

If `boundary statement` feels abstract, read it as the promise line for the project: what the system will do, and what it will never do.

## Milestone 1 - Workflow Definition

Deliverables:

- workflow map
- success criteria
- boundary statement
- risk register

Why this step exists:

- the team needs to agree on the problem before building the solution

Definition of done:

- the team can explain exactly what the agent will and will not do

## Milestone 2 - Intake And Core Agent Flow

Deliverables:

- request schema
- status model
- agent execution path
- initial UI or API

Why this step exists:

- a request needs a clear path from intake to action

Definition of done:

- a request can move from intake to proposed action with visible state

## Milestone 3 - Safety And Governance

Deliverables:

- approval rules
- schema validation
- audit log
- escalation path

Why this step exists:

- risky work needs a clear review process

Definition of done:

- high-risk actions cannot bypass policy

## Milestone 4 - Deployment And Observability

Deliverables:

- deployment config
- environment and secrets guide
- logs, traces, or dashboards
- rollback checklist

Why this step exists:

- a good system should be runnable and operable

Definition of done:

- another engineer can deploy and monitor the system

## Milestone 5 - Evaluation

Deliverables:

- scenario test set
- operator review rubric
- metric summary
- lessons learned report

Why this step exists:

- safety and reliability should be proved, not assumed

Definition of done:

- claims about reliability and safety are backed by evidence

## Milestone 6 - Portfolio Packaging

Deliverables:

- public-friendly README
- architecture note
- demo
- retrospective

Why this step exists:

- the project should read like a serious production-minded system

Definition of done:

- the project is easy to explain and honest about its limits

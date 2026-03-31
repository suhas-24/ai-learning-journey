# Project 3 - Enterprise Workflow Agent

Build a production-minded workflow agent for a narrow business process, with clear boundaries, safety checks, observability, and deployment documentation. This project should show that you know how to make an AI system useful without pretending it can do everything safely.

## Project Goal

Demonstrate end-to-end thinking across:

- task intake
- agent execution
- safety controls
- deployment
- monitoring
- human oversight

## Suitable Use Cases

- support workflow triage
- document intake and classification
- policy-compliant research summaries
- internal operations assistant for a bounded process

## Recommended Folder Layout

```text
03-enterprise-agent/
├── README.md
├── architecture.md
├── build-plan.md
├── eval-plan.md
└── rubric.md
```

When implemented as a code repo, target:

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
- postmortem or retrospective

## Success Criteria

- the agent solves a bounded task well
- risky actions are controlled
- system behavior is observable
- the README communicates both capability and limits clearly

## Demo Guidance

Show:

- a real workflow request
- validation and approval behavior
- task status visibility
- one metric dashboard or report
- one limitation or escalation path

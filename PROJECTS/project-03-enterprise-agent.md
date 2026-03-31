# Project 3 - Enterprise Workflow Agent (Public Deployment)

**Phase:** Phase 8-9  
**Status:** 🔴 Not Started  
**Started:** Not started yet  
**Completed:** Not completed yet

---

## Problem Statement

Build a publicly deployed workflow agent with real safety controls, real metrics, and a real use case. This project should demonstrate that I can think beyond demos and account for production boundaries such as governance, observability, deployment, and user trust.

---

## What This Project Teaches

- how to move from a prototype to a public system
- how to gate risky actions with governance
- how to design for monitoring, rollback, and safety
- how to communicate limitations honestly to users
- how to ship something useful without overclaiming autonomy

---

## Candidate Use Cases

- support or FAQ assistant with policy enforcement
- internal operations assistant for structured workflows
- research summarizer with approval before publishing
- document triage or classification assistant

The use case should be narrow enough to control risk and broad enough to show production judgment.

---

## Planned System Design

### Application Layer

- user-facing interface or API
- task intake and status visibility
- clear feedback about what the agent is doing and why

### Agent Layer

- model-based reasoning with tool access
- structured outputs and validation
- limited scope of autonomy
- task-specific prompts and schemas instead of one giant prompt blob

### Safety Layer

- guardrails
- approval gates
- sandboxing where code execution is possible
- audit log for every significant action
- explicit rules for when the system must stop and ask for help

### Operations Layer

- Docker deployment
- observability dashboard
- cost tracking
- rollback or disable path
- simple deployment documentation that another person could follow

---

## Real Usage Metrics To Track

| Metric | Why it matters |
| --- | --- |
| Users | proves this is not a fake internal benchmark |
| Tasks completed | shows usage volume |
| Success rate | measures reliability |
| Avg cost per task | keeps the system economically honest |
| Human interventions | shows where autonomy still breaks down |
| Latency | affects user trust and usability |

---

## Deployment Checklist

- clear use-case boundary
- secrets handled safely
- audit log enabled
- approval rules defined
- observability connected
- one rollback plan tested
- public README with limitations and safety notes
- a repeatable setup process
- a way to inspect failed runs after deployment
- a defined owner for the system if it is public or semi-public

---

## Main Risks

- choosing a use case too broad to govern safely
- shipping without enough monitoring
- measuring only throughput and not quality
- over-promising autonomy in public
- confusing internal demo success with real production readiness
- exposing users to uncertain behavior without clear guardrails

---

## What "Done" Looks Like

- deployed system with real external access or real internal users
- tracked metrics over time
- documented safety model
- visible postmortem or retrospective after real usage
- portfolio-quality README and demo
- clear explanation of what the system will not do

---

## Links

- **Planned GitHub repo:** to be created during Phases 8-9
- **Live deployment goal:** public URL or internal demo environment with recorded walkthrough
- **Writeup goal:** deployment lessons, safety decisions, and operational metrics

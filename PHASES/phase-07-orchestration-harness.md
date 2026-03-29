# Phase 7 - Agent Orchestration + Harness Engineering

**Status:** 🔴 Not Started  
**Started:** Not started yet  
**Completed:** Not completed yet  
**Estimated Duration:** 6-8 weeks

---

## Why This Phase Matters

This is the phase where toy agents stop being enough. One model calling tools in a loop is fragile for long tasks, hard to debug, and expensive to operate. Orchestration introduces state and control flow. Harness engineering introduces the surrounding system that makes agents resilient.

The harness is the difference between a flashy demo and a durable product.

---

## Core Ideas To Master

### Orchestration Frameworks

- LangGraph for stateful graphs and persistence
- CrewAI for role-based teams and delegation
- PydanticAI for type-safe structured flows
- OpenAI Agents SDK for handoffs, tracing, and validation patterns

### Harness Components

- planning before acting
- reflection or critic loops
- retry and timeout rules
- rollback or reversibility for risky actions
- cost and latency governors
- state persistence and checkpointing
- human approval gates
- immutable audit logs

### Design Patterns

- single agent plus tools
- orchestrator with sub-agents
- parallel workers
- sequential crews
- debate pattern
- map-reduce fan-out and consolidation

---

## What I Need To Internalize

- the model is only one component in the system
- long-running tasks need explicit state and failure handling
- cost discipline must be designed, not wished into existence
- reflection is useful only when scored against a clear rubric
- human oversight should appear at the right irreversible boundaries

---

## Phase Project: Persistent Research + Execution Agent

**Project goal:** build a stateful multi-agent system that can survive longer tasks, recover from failure, and ask for approval at the right moments.  
**Planned repo:** dedicated Phase 7 repository  
**Current project status:** planned, not started

### Planned architecture

- Researcher agent gathers inputs
- Analyst agent synthesizes and critiques
- Reporter agent produces final output
- LangGraph manages state, transitions, and checkpoints
- cost governor limits total spend
- approval gate blocks irreversible output changes

### Harness features that must exist

- checkpoint state every few steps
- retry transient tool failures
- stop on budget overrun
- emit structured logs
- support resume after crash or interruption

---

## Exit Criteria

- I can explain the difference between orchestration and harnessing.
- I can choose a framework based on constraints, not brand familiarity.
- I can build a persistent state model for a multi-step task.
- I can insert human approval where it actually matters.
- I can describe the full path of an agent failure and how the harness should react.

---

## Common Traps To Avoid

- adding more agents when one agent is still poorly designed
- confusing branching logic with true reliability
- building reflection loops without clear scoring criteria
- ignoring checkpoint and resume until after a failure happens
- forgetting that logging is part of the product, not just debugging sugar

---

## Resources For This Phase

| Resource | Why it matters | How I should use it |
| --- | --- | --- |
| LangGraph docs | Best foundation for stateful orchestration | Build the quickstart, then extend it with persistence |
| CrewAI docs | Good comparison point for multi-agent collaboration | Study role design and delegation |
| AI Engineering by Chip Huyen | Strong systems framing | Focus on reliability and production patterns |
| Anthropic agent engineering writeups | Good practical heuristics | Extract repeatable guardrails and harness lessons |

---

## Questions I Want To Answer During This Phase

- When does a second agent help, and when does it just create more failure modes?
- What should be stored in state versus derived on the fly?
- What budget and latency controls are realistic for a production agent?
- Which failures should trigger retry, and which should immediately escalate to a human?

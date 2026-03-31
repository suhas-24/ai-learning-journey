# Phase 7 - Agent Orchestration + Harness Engineering

**Status:** 🔴 Not Started  
**Started:** Not started yet  
**Completed:** Not completed yet  
**Estimated Duration:** 6-8 weeks

---

## Why This Phase Exists

Single-loop agents fail in the real world because they have no durable memory, no explicit control flow, and no disciplined response when something goes wrong. Orchestration adds structure. Harness engineering adds the operational shell that keeps the agent alive long enough to do useful work.

This is the phase where the system becomes more important than the prompt.

---

## Chapter Map

### 7.1 Orchestration Frameworks

- LangGraph gives a graph of nodes, edges, and state transitions.
- CrewAI organizes work by role and delegation.
- PydanticAI emphasizes typed inputs and outputs.
- OpenAI Agents SDK focuses on handoffs, tracing, and validation patterns.

### 7.2 Harness Engineering

The harness is the set of systems around the model that handle planning, retries, rollbacks, budgets, approval gates, checkpoints, and audit logs.

### 7.3 Agent Design Patterns

The same agent architecture should not be used for every problem. Some tasks want one agent with tools. Others want an orchestrator and sub-agents. Still others want parallel workers or a debate structure.

### 7.4 Long-Running Execution

Long tasks need checkpoints, resumability, progress reporting, and a clear dead-letter path when repeated failures happen.

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
- reflection is only useful when it is scored against a clear rubric
- human oversight should appear at the irreversible boundaries

---

## Phase Project: Persistent Research + Execution Agent

**Project goal:** build a stateful multi-agent system that can survive longer tasks, recover from failure, and ask for approval at the right moments.  
**Planned repo:** dedicated Phase 7 repository  
**Current project status:** planned, not started

### Planned Architecture

- Researcher gathers inputs and tool output
- Analyst synthesizes and critiques
- Reporter turns the result into a final artifact
- LangGraph manages state, transitions, and checkpoints
- a cost governor limits total spend
- an approval gate blocks irreversible output changes

### Harness Features That Must Exist

- checkpoint state every few steps
- retry transient tool failures
- stop on budget overrun
- emit structured logs
- support resume after crash or interruption
- log each meaningful decision for debugging later

### What This Project Should Prove

- I can design control flow instead of a single prompt loop.
- I can choose the right orchestration pattern for the job.
- I can make long-running work inspectable and recoverable.
- I can protect the system from cost and failure spirals.

---

## Exit Criteria

- I can explain the difference between orchestration and harnessing.
- I can choose a framework based on constraints, not brand familiarity.
- I can build a persistent state model for a multi-step task.
- I can insert human approval where it actually matters.
- I can describe the failure path for a long-running agent and how the harness should react.

---

## Common Traps To Avoid

- adding more agents when one agent is still poorly designed
- confusing branching logic with real reliability
- building reflection loops without clear scoring criteria
- ignoring checkpoint and resume until after failure happens
- forgetting that logging is part of the product, not just debugging sugar

---

## Resources And What They Help Me Learn

| Resource | What It Teaches |
| --- | --- |
| LangGraph docs | How stateful orchestration is modeled and persisted |
| CrewAI docs | How role design and delegation change multi-agent behavior |
| AI Engineering by Chip Huyen | How to think about reliability, evaluation, and production systems |
| Anthropic agent engineering writeups | Practical heuristics for control, reflection, and failure handling |

---

## Questions I Want To Answer During This Phase

- When does a second agent help, and when does it just add failure modes?
- What should be stored in state versus derived on the fly?
- What budget and latency controls are realistic for a production agent?
- Which failures should trigger retry, and which should immediately escalate to a human?

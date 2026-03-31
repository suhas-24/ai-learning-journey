# Project 2 - Multi-Agent Research Harness

**Phase:** Phase 7  
**Status:** 🔴 Not Started  
**Started:** Not started yet  
**Completed:** Not completed yet

---

## Problem Statement

Build a three-agent system that can research, analyze, and report on a complex task with persistence, retries, approval gates, and observability. The point is not to maximize agent count. The point is to prove I can design a reliable harness around multi-step autonomous behavior.

---

## What This Project Teaches

- how to split work into distinct agent responsibilities
- how state persists across long tasks
- how approvals and rollback protect irreversible actions
- how traces and logs make multi-agent systems debuggable
- how to keep autonomy bounded by a clear harness

---

## Agent Roles

### Researcher

- gathers raw information
- chooses tools and retrieval paths
- records source material clearly
- keeps citations and evidence organized

### Analyst

- synthesizes findings
- checks for contradictions or weak evidence
- decides whether more retrieval is needed
- scores whether the current evidence is good enough to continue

### Reporter

- turns the final result into a usable output format
- makes assumptions explicit
- routes the result to the human approval step
- produces the final artifact in a predictable structure

---

## Planned Architecture

- LangGraph or equivalent stateful orchestration
- persisted state in Redis or SQLite
- MCP or CLI-connected tools for search, files, and GitHub
- reflection step that scores output before advancing
- human approval gate before irreversible actions
- Langfuse traces for every step
- clear schema for task state, evidence, and pending decisions

---

## Harness Features That Must Exist

- checkpoint every few steps
- resume after interruption
- retry transient tool failures
- hard budget cap
- timeout boundaries for long-running tasks
- audit log with structured events
- isolated sub-agent context so one agent does not contaminate another unnecessarily
- a way to stop or pause the run when confidence drops too low

---

## Milestones

1. Build a single-agent research pipeline with state.
2. Split responsibilities into Researcher, Analyst, and Reporter.
3. Add checkpointing and resume.
4. Add reflection and approval gates.
5. Add observability and performance reporting.
6. Harden the harness with clear failure handling and auditability.

---

## Performance Metrics

| Metric | Target Direction |
| --- | --- |
| Task success rate | up |
| Avg cost per task | down or controlled |
| Avg completion time | predictable |
| Tool call success rate | high |
| Human interventions | only where safety requires them |

---

## Main Risks

- too many agents with unclear boundaries
- excessive cost from repeated loops
- state model becoming too messy to reason about
- approval gates added too late in the flow
- agent handoffs becoming inconsistent or lossy
- prompts drifting between runs because state is poorly structured

---

## What "Done" Looks Like

- can complete a complex research task lasting longer than a short chat turn
- survives interruption and resumes correctly
- exposes its reasoning path and tool history through traces
- asks for approval before risky output actions
- has enough logging to debug a bad run after the fact
- the role boundaries are clear enough that another person could extend the system safely

---

## Links

- **Planned GitHub repo:** to be created during Phase 7
- **Demo goal:** record a full run showing pause, resume, and approval

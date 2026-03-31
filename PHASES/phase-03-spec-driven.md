# Phase 3 - Spec-Driven Development

**Status:** 🔴 Not Started  
**Started:** Not started yet  
**Completed:** Not completed yet  
**Estimated Duration:** 2 weeks

---

## Why This Phase Matters

Ad-hoc prompts inside Python files are technical debt. They are hard to review, easy to break, and invisible to future collaborators. This phase introduces the idea that agent behavior should be declared in versioned files before code is written.

The point is to make agent behavior inspectable, editable, and testable.

The deeper lesson is that an AI system should have a human-readable contract. If I cannot explain what the agent is allowed to do, what it should avoid, and how it knows it succeeded, then the system is not yet ready to grow.

---

## Chapter Map

### Chapter 1: Why Specs Exist

Specs turn "what should this agent do?" into a durable artifact. Instead of burying behavior inside code or prompts, I write it down where it can be reviewed and versioned.

### Chapter 2: The Spec Ecosystem

Different files serve different audiences. `AGENTS.md` describes the agent. `CLAUDE.md` describes the repo. `SKILL.md` describes a reusable workflow or capability. `.cursorrules` affects the editor. `SYSTEM.md` captures global policy. The important thing is not the file names themselves, but having clear layers.

### Chapter 3: Writing Good Constraints

Constraints are not there to be dramatic. They are there to prevent ambiguity. Good constraints tell the agent what it must never do, what it should always do, and when it should escalate.

### Chapter 4: Defining Success

An agent needs a finish line. That finish line may be "summarize the findings," "create the issue," or "ask for approval before writing." Without a success definition, the agent can keep wandering.

### Chapter 5: Spec-Driven Workflow

The workflow is contract first, code second. The spec is the source of truth. If the code disagrees with the spec, the code is wrong.

---

## Topic Guide

### Role Definition

- one responsibility per agent keeps behavior understandable
- role language should be concrete, not theatrical
- the agent should know what kind of work belongs to it

### Tool Contracts

- tools should list inputs, outputs, and when to use them
- examples help reduce misuse
- small tools are easier to reason about than giant multipurpose ones

### Boundaries And Escalation

- explicit no-go areas are as important as allowed behaviors
- human escalation should be part of the design
- the agent should know when it should stop and ask instead of guessing

### Versioned Behavior

- spec files belong in Git
- spec changes should be reviewed like code changes
- behavior history should be traceable over time

---

## Study Sequence

1. inspect an existing agent or tool spec
2. identify role, tools, constraints, and success criteria
3. write a minimal but complete `AGENTS.md`
4. add tool-specific `SKILL.md` files only where behavior needs reuse
5. check whether behavior can be changed by editing the spec alone

---

## What Good Specs Should Achieve

- another person can understand the agent without reading Python first
- behavior changes can happen by editing spec files instead of rewriting logic
- coding agents have enough context to make useful changes safely
- failures become easier to debug because intended behavior is written down

---

## A Mental Model For This Phase

Think of specs as the behavioral interface of the agent. The code is the machine. The spec is the contract. The best systems make the contract visible enough that another person can understand and improve it without reading every implementation detail first.

---

## Phase Project: Convert the Phase 2 Agent Into a Spec-Driven System

**Project goal:** take the raw research agent from Phase 2 and move its behavior into spec files.  
**Planned repo:** the same repository as the Phase 2 project, extended with specs  
**Current project status:** design stage only

### What to produce

- `AGENTS.md` for the research agent
- `CLAUDE.md` for repo conventions and working rules
- one `SKILL.md` per important workflow or tool
- a startup step where the agent reads its own spec files

### Validation target

If I can change meaningful behavior by editing a spec file without changing Python code, the phase is working.

---

## Exit Criteria

- I can explain the purpose of `AGENTS.md`, `CLAUDE.md`, and `SKILL.md`.
- I can write constraints that are precise instead of vague.
- I can define "done" for an agent task.
- I can keep specs in Git and treat them like code.
- I can identify behavior that does not belong hardcoded inside an implementation file.

---

## Common Traps To Avoid

- writing specs that are too fluffy to guide implementation
- duplicating the same rules in five places
- mixing architecture decisions, coding style, and behavioral rules into one giant document
- treating specs as marketing copy instead of executable guidance
- changing code but forgetting to update the spec

---

## Resource Notes

### Real `AGENTS.md` Examples

Read them to see how strong instructions stay specific, short, and actionable. The useful pattern is "who this agent is, what it does, what it must not do."

### Claude Code Docs

Use them to understand how repo-level instructions influence coding agents. The goal is a project file that improves output without becoming a junk drawer.

### Cursor Rules Examples

Study them for editor behavior and lightweight guardrails. Good editor rules are narrow, concrete, and easy to update.

---

## Questions I Want To Answer During This Phase

- What is the smallest useful spec that still changes agent behavior?
- Which rules belong in a global file versus a task-specific skill?
- How do I keep specs readable without making them vague?
- What kinds of behavior should never be left implicit?

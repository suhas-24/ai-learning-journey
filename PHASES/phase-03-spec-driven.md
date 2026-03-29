# Phase 3 - Spec-Driven Development

**Status:** 🔴 Not Started  
**Started:** Not started yet  
**Completed:** Not completed yet  
**Estimated Duration:** 2 weeks

---

## Why This Phase Matters

Ad-hoc prompts inside Python files are technical debt. They are hard to review, easy to break, and invisible to future collaborators. This phase introduces the idea that agent behavior should be declared in versioned files before code is written.

The point is to make agent behavior inspectable, editable, and testable.

---

## Core Ideas To Master

### The Spec File Ecosystem

| File | Why it exists |
| --- | --- |
| `AGENTS.md` | Defines role, goals, tools, constraints, and completion conditions |
| `CLAUDE.md` | Gives coding agents project-specific behavior and repo rules |
| `SKILL.md` | Explains a reusable workflow or tool contract clearly |
| `.cursorrules` | Sets editor-level behavior for Cursor |
| `SYSTEM.md` | Establishes high-level global rules for custom agents |

### Spec Design Principles

- one agent should have one clear responsibility
- constraints must be explicit, not implied
- success criteria should tell the agent when it is done
- tool usage should be described in plain language and examples
- escalation behavior matters as much as happy-path behavior

### Workflow Discipline

1. write the behavioral contract
2. write the tool contract
3. review whether the task is actually clear
4. only then implement the code

---

## What Good Specs Should Achieve

- another person can understand the agent without reading Python first
- behavior changes can happen by editing spec files instead of rewriting logic
- coding agents have enough context to make useful changes safely
- failures become easier to debug because intended behavior is written down

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

## Resources For This Phase

| Resource | Why it matters | How I should use it |
| --- | --- | --- |
| Real `AGENTS.md` examples | Shows what good constraints look like | Compare multiple repos and note common patterns |
| Claude Code docs | Helps structure `CLAUDE.md` well | Use it to define repo-specific coding rules |
| Cursor rules examples | Useful for editor behavior | Keep them minimal and testable |

---

## Questions I Want To Answer During This Phase

- What is the smallest useful spec that still changes agent behavior?
- Which rules belong in a global file versus a task-specific skill?
- How do I keep specs readable without making them vague?
- What kinds of behavior should never be left implicit?

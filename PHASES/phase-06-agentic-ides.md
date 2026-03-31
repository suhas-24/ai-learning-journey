# Phase 6 - Agentic IDEs + Coding Agents

**Status:** 🔴 Not Started  
**Started:** Not started yet  
**Completed:** Not completed yet  
**Estimated Duration:** 2 weeks to set up, then used throughout the roadmap

---

## Why This Phase Exists

Coding agents are part of modern development now, but they are not magic. They are productive because they can read files, propose changes, run commands, and iterate faster than a human can type. They are dangerous when they produce code the human cannot explain.

This phase is about building a professional relationship with agentic tools: use them for speed, but keep ownership of judgment, architecture, and review.

---

## Chapter Map

### 6.1 AI-Native IDEs

Cursor, Windsurf, and Zed sit inside the editor. They are strongest when I want interactive help, fast diffs, and a visible model-driven workflow while I stay in the loop.

### 6.2 CLI Agents

Claude Code, OpenAI Codex CLI, and Aider work from the terminal. They tend to feel more like goal-oriented collaborators that can inspect a repo and make file-level changes.

### 6.3 Editor Extensions

Cline, Roo Code, and GitHub Copilot Agent are closer to a plugin experience. They can be helpful, but the quality depends heavily on how clearly the task is framed.

### 6.4 Workflow Discipline

The tool matters less than the process: give good context, inspect the plan, review the diff, and never merge what I do not understand.

---

## Tool Categories To Understand

### AI-Native IDEs

- Cursor: strongest when I want interactive assistance and direct code editing in the editor
- Windsurf: good for comparing multiple model behaviors in one workflow
- Zed: attractive when I want a fast, privacy-oriented editor workflow

### CLI Agents

- Claude Code: terminal-first and file-aware
- OpenAI Codex CLI: useful for structured, repo-aware tasks
- Aider: git-native and open-source, which makes it a strong comparison point

### Editor Extensions

- Cline: flexible and open
- Roo Code: variant with a different task style
- GitHub Copilot Agent: convenient inside the GitHub ecosystem

---

## Working Rules For Coding Agents

- write repo instructions before assigning real work
- let the agent inspect the codebase before it edits anything
- ask for a plan before asking for implementation on non-trivial tasks
- review the diff before running the code, not after blindly accepting it
- use agents to speed up execution, not to outsource understanding
- never merge code that I cannot explain line by line if needed

---

## Practice Loop

1. Pick a bounded task in a repo I already understand.
2. Ask the agent to inspect context and explain its plan.
3. Compare its plan against my own mental model.
4. Let it make a small, testable change.
5. Review the diff and run checks.
6. Write down what the agent got right, what it missed, and what I had to fix.

---

## Phase Project: Agent-Assisted Refactor Log

**Project goal:** maintain a running log of coding-agent sessions, including task framing, model behavior, human review, and outcomes.  
**Planned repo:** could live in a dedicated notes repo or in this repository under a future log section  
**Current project status:** planned, not started

### What The Log Should Capture

- task framing
- tool used
- scope of change
- what the agent understood correctly
- hallucinations, overreach, or unsafe assumptions
- what human review had to correct

### What This Project Should Teach

- which agent surfaces fit exploration versus implementation versus verification
- how much context is enough before handing a task to an agent
- where human review creates the most value

---

## Exit Criteria

- I can explain the difference between an IDE copilot and a goal-based CLI agent.
- I know how to prepare repo instructions before assigning real work.
- I can spot hallucinations, overengineering, and unsafe edits in generated diffs.
- I have a repeatable review workflow for agent-produced code.

---

## Common Traps To Avoid

- vibe coding beyond my understanding
- asking for architecture decisions before understanding the problem
- giving tasks that are too vague or too broad
- trusting clean-looking code more than tested code
- using coding agents as an excuse not to learn fundamentals

---

## Resources And What They Help Me Learn

| Resource | What It Teaches |
| --- | --- |
| Claude Code docs | File-aware CLI workflows, task framing, and review discipline |
| Cursor docs | Editor-centric collaboration and rules-driven behavior |
| Aider docs | Git-native workflows and explicit file diffs |

---

## Questions I Want To Answer During This Phase

- Which tasks should I always keep human-led?
- How much context should I provide before asking an agent to edit?
- What is the fastest safe way to review generated code?
- Which coding agent fits exploration, implementation, and verification best?

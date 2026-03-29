# Phase 6 - Agentic IDEs + Coding Agents

**Status:** 🔴 Not Started  
**Started:** Not started yet  
**Completed:** Not completed yet  
**Estimated Duration:** 2 weeks to set up, then used throughout the roadmap

---

## Why This Phase Matters

Coding agents are now part of the workflow, whether I like it or not. The question is not whether to use them. The question is how to use them without becoming dependent on code I do not understand.

This phase is about learning to collaborate with agents while keeping judgment, review discipline, and architectural ownership.

---

## Tool Categories To Understand

### AI-Native IDEs

- Cursor
- Windsurf
- Zed with local model support

### CLI Agents

- Claude Code
- OpenAI Codex CLI
- Aider

### Editor Extensions

- Cline
- Roo Code
- GitHub Copilot Agent

Each category changes how much autonomy the tool gets, how visible its actions are, and how review should work.

---

## Working Rules For Coding Agents

- write repo instructions before assigning real work
- let the agent read the codebase before asking it to modify anything
- review every diff like a skeptical engineer, not a grateful spectator
- use agents to accelerate execution, not outsource understanding
- never merge code I cannot explain

---

## Practice Loop For This Phase

1. Pick a small task in a repo I understand.
2. Ask one coding agent to inspect context first.
3. Compare its plan with my own mental model.
4. Let it implement a bounded change.
5. Review the diff, run checks, and explain the change in my own words.
6. Record what the agent did well and where it hallucinated, overreached, or missed context.

---

## Phase Project: Agent-Assisted Refactor Log

**Project goal:** maintain a running log of coding-agent sessions, including what task was given, what changed, what failed, and what human review caught.  
**Planned repo:** could live in a dedicated notes repo or in this repository under a future log section  
**Current project status:** planned, not started

### What the log should capture

- prompt or task framing
- tool used
- scope of change
- what the agent understood correctly
- mistakes or dangerous assumptions
- what I had to fix manually

### What this project should teach

- how different agent surfaces behave on the same kind of task
- how to give instructions that produce better results
- where human review creates the most value

---

## Exit Criteria

- I can explain the difference between IDE copilots and goal-based CLI agents.
- I know how to prepare repo instructions for a coding agent.
- I can spot common hallucinations, overengineering, and unsafe edits in generated diffs.
- I have a repeatable review workflow for agent-produced code.

---

## Common Traps To Avoid

- vibe coding beyond my understanding
- asking for architecture decisions before I understand the problem
- giving tasks that are too vague or too broad
- trusting clean-looking code more than tested code
- using coding agents as an excuse not to learn fundamentals

---

## Resources For This Phase

| Resource | Why it matters | How I should use it |
| --- | --- | --- |
| Claude Code docs | Best reference for CLI agent workflows | Practice file-aware tasks and review loops |
| Cursor docs | Useful for repo rules and editor flow | Compare interactive editing with CLI agents |
| Aider docs | Good open-source contrast | Notice how Git-native workflows shape review |

---

## Questions I Want To Answer During This Phase

- Which tasks should I always keep human-led?
- How much context should I provide before asking an agent to edit?
- What is the best way to review generated code quickly but safely?
- Which coding agent fits exploration, implementation, and verification best?

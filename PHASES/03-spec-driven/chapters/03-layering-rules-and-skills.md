# Chapter 3 - Layering Repo Rules, Agent Files, and Skills

If `repo`, `agent`, and `skill` are all new words, here is the simple split:

- a `repo` is the whole project folder
- an `agent` is one worker with a specific job
- a `skill` is one reusable procedure for doing a repeated task

Not every rule belongs in the same file. Good spec-driven systems separate layers so each one has a clear job.

Here, a `layer` just means a level of responsibility. Bigger rules live higher up, and narrower instructions live closer to the worker that uses them.

## 1. Repo-Level Rules

A repo-level instruction file explains rules that apply broadly:

- coding conventions
- review standards
- project structure expectations
- default safety boundaries

This is where a file like `CLAUDE.md` or another repo policy document often fits.

## 2. Agent-Level Rules

An agent-level file explains one worker’s identity and responsibility. That is where `AGENTS.md` or a role-specific contract often fits.

Typical contents:

- ownership
- task boundaries
- success conditions
- escalation behavior

## 3. Skill-Level Rules

A `SKILL.md` file usually describes a reusable workflow, not a whole identity.

Examples:

- how to triage failing tests
- how to review a documentation module
- how to collect evidence before editing

This keeps specialized procedures reusable across multiple agents.

## 4. Worked Layering Example

Repo file:

```text
All documentation changes must include runnable examples where appropriate.
```

Agent file:

```text
You own phases 1 through 3 and may not edit other phases.
```

Skill file:

```text
Before editing docs, inspect the existing file, identify missing examples, then patch the file with explanations and checkpoints.
```

These three rules do different jobs. Putting them all in one file would make the system harder to maintain.

Think of it like this:

- the repo file tells everyone the house rules
- the agent file tells one person what room they are responsible for
- the skill file tells them how to do one repeated task well

## 5. Common Confusion

### Everything lives in one giant file

That creates a junk drawer. Review becomes difficult because unrelated concerns are mixed together.

### Rules are scattered with no ownership

Now nobody knows where to update behavior when the system changes.

## 6. What To Practice

- take one mixed set of rules and separate them into repo, agent, and skill layers
- explain why each rule belongs where you placed it

Next: [Chapter 4: Review and Change Management](./04-review-and-change-management.md)

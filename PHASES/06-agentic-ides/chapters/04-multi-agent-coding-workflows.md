# Chapter 4 - Multi-Agent Coding Workflows

Subagents are useful when they reduce context overload and parallelize genuinely separable work. They are harmful when ownership overlaps or when the conductor does not define integration rules.

## Healthy Multi-Agent Pattern

Use a conductor plus workers:

- conductor owns overall plan, file boundaries, integration, and final verification
- each worker owns a bounded slice with no overlapping writes
- reviewer agents inspect work without rewriting it blindly

## Handoff Contract

A worker assignment should include:

- exact owned files or directories
- files that must not be touched
- required structure or artifacts
- commands to run
- expected summary format

Example:

```text
Own src/retrieval/ and tests/retrieval/.
Do not touch docs/, infra/, or other phases.
Add a benchmark script under scripts/.
Run pytest tests/retrieval -q.
Return files changed, findings, and conductor follow-up.
```

## Integration Rules

The conductor should:

1. review each worker summary
2. inspect overlaps before merging work
3. run repo-level checks only after workers finish
4. preserve unexpected edits made by other workers unless there is a direct conflict

## When To Spawn Another Agent

Add a worker only if:

- the task has a clean ownership boundary
- the worker can finish with its own checks
- the conductor can verify the result without reopening the whole repo

## When Not To

Do not spawn another agent for:

- one-file edits
- vague research with no owned output
- tasks that need the same write access as the main agent

## Final Principle

Multi-agent coding is a coordination problem first and a model problem second. Good boundaries beat clever prompts.

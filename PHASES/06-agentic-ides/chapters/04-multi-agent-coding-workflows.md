# Chapter 4 - Working With More Than One Agent

Multiple agents only help when the work can be split cleanly.

If two agents need the same file at the same time, the setup is probably wrong.

## A Healthy Pattern

Use a conductor and workers:

- the conductor owns the overall plan
- each worker owns a clear slice
- a reviewer checks the work without blindly rewriting it

## What A Handoff Should Say

A good handoff includes:

- the exact files or folders the worker owns
- the files it must not touch
- the artifacts it should produce
- the checks it should run
- the format of the final report

Example:

```text
Own src/retrieval/ and tests/retrieval/.
Do not touch docs/, infra/, or other phases.
Add a benchmark script under scripts/.
Run pytest tests/retrieval -q.
Return files changed, findings, and conductor follow-up.
```

## What The Conductor Does

The conductor should:

1. review each worker summary
2. check for overlap
3. run repo-level checks after the workers finish
4. keep unrelated edits unless they truly conflict

## When To Add Another Agent

Add a worker only if:

- the task has a clear ownership boundary
- the worker can finish with its own checks
- the result can be verified without rereading the whole repo

## When Not To

Do not add another agent for:

- a one-file edit
- vague research with no real output
- work that would still require the same write access

## Final Rule

Multi-agent work is mostly about coordination. Good boundaries matter more than clever prompts.

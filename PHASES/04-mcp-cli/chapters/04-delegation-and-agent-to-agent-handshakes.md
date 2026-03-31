# Chapter 4 - Safe Delegation Between Agents

If `delegation` is new, it just means "give part of the work to someone else on purpose."

Delegation means giving part of the work to another agent on purpose.

A `handshake` is the small exchange of information that lets both sides agree on the task before work starts. In this chapter, it means the notes that make the handoff safe and clear.

That sounds simple, but it only helps when the second agent truly owns a different piece of the job. If both agents need the same files, the same permission, and the same context, then delegation is mostly noise.

## When Delegation Helps

Use a second agent when:

- one worker can do implementation and another can do review
- one worker has a different permission boundary
- one worker can finish a clearly bounded slice in parallel

Do not use a second agent when:

- the prompt is just vague
- the work is one file and one person can finish it
- both agents would have to write the same files

## What A Handoff Should Say

A good handoff is just a clear note.

It should include:

- the goal
- the owned files or folders
- the files that are off limits
- the checks to run
- the format of the final report

Example:

```json
{
  "objective": "Compare retrieval latency before and after reranking.",
  "owned_paths": ["evals/", "reports/retrieval/"],
  "must_not_touch": ["src/production/"],
  "deliverables": ["report.md", "latency-table.csv"],
  "return_format": "short summary with findings and next actions"
}
```

## Builder And Reviewer

One healthy pattern is:

- builder agent changes the code and runs checks
- reviewer agent reads the diff and looks for mistakes

This helps because a builder can accidentally convince itself that its own work is perfect.

## Common Problems

### The task was too big

If a worker needs the whole repository, the split is probably wrong.

### Ownership was unclear

If two agents can change the same file, they can easily collide.

### The summary was treated like proof

Another agent's summary is helpful, but it is not proof. Use diffs, logs, and test output.

## Decision Steps

Before you add another agent, ask:

1. What part of the work is truly separate?
2. Can the second agent finish without shared writes?
3. What proof will show the job is done?
4. Who checks the result?

## Next Step

Do [Lab 1](../labs/lab-01-github-issue-three-ways.md) and compare what changed when the same job was solved three different ways.

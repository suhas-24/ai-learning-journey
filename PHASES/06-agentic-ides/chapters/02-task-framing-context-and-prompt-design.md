# Chapter 2 - Writing a Clear Task Brief

Most agent problems are not really model problems. They are task problems.

If the task is vague, the agent will guess. If the task is bounded, the agent has a chance to be helpful.

## What A Good Brief Includes

- the objective
- the files or folders the agent may edit
- the files or systems the agent must not touch
- the checks the agent should run
- the format of the final answer

Use [../snippets/task-brief-template.md](../snippets/task-brief-template.md) as a starting point.

## Bad Versus Good

Bad:

```text
Fix the retrieval code.
```

Good:

```text
Refactor the retrieval layer so indexing and query execution live in separate modules.
Touch only src/retrieval/ and tests/retrieval/.
Do not change deployment config.
Run pytest tests/retrieval -q.
Return a short summary with files changed and any open risks.
```

The second prompt is better because it says what to change, what not to change, and how to prove success.

## Context

`Context` is the information the agent can see while it works.

Give the agent:

- the repo instructions that matter
- only the files it needs
- nearby files if they help
- one clear definition of done

Do not give the agent:

- a giant pile of unrelated prose
- instructions without boundaries
- both brainstorming and execution instructions at once

## Example

Suppose you want an agent to compare two ranking strategies.

A strong brief would say:

1. inspect `src/retrieval/` and `tests/retrieval/`
2. do not edit deployment config
3. add a tiny benchmark script under `scripts/`
4. return results as a table

That makes it much more likely the agent will produce something useful.

Next: [Chapter 3](./03-review-verification-and-safe-iteration.md).

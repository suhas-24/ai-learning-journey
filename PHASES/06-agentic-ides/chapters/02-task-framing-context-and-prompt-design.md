# Chapter 2 - Writing a Clear Task Brief

Most agent problems are not really model problems. They are task problems.

If the task is vague, the agent guesses. If the task is bounded, meaning small and clearly limited, the agent can help.

## What A Task Brief Is

A task brief is a short instruction that tells the agent:

- what to do
- where to do it
- where not to go
- how success will be checked

Think of it like giving directions before someone starts moving furniture. If the room is not named, the route is not clear, and the rules are not stated, you will get the wrong result.

## What A Good Brief Includes

- the objective in one or two sentences
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

Why this is weak:

- it does not say which retrieval code
- it does not say what "fix" means
- it does not say how to prove success

Good:

```text
Refactor the retrieval layer so indexing and query execution live in separate modules.
Touch only src/retrieval/ and tests/retrieval/.
Do not change deployment config.
Run pytest tests/retrieval -q.
Return a short summary with files changed and any open risks.
```

Why this is better:

- it names the task
- it names the boundaries
- it names the check
- it names the return format

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
- brainstorming notes mixed with execution instructions

## Example

Suppose you want an agent to compare two ranking strategies.

A strong brief would say:

1. inspect `src/retrieval/` and `tests/retrieval/`
2. do not edit deployment config
3. add a tiny benchmark script under `scripts/`
4. return results as a table

That makes it much more likely the agent will produce something useful because the task is narrow and the shape of the output is clear.

Next: [Chapter 3](./03-review-verification-and-safe-iteration.md).

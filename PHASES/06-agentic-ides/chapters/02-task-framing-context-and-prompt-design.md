# Chapter 2 - Task Framing, Context, and Prompt Design

Many agent failures are prompt design failures in disguise. If the task lacks boundaries, expected outputs, or repo context, the model is forced to guess.

## What a Good Task Brief Contains

- objective
- owned files
- forbidden files or systems
- success criteria
- checks to run
- output format

Use [../snippets/task-brief-template.md](../snippets/task-brief-template.md) as a reusable starting point.

## Bad vs Good Prompt

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

The second prompt reduces ambiguity around scope, verification, and return format.

## Context Strategy

Give the agent:

- repo instructions if they exist
- a small set of target files
- adjacent files only when needed
- one clear success definition

Avoid:

- pasting irrelevant architecture prose
- asking for implementation before the agent has inspected the codebase
- mixing brainstorm mode and execute mode in one vague instruction

## Worked Example

Suppose you want an agent to compare two retrieval ranking strategies.

Strong brief:

1. inspect `src/retrieval/` and `tests/retrieval/`
2. do not edit production config
3. add a small benchmark script under `scripts/`
4. return results as a table

That prompt makes it easier for the agent to produce useful artifacts instead of confident fluff.

Continue to [Chapter 3](./03-review-verification-and-safe-iteration.md).

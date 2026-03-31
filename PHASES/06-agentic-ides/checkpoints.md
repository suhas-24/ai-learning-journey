# Phase 06 Checkpoints

Use this page to check understanding, not memorization.

## Concept Checks

You are ready to move on if you can explain:

1. the difference between an IDE agent, a CLI agent, and an extension
2. why the task brief matters so much
3. what makes an agent change trustworthy
4. when a second agent helps and when it does not
5. what the conductor owns in a multi-agent workflow

## Practical Checks

- I can write a task brief with owned and forbidden paths.
- I can review a diff for scope creep.
- I can verify a change with commands, not just summary text.
- I can compare two agent workflows on the same task.
- I can split work across agents without overlapping writes.

## Mini Quiz

Question: An agent changed five unrelated files while supposedly fixing one parser bug. Is that okay if tests pass?

Expected answer: No. Passing tests do not cancel scope creep.

Question: When is a second agent worth adding?

Expected answer: When the work has a clean ownership boundary or a different capability.

# Phase 06 Checkpoints

## Concept Checks

You are ready to advance if you can explain:

1. the difference between an IDE agent, a CLI agent, and an editor extension
2. why task framing often matters more than model choice
3. what evidence makes an agent-produced change trustworthy
4. when a subagent should be spawned and when it should not
5. what the conductor must own in a multi-agent workflow

## Practical Checks

- I can write a bounded task brief with owned and forbidden paths.
- I can review a diff for scope creep and invented behavior.
- I can verify a change with commands instead of relying on summary prose.
- I can compare two agent workflows on the same task fairly.
- I can split work across agents without overlapping writes.

## Mini Quiz

Question: An agent changed five unrelated files while supposedly fixing one parser bug. Is that acceptable if tests pass?

Expected answer: No. Passing tests do not excuse scope creep.

Question: When is a second agent justified?

Expected answer: When the work has a clean ownership boundary or distinct capability, not just because parallelism sounds appealing.

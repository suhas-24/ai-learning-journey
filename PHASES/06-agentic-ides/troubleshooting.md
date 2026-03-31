# Phase 06 Troubleshooting

Use this page when a coding-agent workflow feels fast but unsafe.

## The agent keeps changing unrelated files

Common reasons:

- the prompt was too broad
- ownership was not stated
- planning and execution were mixed together

Try this:

- rewrite the brief with exact owned paths
- ask for a plan first
- reject edits outside scope

## The agent sounds confident but the code is wrong

Confidence is not proof.

Try this:

- inspect the diff
- run the checks
- ask for the exact command output

## The agent wants to redesign architecture immediately

Common reasons:

- the task was too vague
- the model filled gaps with guesses

Try this:

- narrow the goal
- say what must not change
- ask for small edits first

## Multi-agent work caused collisions

Common reasons:

- ownership overlapped
- the conductor rules were weak
- workers edited shared files

Go back to [Chapter 4](./chapters/04-multi-agent-coding-workflows.md) and make the split smaller.

# Phase 06 Troubleshooting

Use this page when a coding-agent workflow feels fast but unsafe.

## The agent keeps changing unrelated files

Likely causes:

- the prompt is too broad
- ownership was not specified
- the task mixes planning and execution without boundaries

Fix:

- rewrite the brief with exact owned paths
- ask for a plan first
- reject edits outside scope

## The agent sounds confident but the code is wrong

This is normal. Confidence is not evidence.

Response:

- inspect the diff
- run the checks
- ask for the concrete log or command output summary

## The agent wants to redesign architecture immediately

Likely causes:

- the task is underspecified
- the model is filling gaps with assumptions

Fix:

- narrow the goal
- state what must stay unchanged
- require incremental edits

## Multi-agent setup caused merge collisions

This usually means:

- ownership overlapped
- conductor rules were weak
- workers edited shared docs without coordination

Use [Chapter 4](./chapters/04-multi-agent-coding-workflows.md) and reduce overlap before rerunning the workflow.

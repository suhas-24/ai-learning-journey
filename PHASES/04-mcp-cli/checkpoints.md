# Phase 04 Checkpoints

Use these checks after the chapters and the lab.

## Concept Checks

You should be able to explain:

1. why a command is often the simplest choice for local work
2. what MCP adds beyond a plain function call
3. when a direct HTTP request is simpler than MCP
4. why delegation needs clear ownership
5. which parts of a tool should stay hidden on the server

## Practical Checks

- I can write a JSON schema that rejects extra properties.
- I can wrap a command without building one giant shell string.
- I can explain who owns auth in the CLI and API paths.
- I can write a handoff that names owned files and forbidden files.
- I can compare one workflow across at least two surfaces.

## Mini Quiz

Question: A CI job already has `gh` installed and authenticated. What is the simplest way to create an issue?

Expected answer: `CLI`, unless shared typed discovery is the real requirement.

Question: A team wants one issue-creation tool that several agents can discover. What is the better fit?

Expected answer: `MCP`, because the shared tool contract matters.

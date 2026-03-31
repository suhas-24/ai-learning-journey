# Phase 04 Checkpoints

Use these checkpoints after reading the chapters and completing the labs.

## Concept Checks

You are ready to move on if you can answer these without hand-waving:

1. Why is CLI often the best default for local developer tooling?
2. What value does MCP add beyond "the model can call a function"?
3. When is a direct API wrapper simpler than MCP?
4. What makes a delegation boundary healthy instead of noisy?
5. Which parts of a tool contract should stay server-side?

## Practical Checks

- I can write a JSON schema that rejects extra properties.
- I can wrap a CLI command without shell-string interpolation.
- I can explain the auth flow for both CLI and API variants.
- I can design a handoff contract with explicit owned paths.
- I can compare the same workflow across at least two tool surfaces.

## Mini Quiz

Question: A model running in CI needs to open a GitHub issue, and the runner already has `gh` installed and authenticated. What is the best starting point?

Expected answer: `CLI`, unless there is a strong requirement for reusable typed discovery across clients.

Question: A shared platform team wants one discoverable issue tool for several agent clients. What is the better fit?

Expected answer: `MCP`, because the schema and discovery layer are part of the requirement.

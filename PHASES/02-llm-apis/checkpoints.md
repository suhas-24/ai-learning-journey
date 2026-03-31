# Phase 2 Checkpoints

## Concept Checks

1. What is an LLM in plain language?
   Review: [Chapter 1](./chapters/01-request-shape-and-message-roles.md)
2. What information does a model request usually include?
   Review: [Chapter 1](./chapters/01-request-shape-and-message-roles.md)
3. Why is structured output better than free-form text for downstream code?
   Review: [Chapter 2](./chapters/02-structured-output-and-tool-calling.md)
4. What is the exact role of your program in a tool-calling loop?
   Review: [Chapter 2](./chapters/02-structured-output-and-tool-calling.md)
5. What makes context focused instead of overloaded?
   Review: [Chapter 3](./chapters/03-context-engineering.md)
6. How would you separate a prompt problem from a tool problem?
   Review: [Chapter 4](./chapters/04-cost-latency-and-failure-analysis.md)

## Practical Checks

- sketch a message array with system, user, assistant, and tool roles
- simulate one tool call by hand
- trim a bloated context window into a focused one
- log latency and validation success for one model step

## Exit Standard

You are ready for the next phase when you can explain the full path from user request to model output to tool result to final answer.

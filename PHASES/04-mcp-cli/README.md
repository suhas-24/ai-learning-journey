# Phase 04 - MCP, CLI, APIs, and Agent Delegation

This module teaches how to choose the right tool surface for an agent system instead of defaulting to the fanciest protocol. By the end, you should be able to explain when a task belongs behind a local CLI, a direct API wrapper, an MCP server, or a specialized downstream agent.

## What You Will Build

- a simple MCP server that exposes a typed tool
- a CLI-driven workflow that shells out to `gh`
- a direct API integration using `httpx`
- a delegation flow where one agent hands work to another with an explicit contract

## Learning Outcomes

After this phase, you should be able to:

- compare MCP, CLI, API, and agent-to-agent patterns with a concrete decision framework
- design a safe tool contract with input validation and constrained side effects
- debug common failures such as bad JSON schemas, shell quoting bugs, and token-heavy prompts
- explain the operational tradeoffs around auth, observability, portability, and maintenance

## Module Map

1. [Chapter 1: Choosing a Tool Surface](./chapters/01-choosing-a-tool-surface.md)
2. [Chapter 2: Building and Calling MCP Tools](./chapters/02-building-and-calling-mcp-tools.md)
3. [Chapter 3: CLI and Direct API Workflows](./chapters/03-cli-and-direct-api-workflows.md)
4. [Chapter 4: Delegation and Agent-to-Agent Handshakes](./chapters/04-delegation-and-agent-to-agent-handshakes.md)
5. [Labs](./labs/lab-01-github-issue-three-ways.md)
6. [Checkpoints](./checkpoints.md)
7. [Troubleshooting](./troubleshooting.md)

## Suggested Order

1. Read Chapter 1 and write down the default tool surface you would choose for three example tasks.
2. Read Chapter 2 and inspect the sample schema in [snippets/mcp-tool-schema.json](./snippets/mcp-tool-schema.json).
3. Read Chapter 3 and run through the CLI and API examples.
4. Read Chapter 4 and model a delegation contract before building one.
5. Complete the lab and then self-test with [checkpoints.md](./checkpoints.md).

## Quick Principle

Use the lightest integration that preserves safety and clarity:

- choose `CLI` for local developer actions that already exist as trustworthy commands
- choose `API` for narrow remote workflows where latency and simplicity matter
- choose `MCP` when discoverability, structured contracts, and tool reuse matter
- choose `A2A` only when a second agent actually owns distinct capability or context

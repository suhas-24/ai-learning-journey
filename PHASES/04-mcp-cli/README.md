# Phase 04 - Tools, Commands, and Handoffs

This phase explains how an AI system reaches outside itself to do real work.

A simple way to think about it is this:

- a `tool` is something that does one job for the system
- a `CLI` is a tool you run by typing a command
- an `API` is a tool you call over the network
- `MCP` is a standard way to describe tools so different clients can discover them
- `agent-to-agent delegation` is one AI worker asking another AI worker to handle a bounded task

If those phrases are new, that is completely fine. The chapters in this module build them from the ground up.

If you want the smallest beginner version of the ideas:

- a `tool` is a helper the system can use to get something done
- a `client` is the thing asking for the tool
- a `server` is the thing that offers the tool and performs the work
- a `protocol` is the shared rulebook that lets the client and server understand each other
- a `tool boundary` is the line between what the model decides and what the tool is allowed to do

## What You Will Learn

- how to choose the simplest tool surface that still solves the job
- how to describe a tool so the caller knows exactly what inputs it accepts
- how to tell the difference between a local command and a remote service
- how to give work to another agent without losing control of scope

## What You Will Build

- one GitHub issue workflow through `gh`
- one GitHub issue workflow through a direct HTTP request
- one small MCP tool with a strict input schema
- one handoff contract for a second agent or reviewer

## Module Map

1. [Chapter 1: What a Tool Surface Is](./chapters/01-choosing-a-tool-surface.md)
2. [Chapter 2: How MCP Tools Work](./chapters/02-building-and-calling-mcp-tools.md)
3. [Chapter 3: CLI and Direct API Workflows](./chapters/03-cli-and-direct-api-workflows.md)
4. [Chapter 4: Safe Delegation Between Agents](./chapters/04-delegation-and-agent-to-agent-handshakes.md)
5. [Lab 1: Build One Workflow Three Ways](./labs/lab-01-github-issue-three-ways.md)
6. [Checkpoints](./checkpoints.md)
7. [Troubleshooting](./troubleshooting.md)

## How To Study This Phase

1. Read Chapter 1 to learn the words.
2. Read Chapter 2 to learn how a tool contract is described.
3. Read Chapter 3 to see when a plain command or API call is enough.
4. Read Chapter 4 to learn when a second agent is actually useful.
5. Do the lab and compare the three ways of solving the same job.

## Simple Rule

Start with the smallest safe integration.

- use a `CLI` when the work already exists as a trustworthy command
- use an `API` when the work is remote and the request is naturally structured
- use `MCP` when you want a shared, typed tool description
- use another agent only when it owns a different job, permission, or chunk of context

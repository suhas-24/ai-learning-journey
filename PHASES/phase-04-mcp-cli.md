# Phase 4 - MCP + CLI + A2A Protocols

**Status:** 🔴 Not Started  
**Started:** Not started yet  
**Completed:** Not completed yet  
**Estimated Duration:** 3-4 weeks

---

## Why This Phase Matters

An agent without tools is just a chat interface. Real utility comes from the ability to call external systems safely and predictably. In 2026 there is no single tool-connection pattern that wins everywhere, so I need to learn the tradeoffs:

- MCP for typed, discoverable, auth-friendly tool contracts
- CLI for local tools and token-efficient workflows
- direct API wrappers for the simplest and lowest-latency integrations
- A2A when one agent needs help from another

This phase is where the curriculum stops being about model responses and starts being about action. The difference is huge: a model answer is information, but a tool call can change state in the real world.

---

## Chapter Map

### Chapter 1: Tool Surfaces

Agents can use tools through direct API calls, command-line programs, or protocol-based servers. The question is not which one is coolest. The question is which one fits the task and the environment.

### Chapter 2: MCP

MCP provides a typed way to expose tools and resources. That matters when the tool boundary should be explicit, discoverable, and stable. It is especially useful when authentication, remote services, and structured contracts matter.

### Chapter 3: CLI Integration

The command line is still one of the best tool surfaces for local and developer-oriented tasks. Tools like `git`, `gh`, `pytest`, and `docker` are already standardized, fast, and familiar. Good CLI integration is often simpler than building a protocol server.

### Chapter 4: Direct API Wrappers

Sometimes the right answer is a thin Python client around a REST endpoint. This is often the simplest path when latency matters and the integration surface is small.

### Chapter 5: A2A

A2A is the language of delegation between agents. It becomes useful when one agent should hand off to another with a different capability, rather than trying to do everything itself.

---

## Topic Guide

### MCP Concepts

- the server exposes capability
- the client discovers and calls it
- typed definitions reduce ambiguity
- authentication belongs in the architecture, not as an afterthought

### CLI Concepts

- shell tools are composable
- local commands are often the fastest bridge to real system actions
- parsing command output is part of the job
- safe execution needs timeout, validation, and scope limits

### API Wrapper Concepts

- the wrapper is often only a few lines
- the important part is handling auth, errors, and payload shape cleanly
- wrappers are useful when the task is narrow and the API is stable

### A2A Concepts

- capability discovery means one agent can ask what another can do
- delegation lets specialized agents work in parallel
- handoff is better than duplication when a task changes shape

---

## Decision Framework To Internalize

| Situation | Best default |
| --- | --- |
| Remote service with complex auth and typed contracts | MCP |
| Local dev tool or script | CLI |
| Simple wrapper where speed matters most | Direct API |
| Agent handing work to another agent | A2A |

The important lesson is not "always use MCP." The important lesson is choosing the lightest tool surface that preserves safety and clarity.

That means the same task can have three valid answers, but the best one depends on context:

- local developer task: CLI
- remote structured service: MCP
- very small integration: direct API
- specialized handoff: A2A

---

## Study Sequence

1. read one MCP quickstart and inspect how tools are described
2. practice calling a local CLI from Python
3. write a direct API wrapper for one narrow service
4. compare the maintenance and runtime tradeoffs
5. reason about where delegation between agents would actually help

---

## Phase Project: One Tool, Three Implementations

**Project goal:** implement the same GitHub Issue Creator workflow three ways and compare them.  
**Planned repo:** a dedicated experiment repo created during this phase  
**Current project status:** planned, not started

### Required implementations

1. MCP server implementation
2. CLI implementation using `gh`
3. direct REST API implementation using `httpx`

### What to measure

- token usage
- implementation complexity
- latency
- reliability
- how much context the agent needs to use each tool correctly

### What this project is really teaching

- there is no silver bullet integration style
- protocol choices affect cost, speed, observability, and operator experience

---

## Exit Criteria

- I can explain when MCP is the right tool and when it is overkill.
- I can safely invoke local CLI tools from Python.
- I can build one small MCP server.
- I can compare CLI and API integrations on more than "it feels better."
- I understand what A2A solves that normal tool calling does not.

---

## Common Traps To Avoid

- building a protocol-heavy solution for a tiny local task
- ignoring auth and audit requirements when choosing a tool integration
- treating CLI output as stable if it actually is not
- assuming agent-to-agent delegation is useful before a single agent works reliably

---

## Resource Notes

### MCP Official Docs

Start with the quickstart and the explanation of client/server roles. Focus on how tools are described and discovered rather than trying to memorize every transport detail.

### A2A Spec

Read it for capability discovery, delegation, and workflow composition. The useful part is the shape of cooperation, not the vendor names.

### `gh` CLI Docs

Use them to understand a practical, production-grade developer tool surface. This matters because a lot of useful agent behavior can be implemented by composing existing commands.

### GitHub REST API Docs

Use them as the simplest baseline for direct integrations. They are the reference point for comparison when deciding whether MCP or CLI adds enough value.

---

## Questions I Want To Answer During This Phase

- What extra safety does MCP buy me in practice?
- How much cheaper is a CLI workflow for local development tasks?
- When is a direct API wrapper the most maintainable answer?
- What coordination problems are actually worth solving with A2A?

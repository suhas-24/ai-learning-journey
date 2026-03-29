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

---

## Core Ideas To Master

### MCP

- client/server model
- JSON-RPC transport
- tool discovery and typed contracts
- authentication-heavy integrations such as GitHub, Slack, databases, and browser tools

### CLI As A Tool Surface

- shell commands can be cheaper and faster than wrapping everything in an MCP server
- local development workflows often fit naturally as `git`, `gh`, `docker`, `pytest`, or `aws` commands
- command execution needs guardrails, argument hygiene, and good output parsing

### A2A

- capability discovery across agents
- delegation to a specialized peer agent
- coordination for parallel work
- best suited to multi-agent systems or mixed-vendor environments

---

## Decision Framework To Internalize

| Situation | Best default |
| --- | --- |
| Remote service with complex auth and typed contracts | MCP |
| Local dev tool or script | CLI |
| Simple wrapper where speed matters most | Direct API |
| Agent handing work to another agent | A2A |

The important lesson is not "always use MCP." The important lesson is choosing the lightest tool surface that preserves safety and clarity.

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

## Resources For This Phase

| Resource | Why it matters | How I should use it |
| --- | --- | --- |
| MCP official docs | Primary source for the standard | Build the quickstart server first |
| A2A spec | Shows the shape of agent delegation | Read for concepts, not memorization |
| `gh` CLI docs | Best local GitHub workflow surface | Rebuild one action end to end |
| GitHub REST API docs | Baseline direct integration example | Compare response shape and auth flow |

---

## Questions I Want To Answer During This Phase

- What extra safety does MCP buy me in practice?
- How much cheaper is a CLI workflow for local development tasks?
- When is a direct API wrapper the most maintainable answer?
- What coordination problems are actually worth solving with A2A?

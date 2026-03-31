# Chapter 1 - Choosing a Tool Surface

The first design mistake in agent systems is choosing the integration method before understanding the task. Tooling decisions should come from the shape of the work, not from protocol hype.

## Four Common Tool Surfaces

### CLI

The command line is best when:

- the tool already exists and is trusted
- the task runs on the same machine as the agent
- a human could plausibly run the same command by hand

Examples:

```bash
gh issue create --title "Bug: cache invalidation" --body "Cache is stale after deploy"
pytest tests/retrieval/test_ranker.py -q
git status --short
```

CLI advantages:

- low implementation cost
- easy local debugging
- good fit for dev tooling

CLI risks:

- brittle parsing if output format changes
- shell quoting bugs
- weaker portability across operating systems

### Direct API Wrapper

An API wrapper is best when:

- you only need a few endpoints
- the service is remote anyway
- you want deterministic request and response handling

Example:

```python
import httpx

response = httpx.post(
    "https://api.github.com/repos/OWNER/REPO/issues",
    headers={"Authorization": f"Bearer {token}"},
    json={"title": "Cache bug", "body": "Repro steps..."},
    timeout=20.0,
)
response.raise_for_status()
```

API advantages:

- explicit payloads
- low latency compared with spawning shells
- easier unit testing than many CLI wrappers

API risks:

- you own auth, retries, and pagination yourself
- the model needs to know the payload contract
- every integration becomes custom code

### MCP

Model Context Protocol is best when:

- the same tool should be discoverable by multiple clients
- tool contracts should be typed and self-describing
- you want a stable boundary between the model and external systems

MCP advantages:

- discoverable tool metadata
- typed schemas reduce ambiguity
- clean separation between client and tool implementation

MCP risks:

- more infrastructure than a one-off script
- another layer to debug
- overkill for tiny local tasks

### Agent-to-Agent Delegation

Delegation is best when:

- a different agent owns distinct context, permissions, or expertise
- the task is large enough to partition
- you need parallel work rather than one giant prompt

Delegation risks:

- extra orchestration complexity
- ambiguous handoff boundaries
- context drift if contracts are weak

## Decision Framework

Use this sequence every time:

1. What side effect is needed?
2. Where does the capability already live?
3. Who owns authentication?
4. Does the model need a typed contract or just a bounded action?
5. Will multiple agents or clients reuse the tool?
6. What is the cheapest safe option?

## Worked Example

Question: "Create a GitHub issue when a nightly evaluation fails."

Option analysis:

- `CLI`: great for a local developer machine or CI runner that already has `gh` auth
- `API`: great for a small service that already talks to GitHub over HTTP
- `MCP`: great if several agent clients should discover and call the same issue-creation tool
- `A2A`: only useful if a separate repo-ops agent owns GitHub permissions and audit policy

Best answer depends on environment:

- local prototype: `CLI`
- backend service: `API`
- shared enterprise tool layer: `MCP`
- regulated team with specialized repo agent: `A2A`

## Anti-Patterns

- building an MCP server for a single `ls` command
- using a shell pipeline when the API payload is simple and structured
- delegating to another agent because the first agent prompt is weak
- letting a model invent flags instead of teaching the actual tool contract

Continue to [Chapter 2](./02-building-and-calling-mcp-tools.md) for the mechanics of MCP tool design.

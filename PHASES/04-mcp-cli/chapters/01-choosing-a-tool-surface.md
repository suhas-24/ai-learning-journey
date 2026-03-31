# Chapter 1 - What a Tool Surface Is

A tool surface is the way a system reaches outside itself to do work.

For example, if an AI system needs to open a GitHub issue, it can do that in more than one way. It might run a command, send an HTTP request, call a shared tool, or ask another agent to do the job. The choice matters because each path has different cost, safety, and reuse tradeoffs.

## Start With the Job

Before choosing a surface, ask a simple question: what must happen in the real world?

- maybe a file should change
- maybe an issue should be created
- maybe a report should be generated
- maybe another worker should review the result

Once the job is clear, the surface becomes easier to choose.

## CLI

`CLI` means command-line interface. That is just a program you run by typing a command in a terminal.

Choose a CLI when:

- the command already exists
- the command is trusted
- the work is local or already available on the machine

Examples:

```bash
git status --short
gh issue create --title "Bug: cache invalidation" --body "Cache is stale after deploy"
pytest tests/retrieval/test_ranker.py -q
```

Why this is nice:

- it is easy to debug
- it is already familiar to many developers
- it is usually the cheapest path

What can go wrong:

- shell quoting can break commands
- text output can be hard to parse
- commands can differ slightly between machines

## API

`API` means application programming interface. In plain English, that means a program sends a request to another program over the network.

Choose an API when:

- the service already lives somewhere remote
- the request can be described with clear input fields
- you want structured responses back

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

Why this is nice:

- the input is explicit
- the response can be JSON
- testing is often simpler than shell parsing

What can go wrong:

- you must manage auth and retries
- you own the network failure handling
- the contract has to be written clearly

## MCP

`MCP` stands for Model Context Protocol. Here, `model` means the AI program, `context` means the information the model can see right now, and `protocol` means an agreed set of rules.

Choose MCP when:

- several clients should find the same tool
- you want a typed, discoverable contract
- you want the tool boundary to stay clear

Why this is nice:

- the tool can advertise what it does
- the input shape is explicit
- multiple clients can reuse the same tool

What can go wrong:

- it adds another system to maintain
- it is too much for one tiny command
- a bad schema can still confuse the caller

## Agent-To-Agent Delegation

Delegation means one agent gives a bounded task to another agent.

Choose delegation when:

- the second agent owns a different piece of the work
- the task can be split without shared writes
- a separate review or verification step would help

Why this is nice:

- you can work in parallel
- a reviewer can catch mistakes
- different permissions can stay separated

What can go wrong:

- the handoff can be vague
- two agents can edit the same file
- the first agent can use delegation to avoid thinking

## Decision Steps

Use this order:

1. What is the job?
2. Is there already a safe command for it?
3. Is the service remote?
4. Do multiple clients need the same tool?
5. Does a second agent truly own a different part of the work?
6. Which option is the smallest safe choice?

## Example

Task: create a GitHub issue when an evaluation fails.

- use `CLI` if the machine already has `gh` and the workflow is local
- use `API` if you are already inside a service that talks to GitHub
- use `MCP` if multiple clients should discover the same issue-creation tool
- use delegation if another agent owns repository operations and review

Next: [Chapter 2](./02-building-and-calling-mcp-tools.md).

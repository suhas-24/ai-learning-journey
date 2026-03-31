# Lab 1 - Build One Workflow Three Ways

In this lab, you will implement the same GitHub issue creation workflow with a CLI wrapper, a direct API wrapper, and an MCP tool. The goal is not just to make the issue appear. The goal is to compare ergonomics, observability, and maintenance cost.

## Goal

Create an issue titled `Lab: compare tool surfaces` in a test repository and record the differences among three implementations.

## Prerequisites

- GitHub account and a test repository
- `gh` installed and authenticated
- Python 3.11+
- an isolated environment with `httpx`

## Part A - CLI Path

Run:

```bash
gh auth status
gh issue create \
  --repo OWNER/TEST_REPO \
  --title "Lab: compare tool surfaces" \
  --body "Created through the CLI workflow." \
  --label experiment
```

Record:

- how much setup was required
- what the failure mode looked like if auth was missing
- whether the output was easy to parse

## Part B - Direct API Path

Use the example in [../snippets/httpx-create-issue.py](../snippets/httpx-create-issue.py).

Run:

```bash
export GITHUB_TOKEN=YOUR_TOKEN
python ../snippets/httpx-create-issue.py
```

Record:

- how explicit the request contract felt
- what extra code you had to own
- how easy it was to surface structured errors

## Part C - MCP Path

Start from [../snippets/mcp-tool-schema.json](../snippets/mcp-tool-schema.json) and implement a server-side tool that hides the repository name and token.

Record:

- how the schema improved or failed to improve tool use
- whether a second client could reuse the same tool easily
- what logs you would want in production

## Reflection Questions

1. Which path had the lowest implementation cost?
2. Which path had the clearest failure surface?
3. Which path would you standardize across a team?
4. Was a second agent needed anywhere in this workflow?

## Deliverable

Create a short comparison table with these columns:

| Approach | Setup cost | Runtime clarity | Reuse potential | Best fit |
| --- | --- | --- | --- | --- |

Then review [../checkpoints.md](../checkpoints.md).

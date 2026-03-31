# Lab 1 - Build One Workflow Three Ways

This lab uses the same small job three times so you can feel the difference between a command, a direct request, and a shared tool description.

## Goal

Create a GitHub issue titled `Lab: compare tool surfaces` in a test repository, then compare the experience.

## What You Need

- a GitHub account
- a test repository you can safely write to
- `gh` installed and signed in
- Python 3.11+ with `httpx`

## Part A - Use The Command

Run:

```bash
gh auth status
gh issue create \
  --repo OWNER/TEST_REPO \
  --title "Lab: compare tool surfaces" \
  --body "Created through the CLI workflow." \
  --label experiment
```

Write down:

- how much setup was needed
- what happened when auth was missing
- how easy the output was to understand

## Part B - Use The HTTP Request

Use [../snippets/httpx-create-issue.py](../snippets/httpx-create-issue.py).

Run:

```bash
export GITHUB_TOKEN=YOUR_TOKEN
python ../snippets/httpx-create-issue.py
```

Write down:

- how clear the request felt
- what extra code you had to own
- how easy it was to see structured errors

## Part C - Use The Shared Tool Shape

Start from [../snippets/mcp-tool-schema.json](../snippets/mcp-tool-schema.json).

Imagine a tool server that hides the repository name and token. The caller only provides the issue title, body, and labels.

Write down:

- whether the schema made the tool easier to understand
- whether a second client could reuse the same tool
- what you would want to log in a real system

## Reflection

1. Which path took the least setup?
2. Which path gave the clearest error messages?
3. Which path would you choose for a team-wide standard?
4. Did a second agent actually help anywhere, or was one worker enough?

## Deliverable

Create a small comparison table:

| Approach | Setup cost | Clarity | Reuse potential | Best fit |
| --- | --- | --- | --- | --- |

Then review [../checkpoints.md](../checkpoints.md).

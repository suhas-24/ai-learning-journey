# Chapter 3 - CLI and Direct API Workflows

If `workflow` sounds abstract, just think "the step-by-step path from a request to a result."

Not every job needs a special protocol.

Sometimes the best tool is already available as a command. Sometimes the best tool is a direct request to a web service. This chapter helps you choose between those two simple options before you reach for anything heavier.

## CLI

`CLI` means command-line interface. It is a program you run from the terminal.

CLI is a strong choice when:

- the command already exists
- the command is trusted
- the work is local or CI-based

Example:

```bash
gh auth status
gh issue create \
  --repo OWNER/REPO \
  --title "Bug: retrieval timeout regression" \
  --body-file issue.md \
  --label bug
```

Why this is useful:

- the command is already doing the hard work
- humans can run the same command by hand
- debugging is usually straightforward

Things to watch:

- quoting mistakes
- unexpected output changes
- hidden environment assumptions

If you wrap a CLI in Python, keep the command as a list of arguments instead of one big string.

```python
import subprocess

command = [
    "gh",
    "issue",
    "create",
    "--repo",
    "OWNER/REPO",
    "--title",
    "Bug: retrieval timeout regression",
    "--body",
    "Observed after deploy 2026-03-31",
]

result = subprocess.run(command, capture_output=True, text=True, timeout=20)
if result.returncode != 0:
    raise RuntimeError(result.stderr.strip())
print(result.stdout.strip())
```

## Direct API

A direct API means your code sends a request to another service over HTTP.

This is often a better choice when:

- the service is already remote
- the input is naturally structured
- you want easier testing and clearer error handling

Example:

```python
import httpx

def create_issue(token: str, repo: str, title: str, body: str) -> dict:
    owner, name = repo.split("/", maxsplit=1)
    response = httpx.post(
        f"https://api.github.com/repos/{owner}/{name}/issues",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
        },
        json={"title": title, "body": body},
        timeout=20.0,
    )
    response.raise_for_status()
    return response.json()
```

Why this is useful:

- the request shape is explicit
- JSON is easy to inspect
- unit tests can mock the request cleanly

Things to watch:

- auth errors
- retries
- rate limits
- network failures

## Quick Comparison

| Question | CLI | API |
| --- | --- | --- |
| Already exists as a trusted command? | Strong | Maybe not |
| Easy to run by hand? | Strong | Weak |
| Easy to test in code? | Medium | Strong |
| Best for a remote service? | Weak | Strong |
| Best when the output is structured? | Medium | Strong |

## Example Choice

Task: run a retrieval evaluation and upload the results.

- use `CLI` if the evaluation tool already ships as a command
- use `API` if the evaluation service is remote and returns JSON

## Simple Rule

If the job is already embodied in a command, use the command. If the job is already a remote service, call the service directly.

Next: [Chapter 4](./04-delegation-and-agent-to-agent-handshakes.md).

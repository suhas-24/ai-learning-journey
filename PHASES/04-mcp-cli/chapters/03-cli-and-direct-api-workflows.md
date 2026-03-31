# Chapter 3 - CLI and Direct API Workflows

MCP is not the answer to everything. Many production systems mix all three patterns: CLI for local tooling, APIs for narrow integrations, and MCP for shared discovery.

## CLI Workflow Design

CLI workflows shine when the tool already exists. The model does not need to know how GitHub issues are created internally if `gh issue create` already does it well.

Example shell flow:

```bash
gh auth status
gh issue create \
  --repo OWNER/REPO \
  --title "Bug: retrieval timeout regression" \
  --body-file issue.md \
  --label bug
```

Safe CLI design principles:

- check tool presence before execution
- keep commands explicit instead of dynamically concatenating strings
- prefer argument arrays in code instead of shell interpolation
- capture exit code, stdout, and stderr separately

Example Python wrapper:

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

## API Workflow Design

A direct API wrapper is often easier to test and reason about than a shell wrapper.

Sample implementation:

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

## CLI vs API Tradeoff Table

| Question | CLI | API |
| --- | --- | --- |
| Already installed and authenticated locally? | Strong | Depends |
| Easy to test in pure unit tests? | Weaker | Stronger |
| Best for CI shell automation? | Strong | Strong |
| Lowest custom code? | Strong | Medium |
| Most portable across environments? | Medium | Strong |
| Fine-grained error handling? | Medium | Strong |

## Worked Comparison

Scenario: "Run a retrieval evaluation job and upload results."

Use `CLI` when:

- the evaluation tool already exists as a stable command
- the job runs in a developer or CI environment
- the output can be captured in a predictable format

Use `API` when:

- the evaluation service is remote
- you need strong retry logic
- the result payload should be parsed as JSON

## Practical Rule

If your integration is local, short-lived, and already embodied in a trustworthy command, prefer CLI. If your integration is remote, narrow, and data-centric, prefer an API wrapper.

Next, read [Chapter 4](./04-delegation-and-agent-to-agent-handshakes.md) before introducing another agent into the system.

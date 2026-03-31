# Phase 04 Troubleshooting

Use this page when examples fail or the tool-choice logic feels fuzzy.

## `gh auth status` fails

Symptoms:

- `gh` says you are not logged in
- issue creation exits with auth errors

Fix:

```bash
gh auth login
gh auth status
```

If you are running in CI, use a non-interactive token flow instead of assuming a browser login.

## Shell command works manually but fails in code

Common causes:

- you built one long shell string instead of an argument array
- environment variables are missing in the subprocess
- the working directory is not what you expected

Safer pattern:

```python
subprocess.run(["gh", "issue", "list"], check=True)
```

## MCP tool is called with junk arguments

Causes:

- schema is too permissive
- description is vague
- required fields are missing

Fixes:

- set `additionalProperties` to `false`
- add `minLength`, `maxLength`, and bounded arrays
- tighten the tool description to one job only

## Delegation created more confusion than value

This usually means one of three things:

- the worker did not have clear ownership
- the handoff lacked success criteria
- the task should have stayed with one agent

Return to [Chapter 4](./chapters/04-delegation-and-agent-to-agent-handshakes.md) and rewrite the contract before trying again.

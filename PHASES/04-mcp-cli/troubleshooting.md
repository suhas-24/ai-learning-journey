# Phase 04 Troubleshooting

Use this page when a command, API call, or handoff does not behave the way you expected.

## `gh auth status` fails

What you may see:

- `gh` says you are not signed in
- issue creation fails with an auth error

What to try:

```bash
gh auth login
gh auth status
```

If you are in CI, use a token-based flow. Do not assume a browser login will exist there.

## A command works in the terminal but not in code

Common reasons:

- you built one long shell string instead of a list of arguments
- the subprocess is missing environment variables
- the working directory is wrong

Safer pattern:

```python
import subprocess

subprocess.run(["gh", "issue", "list"], check=True)
```

## MCP accepts the wrong inputs

Common reasons:

- the schema is too open
- the description is too vague
- the required fields are not strict enough

Fixes:

- reject extra fields
- add length limits
- keep the tool focused on one job

## Delegation caused more confusion than help

That usually means:

- the worker ownership was unclear
- the handoff did not say what success looked like
- the second agent was not actually needed

Go back to [Chapter 4](./chapters/04-delegation-and-agent-to-agent-handshakes.md) and make the handoff smaller and clearer.

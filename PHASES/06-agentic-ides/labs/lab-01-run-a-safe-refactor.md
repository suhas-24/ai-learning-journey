# Lab 1 - Run a Safe Refactor With an Agent

This lab is about using an agent carefully, not automatically. A `refactor` means changing how code is organized without changing what it does for the user.

## Goal

Use a coding agent to make one small refactor in a repository you already understand, then verify it yourself.

## Pick A Task

Choose something like:

- move duplicated parsing code into one helper
- rename a confusing function and update tests
- separate configuration loading from business logic

Do not try to redesign the whole system.

## Task Brief

Start with [../snippets/task-brief-template.md](../snippets/task-brief-template.md) and fill it in for your repo.

## Steps

1. let the agent inspect the relevant files
2. ask for a plan
3. approve only the bounded change
4. inspect the diff
5. run the checks
6. write down what the agent did well and what it missed

If the agent wants to widen the change, stop and re-state the small goal. `Bounded` here means the change stays small and clearly limited.

## Command Examples

```bash
git status --short
pytest tests/module_x -q
git diff -- src/module_x.py tests/test_module_x.py
```

## Deliverable

Write a session log using [../snippets/session-log-template.md](../snippets/session-log-template.md).

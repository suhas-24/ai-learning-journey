# Lab 1 - Run a Safe Refactor With an Agent

This lab teaches disciplined execution, not blind automation.

## Goal

Use a coding agent to make one bounded refactor in a repository you understand, then verify it properly.

## Pick a Task

Choose something like:

- extract duplicated parsing logic into a helper
- rename a confusing function and update tests
- separate configuration loading from business logic

Avoid architecture rewrites for this lab.

## Task Brief

Start with [../snippets/task-brief-template.md](../snippets/task-brief-template.md) and fill it in for your repo.

## Execution Steps

1. let the agent inspect the relevant files
2. ask for a plan
3. approve only the bounded change
4. inspect the diff
5. run the relevant checks
6. record what the agent got right and wrong

## Command Examples

```bash
git status --short
pytest tests/module_x -q
git diff -- src/module_x.py tests/test_module_x.py
```

## Deliverable

Write a session log using [../snippets/session-log-template.md](../snippets/session-log-template.md).

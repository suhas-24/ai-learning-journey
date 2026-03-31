# Chapter 3 - Checking The Result Safely

An agent output is only useful if it survives review.

A nice-looking diff is not proof. A confident summary is not proof either.

`Review` means looking at the changes with your own eyes. `Verification` means checking that the change really works.

If those words are new, think of it this way:

- review is reading the grocery list before you pay
- verification is checking that the food is actually in the bag when you get home
- a `diff` is the line-by-line view of what changed

The big idea is simple: do not trust a change just because a tool made it.

## The Review Loop

Use this loop for anything beyond a tiny edit:

1. inspect the plan
2. inspect the changed files
3. run the checks
4. read the logs or output
5. decide whether to accept, revise, or reject

## What To Look For

When you review an agent change, ask:

- Did it change files outside the request?
- Did it repeat logic that already exists?
- Did it invent commands or APIs that do not exist?
- Did it add tests that only fit the new code and not the real problem?
- Did it forget error handling?

## Three Kinds Of Verification

### Static verification

This means checking the code without running the whole system.

- linting
- type checks
- schema checks

### Behavioral verification

This means running the code and seeing what happens.

- unit tests
- integration tests
- snapshot checks

### Human reasoning

This means asking whether the result makes sense as a solution.

- does the design still fit the job?
- did the code match the request?
- would you trust this in review?

## Example

If an agent says it fixed retrieval ranking, you might run:

```bash
pytest tests/retrieval -q
python scripts/compare_rankers.py
git diff -- src/retrieval tests/retrieval
```

The point is not to run commands for decoration. The point is to check the code, the behavior, and the shape of the change.

If the tests pass but unrelated config changed, the result is still not acceptable.

## Red Flags

- the agent says `done` without naming checks
- the summary mentions tests but not the actual output
- the diff changes architecture without approval
- the agent touched files outside the brief

If one of these happens, pause and ask for a smaller, clearer fix. A slow correction is safer than a fast mistake.

Next: [Chapter 4](./04-multi-agent-coding-workflows.md).

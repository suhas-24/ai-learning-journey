# Chapter 3 - Checking The Result Safely

An agent output is only useful if it survives review.

A nice-looking diff is not proof. A confident summary is not proof either.

## The Review Loop

Use this loop for anything beyond a tiny edit:

1. inspect the plan
2. inspect the changed files
3. run the checks
4. read the logs or output
5. decide whether to accept, revise, or reject

## What To Look For

- changes in unrelated files
- duplicated logic instead of reuse
- invented commands or APIs
- tests that only fit the new code
- missing error handling

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

This means asking whether the result actually makes sense.

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

If the tests pass but unrelated config changed, the result is still not acceptable.

## Red Flags

- the agent says `done` without naming checks
- the summary mentions tests but not the actual output
- the diff changes architecture without approval
- the agent touched files outside the brief

Next: [Chapter 4](./04-multi-agent-coding-workflows.md).

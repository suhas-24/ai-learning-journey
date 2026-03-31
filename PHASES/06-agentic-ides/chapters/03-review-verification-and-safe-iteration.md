# Chapter 3 - Review, Verification, and Safe Iteration

Agent output is only useful when it survives verification. A clean-looking diff is not evidence.

## Review Loop

Use this loop for non-trivial changes:

1. inspect the plan
2. inspect the changed files
3. run the relevant checks
4. review logs or test output
5. decide whether to accept, revise, or reject

## What To Look For In Diffs

- scope creep into unrelated files
- duplicated logic instead of proper reuse
- invented APIs or flags
- fragile tests that only match the new implementation
- missing error handling around I/O or network calls

## Verification Layers

### Static verification

- linting
- type checks
- schema validation

### Behavioral verification

- unit tests
- integration tests
- golden file or snapshot comparisons

### Human reasoning

- does the architecture still make sense?
- does the code match the actual requirement?
- would you trust this in a code review?

## Worked Example

Agent claim: "I fixed retrieval ranking."

Verification:

```bash
pytest tests/retrieval -q
python scripts/compare_rankers.py
git diff -- src/retrieval tests/retrieval
```

If the tests pass but the diff quietly changed unrelated config, the work is still not acceptable.

## Red Flags

- the agent says "done" without mentioning checks
- commands are summarized but logs are absent
- the diff rewrites architecture with no prior approval
- the agent touched files outside ownership

Continue to [Chapter 4](./04-multi-agent-coding-workflows.md).

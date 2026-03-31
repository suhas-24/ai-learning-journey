# Observability, Traces, and Runtime Signals

Evaluation tells you whether a system is good on known cases. Observability tells you what happened during a real run.

You need both.

## First words

- `trace` means a step-by-step record of what the system did
- `signal` means a number or event that helps you notice a problem
- `dashboard` means a screen that shows those signals together
- a `token` is a small piece of text the model reads or writes
- a `node` is one step in a larger workflow
- a `validator` is a pass-or-fail check that looks for mistakes

## Why this matters

When something goes wrong in production, you need clues. Observability gives you those clues so you can stop guessing.

## What to log for each run

At minimum, record:

- run id
- prompt or policy version
- model name
- tool name and arguments summary
- latency
- token usage
- cost
- node transitions
- validator outcomes
- approval events

`Token usage` is the count of those pieces, which helps you estimate how much work a run did and how much it cost.

If the word token feels strange, just read it as "small text piece."

Other quick meanings:

- a `run id` is the label for one full attempt
- a `prompt version` is the exact wording of the instruction used for that run
- `node transitions` means the order of workflow steps the system moved through
- `validator outcomes` means which checks passed and which checks failed

## A useful trace shape

```json
{
  "run_id": "run_2026_04_11_004",
  "node": "validate_answer",
  "model": "gpt-5.4",
  "latency_ms": 1820,
  "input_tokens": 1440,
  "output_tokens": 330,
  "tool_calls": [],
  "validators": [
    {"name": "citation_check", "result": "failed"}
  ],
  "outcome": "reroute_to_retrieval"
}
```

More structure is available in [Trace Schema](../snippets/trace-schema.md).

## The runtime signals that matter most

Track these over time:

- task success rate
- cost per run
- latency percentiles
- retry rate
- validator failure rate
- approval frequency
- dead-letter rate

Plain-language definitions:

- `latency` means how long one run takes from start to finish
- a `percentile` helps you see how bad the slower runs are, not just the average
- `P95 latency` means 95 out of 100 runs finish faster than that number, while the slowest 5 runs take longer
- a `dead-letter rate` is the share of runs that fail so badly they get pushed into a holding area for manual inspection
- a `trace_id` is a shared label that lets you connect logs, tool calls, approvals, and validator results from the same run

Those definitions matter because a dashboard is only useful when you know what each number means.

Sample operational dashboard:

| Signal | Healthy range | Warning sign |
| --- | --- | --- |
| P95 latency | under 8s | rising after the instructions get much longer |
| Cost per run | under $1.20 | sudden spike after the system starts many branches at once |
| Validator failure rate | under 5% | jumps after the expected output format changes |
| Dead-letter rate | under 2% | most failures now happen in one workflow step |

## Failure case: no trace linkage

Scenario:

- user reports a bad answer
- logs show model calls but not which run they belong to
- approval record lives in a separate store with no shared id

Result:

- root cause analysis takes hours

Fix:

- propagate `run_id` and `trace_id` through every node, tool, validator, and approval record

## Practical rule

If an incident cannot be reconstructed from traces in 10 minutes, the observability layer is too weak.

Continue with [Regression Management and Failure Loops](./04-regression-management-and-failure-loops.md).

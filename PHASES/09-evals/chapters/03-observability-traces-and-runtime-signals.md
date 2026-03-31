# Observability, Traces, and Runtime Signals

Evaluation tells you whether a system is good on known cases. Observability tells you what happened during a real run.

You need both.

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

`Token` is a small piece of text that the model reads or writes. `Token usage` is the count of those pieces, which helps you estimate how much work a run did and how much it cost.

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

Sample operational dashboard:

| Signal | Healthy range | Warning sign |
| --- | --- | --- |
| P95 latency | under 8s | rising after prompt expansion |
| Cost per run | under $1.20 | sudden spike after parallel fan-out |
| Validator failure rate | under 5% | jumps after schema change |
| Dead-letter rate | under 2% | cluster on one node |

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

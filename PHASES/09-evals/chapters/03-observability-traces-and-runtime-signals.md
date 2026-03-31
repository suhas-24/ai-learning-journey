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

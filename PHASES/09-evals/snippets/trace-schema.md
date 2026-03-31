# Trace Schema

Use this shape to keep traces queryable and comparable.

This example shows the kind of record you want when you need to answer: what happened, when did it happen, and where did the problem start?

```json
{
  "trace_id": "trace_001",
  "run_id": "run_001",
  "node": "retrieve_docs",
  "kind": "tool_call",
  "started_at": "2026-04-11T10:00:00Z",
  "ended_at": "2026-04-11T10:00:02Z",
  "model": null,
  "tool": "search_docs",
  "input_tokens": 0,
  "output_tokens": 0,
  "latency_ms": 2000,
  "cost_usd": 0.03,
  "validator_results": [],
  "outcome": "success",
  "next_node": "summarize"
}
```

## Tips

- use the same `run_id` everywhere
- record both successes and failures
- keep trace fields machine-readable so dashboards and scripts can query them

Machine-readable just means another program can read the data without guessing.

Pair this with [Troubleshooting](../troubleshooting.md).

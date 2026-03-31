# Runtime Commands

These commands are examples of how an operator might inspect an orchestrated run.

They are not the workflow itself. They are the tools you use to look at the workflow after it has run.

## Find failed runs

```bash
jq 'select(.status=="failed")' runs/*.json
```

## Inspect budget usage

```bash
jq '{run_id, current_node, spent: .budget.spent_usd, limit: .budget.max_usd}' runs/run_001.json
```

## Count retry-heavy runs

```bash
jq 'select(.attempts.validate > 2)' runs/*.json
```

## Search logs for one run

```bash
rg "run_2026_04_07_001" logs/trace.log
```

These examples pair well with [Troubleshooting](../troubleshooting.md).

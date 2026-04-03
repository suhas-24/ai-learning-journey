# State Schema

Use this as a compact template for orchestrated runs.

This is the memory card for one run. Keep it small, clear, and easy to resume from.

If these field names are new:

- `run_id` is the unique name for one attempt
- `task_type` is the kind of job the workflow is doing
- `current_node` is the step that is running now
- `status` says whether the run is waiting, running, failed, or finished

```json
{
  "run_id": "string",
  "task_type": "string",
  "current_node": "string",
  "status": "queued|running|awaiting_human_approval|failed|completed",
  "completed_nodes": [],
  "attempts": {},
  "artifacts": {},
  "budget": {
    "max_usd": 0,
    "spent_usd": 0,
    "max_runtime_seconds": 0
  },
  "policy": {
    "approval_required": false,
    "max_model_escalations": 1
  },
  "approval": {
    "decision": null,
    "approved_by": null,
    "approved_at": null,
    "idempotency_key": null
  },
  "last_error": null,
  "last_checkpoint_at": null
}
```

## Why each field exists

- `current_node`: tells the harness where to resume
- `attempts`: stops infinite retry loops
- `artifacts`: points to external outputs without bloating state
- `budget`: allows policy checks before each expensive step
- `approval`: makes irreversible actions auditable

If a field does not help the system continue or recover, it probably belongs somewhere else.

Return to [README](../README.md).

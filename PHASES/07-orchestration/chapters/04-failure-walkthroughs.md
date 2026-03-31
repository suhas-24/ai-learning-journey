# Failure Walkthroughs

Reliable systems are designed by tracing failure paths before users discover them.

## Walkthrough 1: fan-out search causes budget spiral

### Scenario

The orchestrator launches eight parallel research workers because the query is broad. Each worker performs multiple retrieval calls and uses a large model for summarization.

### What failed

- no fan-out limit
- no per-worker budget
- no early stopping when source overlap became obvious

### Symptoms

- spend jumps from $0.40 to $4.70
- latency grows past the user SLA
- final answer contains duplicate sources

### Better design

```yaml
fan_out_policy:
  max_workers: 3
  max_search_calls_per_worker: 2
  stop_when:
    - source_overlap_over_70_percent
    - remaining_budget_below_0_30_usd
```

### Lesson

Parallelism without a budget policy is just a faster way to fail.

## Walkthrough 2: crash between approval and execution

### Scenario

The system asks a human to approve sending a summary email. Approval is granted. The process crashes before the email node runs.

### Unsafe design

- approval decision stored only in memory
- restart asks for approval again
- operator approves twice and worries about duplicate send

### Safe design

- approval stored as a durable event
- send node checks idempotency key before acting

Example:

```json
{
  "approval_id": "approve_8842",
  "approved_action": "send_summary_email",
  "idempotency_key": "email_run_2026_04_07_001"
}
```

### Lesson

Every irreversible action needs an idempotent boundary.

## Walkthrough 3: tool schema drift

### Scenario

A downstream API changes `title` to `headline`. The tool adapter is not updated.

### What happens without validation

- the writer node receives partial data
- the model hallucinates missing details
- the run looks successful but the answer is wrong

### Correct response

1. validate tool output at the boundary
2. fail fast with a typed error
3. route to fallback or escalation
4. create a regression test from the broken payload

## Runbook habit

For every major node, write down:

- most likely failure
- worst-case failure
- containment action
- recovery action
- signal you want in logs

This habit turns orchestration from abstraction into operations.

## Next step

Practice the design work in [Lab 01](../labs/01-design-an-orchestrator.md) and [Lab 02](../labs/02-add-retries-budgets-and-approvals.md).

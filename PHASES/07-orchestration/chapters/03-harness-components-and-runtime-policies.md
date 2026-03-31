# Harness Components and Runtime Policies

The harness is the operational shell around the model.

If the model is the part that writes the next sentence or picks the next action, the harness is the part that asks, "Should we do that, can we afford that, and what should happen if it fails?" It keeps the work safe, repeatable, and observable.

## The minimum viable harness

A production-worthy harness usually includes:

- planner or dispatcher
- state store
- retry policy
- timeout policy
- budget guard
- approval gate
- structured logs and traces
- dead-letter path for repeated failures

That sounds like a lot, but each piece solves one simple problem:

- who decides the next step
- where do we remember progress
- when do we try again
- when do we stop
- when do we ask a person
- how do we know what happened

## Where each piece fits

```mermaid
flowchart TD
    A["User Request"] --> B["Planner / Router"]
    B --> C["Execution Node"]
    C --> D{"Tool or Model Succeeded?"}
    D -->|Yes| E["Checkpoint State"]
    D -->|No, Transient| F["Retry Policy"]
    D -->|No, Unsafe or Repeated| G["Dead-Letter Queue / Escalation"]
    E --> H{"Needs Approval?"}
    H -->|Yes| I["Human Gate"]
    H -->|No| J["Next Node"]
    I --> J
```

## Retries

Not every error deserves another attempt.

Retry these:

- rate limits
- temporary network failures
- known flaky provider responses

Do not blindly retry these:

- invalid tool arguments
- schema mismatch caused by bad prompt design
- budget exhaustion
- approval rejection

Sample retry policy:

```yaml
retry_policy:
  max_attempts: 3
  backoff: exponential
  retry_on:
    - http_429
    - http_503
    - socket_timeout
  do_not_retry_on:
    - schema_validation_failed
    - permission_denied
    - budget_exceeded
```

## Budgets

Budgets keep the system from turning a small task into an expensive mystery. A budget is just a limit on time, money, or effort.

When a model processes text, its work is often counted by `tokens`, which are small pieces of text. You do not need to memorize the counting rule yet. For now, just remember that token count is one way to measure how much text the system read or wrote.

Track:

- total tokens
- tool cost
- elapsed time
- model tier used

Example budget scoreboard:

| Metric | Limit | Current | Action |
| --- | --- | --- | --- |
| Spend per run | $1.50 | $0.82 | continue |
| Wall clock time | 120s | 108s | warn |
| Search calls | 6 | 6 | stop fan-out |
| Model escalations | 1 | 1 | block further upgrades |

## Approval gates

Use approvals at irreversible boundaries, not everywhere.

Good approval triggers:

- sending an email
- mutating external data
- deleting files
- publishing to a customer-facing channel
- exceeding a financial threshold

Bad approval trigger:

- every low-risk read operation

Too many gates make the system unusable.

## Dead-letter handling

Repeated failure must land somewhere explicit.

Send runs to a dead-letter path when:

- retries are exhausted
- the same node fails with the same error signature
- policy rejects execution
- required human approval never arrives before timeout

Dead-letter record example:

```json
{
  "run_id": "run_2026_04_07_001",
  "failed_node": "validate_citations",
  "error_code": "schema_validation_failed",
  "attempt_count": 3,
  "budget_spent_usd": 0.91,
  "next_action": "manual_review"
}
```

## Failure containment checklist

- can the run be resumed safely
- can the operator tell what failed first
- can the system stop before wasting more budget
- can the same bug be reproduced from logs and artifacts

Continue with [Failure Walkthroughs](./04-failure-walkthroughs.md).

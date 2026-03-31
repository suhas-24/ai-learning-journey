# Policy, Approvals, and Least Privilege

Guardrails become real when the system knows not only what it can do, but also what it is forbidden to do without extra permission.

## Least privilege

Give each tool, worker, and role the minimum power required.

Examples:

- a researcher can read from the document index but cannot send email
- a summarizer can transform data but cannot mutate records
- a publisher can send externally but only after approval

This matters because prompt mistakes become less dangerous when the agent has less reach.

## Policy tiers

A useful pattern is to group actions by risk.

| Tier | Example action | Default behavior |
| --- | --- | --- |
| Low | read a public document | allow |
| Medium | query internal knowledge base | allow with logging |
| High | draft an outbound email | require validation and policy check |
| Critical | send email or delete data | require human approval |

## Approval design

An approval gate should answer:

- who can approve
- what exactly is being approved
- when approval expires
- whether the approved action is idempotent
- what gets recorded for audit

Example approval record:

```json
{
  "approval_id": "appr_2026_04_10_12",
  "action": "send_email",
  "approved_by": "ops_manager",
  "approved_at": "2026-04-10T08:41:00Z",
  "expires_at": "2026-04-10T09:11:00Z",
  "idempotency_key": "send_run_912"
}
```

## Safe execution environments

When the agent can run code or shell commands, isolation is non-negotiable.

Minimum controls:

- sandboxed runtime
- network restrictions where possible
- read-only mounts unless writes are required
- temporary credentials
- resource limits

## Failure case: overpowered helper tool

Scenario:

- a "document helper" tool accidentally has write access to the shared drive
- the model issues a cleanup instruction based on confusing input
- files are deleted

Root cause:

- permission design ignored least privilege

Fix:

- split read and write tools
- place write tools behind approval and path allowlists

## Policy as code

Keep policy explicit and reviewable.

```yaml
policies:
  send_email:
    requires_approval: true
    allowed_domains:
      - example.com
    max_recipients: 3
  delete_file:
    requires_approval: true
    allowed_paths:
      - /tmp/sandbox/
```

Continue with [Failure and Incident Walkthroughs](./04-failure-and-incident-walkthroughs.md).

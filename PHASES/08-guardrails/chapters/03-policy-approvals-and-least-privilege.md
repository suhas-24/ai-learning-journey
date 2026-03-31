# Policy, Approvals, and Least Privilege

Guardrails become real when the system knows not only what it can do, but also what it is forbidden to do without extra permission.

`Least privilege` means giving each part of the system only the power it truly needs. If a component only needs to read data, do not let it write or delete data too.

## First words

- `policy` means a rule about what is allowed
- `approval` means a human or trusted process says yes before an action happens
- `privilege` means power or permission
- `idempotency` means doing the same approved action twice should not create two side effects
- `isolation` means running risky work in a contained place so it cannot freely affect the rest of the system

## Why this matters

If one helper has too much power, one bad prompt can become a real incident. Least privilege keeps small mistakes small.

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

`Idempotency key` is a unique label that helps the system recognize "this exact action already happened" if it restarts or retries.

## Safe execution environments

When the agent can run code or shell commands, isolation is non-negotiable.

Minimum controls:

- sandboxed runtime
- network restrictions where possible
- read-only mounts unless writes are required
- temporary credentials
- resource limits

Plain-language meanings:

- a `sandboxed runtime` is a contained execution space for code
- `read-only mounts` mean files can be seen but not changed
- `temporary credentials` are short-lived secrets so stolen access does not last long
- `resource limits` cap things like memory, time, or CPU so one bad run cannot consume everything

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

A `path allowlist` is a short list of folders the tool is allowed to touch. If a path is not on the list, the tool should refuse the action.

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

This kind of file is useful because people can read it, test it, and review it before a mistake reaches production.

Continue with [Failure and Incident Walkthroughs](./04-failure-and-incident-walkthroughs.md).

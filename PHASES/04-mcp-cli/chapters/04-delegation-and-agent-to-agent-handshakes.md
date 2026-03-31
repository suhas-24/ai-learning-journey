# Chapter 4 - Delegation and Agent-to-Agent Handshakes

Many teams reach for multi-agent systems too early. A second agent is only justified when it owns something the first agent does not: different permissions, different context, or different specialization.

## When Delegation Is Worth It

Delegation makes sense when:

- one agent owns the codebase and another owns deployment policy
- one agent can parallelize a bounded research task
- one agent should verify or review another's work independently

Delegation is not worth it when:

- the main agent simply has an underspecified prompt
- both agents need the same full context anyway
- the task could be one tool call

## Handoff Contract

A good handoff includes:

- task objective
- owned files or owned systems
- success criteria
- forbidden actions
- expected return format

Example:

```json
{
  "objective": "Compare retrieval latency before and after reranking.",
  "owned_paths": ["evals/", "reports/retrieval/"],
  "must_not_touch": ["src/production/"],
  "deliverables": ["report.md", "latency-table.csv"],
  "return_format": "brief summary with findings and next actions"
}
```

## Designing a Reviewer Agent

One useful A2A pattern is `builder -> reviewer`.

- builder agent changes files and runs tests
- reviewer agent only inspects diffs, logs, and failure risks

That separation reduces self-confirmation bias.

## Failure Modes

### Context leakage

If a worker needs the whole repository, the split is probably weak.

### Ownership ambiguity

If two agents can both edit the same file, collisions are likely.

### Handoff without verification

Never treat another agent's summary as evidence. Require artifacts, logs, or diffs.

## Decision Checklist

Before adding an agent, ask:

1. What capability is unique to the second agent?
2. Can the task be split without shared writes?
3. What artifact proves completion?
4. Who validates the result?

## Next Action

Complete [Lab 1](../labs/lab-01-github-issue-three-ways.md) and explicitly note where delegation helped or did not help.

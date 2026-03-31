# Eval Plan - Enterprise Workflow Agent

## Eval Questions

- Does the agent complete the bounded workflow accurately?
- Does it ask for approval when it should?
- Does it fail safely when inputs are weak or risky?
- Can operators understand what happened after a run?

## Scenario Matrix

Test scenarios should include:

- normal valid request
- missing required evidence
- policy-violating request
- borderline approval case
- tool failure during execution
- operator rejection and retry

## Metrics

Track:

- workflow completion rate
- approval precision
- intervention rate
- latency
- cost per task
- audit log completeness

## Human Review

Have a reviewer score:

- correctness of proposed actions
- policy compliance
- clarity of escalation messages
- usefulness of logs and artifacts

## Success Criteria

- high-risk actions always require approval
- failed tasks leave enough evidence for review
- the system remains useful without overclaiming autonomy

## Demo Eval Guidance

In the demo, show:

- a normal successful task
- a policy-triggered approval
- a rejected or failed case
- the operator-facing audit trail

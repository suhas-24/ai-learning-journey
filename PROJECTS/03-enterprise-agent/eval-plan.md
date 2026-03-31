# Eval Plan - Enterprise Workflow Agent

This eval plan checks quality, safety, and operator trust.

Here, an `operator` is the person who watches or manages the system, and `trust` means they can understand what happened and rely on the controls.

Quick meanings:

- `operator trust` means a human reviewer feels the system is understandable and safe enough to rely on
- `approval precision` asks whether the system requests approval for the right cases instead of too many or too few
- `audit log completeness` asks whether the record contains enough detail to reconstruct what happened
- `autonomy` means how much the system does on its own without a human step

## Questions To Answer

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

## Metrics To Track

Measure:

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

## Success Looks Like

You should be able to show that:

- high-risk actions always require approval
- failed tasks leave enough evidence for review
- the system remains useful without overclaiming autonomy

## Demo Guidance

Show:

- a normal successful task
- a policy-triggered approval
- a rejected or failed case
- the operator-facing audit trail

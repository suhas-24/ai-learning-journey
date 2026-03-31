# Eval Plan - Multi-Agent Research Harness

This eval plan checks more than success.

It checks whether the harness works safely, recovers cleanly, and leaves enough evidence to understand what happened.

Quick meanings:

- a `scenario` is one repeatable test situation
- an `intervention` is a moment when a human needs to step in
- a `final artifact` is the saved result of the run, such as a report or summary

## Questions To Answer

- Can the harness complete complex tasks reliably?
- Can it recover from interruption?
- Are approvals triggered at the right moments?
- Are failures explainable after the fact?

## Scenario Suite

Create 10 to 20 scenario tests such as:

- research a topic and produce a cited summary
- hit a tool failure and retry
- exceed budget and stop cleanly
- pause midway and resume
- escalate when confidence drops

## Metrics To Track

Measure:

- task completion rate
- successful resume rate
- tool-call success rate
- average number of retries
- unnecessary human interventions
- time to final artifact

## Qualitative Review

Read the runs and check:

- whether handoffs make sense
- whether Analyst catches weak evidence
- whether Reporter states uncertainty honestly
- whether approval prompts are understandable

## Success Looks Like

You should be able to show that:

- resume works in most tested interruption cases
- risky actions consistently trigger approval
- run summaries are detailed enough to debug failures

## Demo Guidance

Show one scenario with:

- normal progress
- an induced fault
- recovery or escalation
- the final report plus trace evidence

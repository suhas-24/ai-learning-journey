# Eval Plan - Multi-Agent Research Harness

An eval plan answers a simple question: did the harness do the whole job safely and recoverably, or did it only look good in one demo?

## Eval Questions

- Can the harness complete complex tasks reliably?
- Can it recover from interruption?
- Are approvals triggered at the right moments?
- Are failures explainable after the fact?

## Scenario Suite

Create 10 to 20 scenario-based tests such as:

- research a topic and produce a cited summary
- hit a tool failure and retry
- exceed budget and stop cleanly
- pause midway and resume
- escalate when confidence drops

## Metrics

Track:

- task completion rate
- successful resume rate
- tool-call success rate
- average number of retries
- unnecessary human interventions
- time to final artifact

## Qualitative Review

Review:

- handoff quality between roles
- whether Analyst catches weak evidence
- whether Reporter reflects uncertainty honestly
- whether approval gates are understandable

## Success Criteria

- resume works in most tested interruption cases
- risky actions consistently trigger approval
- run summaries provide enough detail to debug failures

## Demo Eval Guidance

During the demo, show one scenario with:

- normal progress
- an induced fault
- recovery or escalation
- the final report plus trace evidence

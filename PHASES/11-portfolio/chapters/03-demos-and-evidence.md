# Chapter 3 - Demos And Evidence

A demo should confirm your engineering work, not hide missing rigor behind a happy path.

Here are the words we need first:

- a `demo` is a short walkthrough that shows the system working
- `evidence` is proof a reviewer can inspect
- a `trace` is a record of what the system did step by step

## What A Good Demo Shows

A strong technical demo includes:

- the real input
- what the system does step by step
- where the outputs come from
- one metric or eval artifact
- one failure boundary or safety check

Show both capability and control.

## Demo Structure

Use this order:

1. Problem and user goal
2. Architecture sketch
3. Live or recorded walkthrough
4. Eval summary
5. Known limitations and next step

Keep it short. Five focused minutes beats fifteen wandering minutes.

## Evidence Types That Matter

- screenshots of traces or logs
- sample eval tables
- confusion matrix or scorecard
- architecture diagram
- test cases
- example failures with explanation

## What To Avoid

- silent screen recordings with no context
- only showing successful cases
- hiding cost, latency, or quality tradeoffs
- claiming production readiness without proof

## Demo Script Skeleton

See [snippets/demo-script-template.md](../snippets/demo-script-template.md) and adapt it per project.

## Chapter Exercise

Record a draft demo for one project. Then review it and answer:

- Did I explain why this system exists?
- Did I show one real metric?
- Did I show one limitation honestly?

If any answer is no, record it again.

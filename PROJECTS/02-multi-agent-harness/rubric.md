# Rubric - Multi-Agent Research Harness

Use this rubric to check whether the design is controlled instead of merely complicated.

Here, `autonomy` means how much the system does on its own without waiting for a person.

If `bounded` feels fuzzy, it means the system is allowed to act, but only inside a narrow and clearly defined limit.

Score each area from 1 to 5.

## Role Design

- 1: multiple agents, but no clear responsibilities
- 3: role boundaries exist
- 5: boundaries, handoffs, and isolation choices are justified

## Control Layer

- 1: mostly autonomous with weak safeguards
- 3: retries and approvals exist
- 5: the amount the system does on its own is clearly limited and testable

## Persistence

- 1: run state disappears on failure
- 3: basic resume works
- 5: checkpointing and recovery are dependable and documented

## Observability

- 1: hard to inspect runs
- 3: logs or traces exist
- 5: traces, events, and reports make debugging straightforward

## Communication

- 1: the project feels conceptual only
- 3: build and eval plans are clear
- 5: the repo presents a credible engineering harness with evidence

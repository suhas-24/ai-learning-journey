# Regression Management and Failure Loops

The most valuable eval habit is simple: every serious failure should have a path to becoming a permanent test.

## Evaluation-driven development loop

```text
define target -> add eval cases -> make change -> run evals -> inspect failures -> fix -> rerun
```

For AI systems, the loop expands:

```text
production failure -> classify failure -> add dataset case -> add trace label -> patch system -> rerun evals
```

## What should block a merge

Good merge-blocking signals:

- significant drop in task success rate
- major regression in safety refusal correctness
- increased dead-letter rate in a critical workflow
- schema validation failures introduced by a change

Signals that should warn but not always block:

- slight cost increase
- small latency regression on non-critical paths
- low-confidence judge disagreement

## Example release gate

```yaml
release_gate:
  min_task_success_rate: 0.90
  min_refusal_correctness: 0.98
  max_dead_letter_rate: 0.02
  max_schema_validation_failure_rate: 0.01
```

## Failure loop example

Incident:

- retrieved text included stale policy
- answer cited outdated onboarding rules

Good response:

1. preserve failing trace
2. label the failure as `stale_retrieval`
3. add a dataset case with the stale chunk
4. add metadata freshness checks or ranking improvements
5. rerun retrieval and answer evals

## Cross-phase integration

Use these links when fixing failures:

- orchestration bugs often start in [Phase 07](../07-orchestration/README.md)
- safety regressions often come from missing controls in [Phase 08](../08-guardrails/README.md)

## The real standard

A mature AI repo does not merely collect dashboards. It uses measurements to decide whether a change was safe, useful, and worth shipping.

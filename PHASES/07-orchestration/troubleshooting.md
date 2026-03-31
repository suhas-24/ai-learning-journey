# Troubleshooting

## Symptom: the agent keeps calling the same tool

Likely causes:

- no retry ceiling
- no state flag marking the step complete
- model prompt encourages more evidence without a stop rule

Fix:

- track attempts per node
- add a source sufficiency rule
- checkpoint successful tool outputs

## Symptom: runs restart from the beginning after a crash

Likely causes:

- checkpoints are missing
- checkpoints do not include `current_node`
- artifacts are written after state instead of before it

Fix:

- persist artifact first
- then update checkpoint
- test recovery by killing the process intentionally

## Symptom: operator cannot explain what happened

Likely causes:

- logs are unstructured
- run id is missing from events
- state and trace data are not linked

Fix:

- emit structured events with run id, node, outcome, latency, and cost
- store pointer fields from state to trace ids

## Symptom: orchestrator feels too complex

Likely causes:

- too many agents
- nodes split too finely
- topology chosen for novelty instead of need

Fix:

- collapse back to fewer roles
- merge adjacent deterministic steps
- re-read [Control Flow and Topologies](./chapters/01-control-flow-and-topologies.md)

Next phase connection:

- safety boundaries build on this runtime in [Phase 08 Guardrails](../08-guardrails/README.md)

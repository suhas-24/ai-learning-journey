# Troubleshooting

## Symptom: eval scores look strong, but users still complain

Likely causes:

- dataset is too easy
- production edge cases are not represented
- overall score hides subsystem failures

Fix:

- add failure-derived cases
- split reporting by task type and subsystem
- review a sample of real traces against the dataset

## Symptom: dashboards are full, but no one knows what to do

Likely causes:

- too many metrics and no thresholds
- signals are not tied to decisions
- traces lack enough context for diagnosis

Fix:

- define blocking and warning thresholds
- reduce dashboard noise to operationally useful signals
- require run ids and node outcomes everywhere

## Symptom: prompt changes cause mystery regressions

Likely causes:

- prompt versions are not tracked
- evals are not rerun on change
- failures are discussed informally but never captured

Fix:

- version prompts and policies
- rerun golden dataset cases before merge
- add failing production examples into the dataset

## Symptom: retrieval metrics are poor, but answer quality sometimes looks good

Likely causes:

- the model is compensating with prior knowledge
- retrieved context is noisy but partially sufficient

Fix:

- inspect faithfulness separately from relevance
- improve retrieval ranking before celebrating answer polish

Cross-phase reminder:

- many regressions originate upstream in [Phase 07](../07-orchestration/README.md) or [Phase 08](../08-guardrails/README.md)

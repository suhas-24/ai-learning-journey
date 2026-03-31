# Eval Scorecard Template

Use this page to compare a baseline model and a tuned model side by side. The goal is to make the decision easy to explain later.

## Run Metadata

- experiment:
- date:
- base model:
- tuning method:
- dataset version:

## Quantitative Results

| Metric | Baseline | Tuned | Delta |
| --- | --- | --- | --- |
| Accuracy |  |  |  |
| Macro F1 |  |  |  |
| Schema validity |  |  |  |
| Avg latency (ms) |  |  |  |
| Cost per 1k requests |  |  |  |

## Failure Clusters

- confusion between:
- formatting problems:
- low-confidence cases:
- out-of-domain behavior:

## Recommendation

- ship
- iterate
- abandon

## Why

Write 5 to 8 lines explaining the decision in engineering terms.

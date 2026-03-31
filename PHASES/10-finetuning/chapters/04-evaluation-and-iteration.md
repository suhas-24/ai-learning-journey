# Chapter 4 - Evaluation And Iteration

A tuned model is not "better" because the training loss went down. It is better only if it performs better than the baseline on the task you care about.

## Baselines First

Always compare at least:

- prompt-only baseline
- prompt plus validation or post-processing baseline, if relevant
- tuned model

If the task needs private or fresh knowledge, also compare a retrieval-augmented baseline.

## What To Measure

Choose metrics that match the task:

- classification: accuracy, macro F1, confusion matrix
- extraction: exact match, field-level precision and recall
- structured generation: schema validity and task-specific correctness
- summarization or rewriting: human rubric plus constrained checks

Avoid single-metric thinking. A tuned model that improves accuracy but breaks output format may still be worse in production.

## Error Analysis

After scoring, cluster failures:

- class confusion
- verbosity problems
- hallucinated fields
- formatting drift
- edge-case instability
- out-of-domain collapse

For each cluster, ask whether the issue comes from:

- data gap
- unclear policy
- underpowered model
- weak baseline design
- mismatch between training examples and real traffic

## Example Scorecard

Use a scorecard like the one in [snippets/eval-scorecard.md](../snippets/eval-scorecard.md).

```text
Baseline macro F1: 0.81
Tuned macro F1: 0.88
Baseline schema validity: 0.95
Tuned schema validity: 0.99
Most improved class: account_access
Worst remaining weakness: feature_request vs other boundary cases
```

## Iteration Loop

Use this loop after every run:

1. Compare held-out scores.
2. Inspect confusing examples manually.
3. Revise label policy if it was ambiguous.
4. Add targeted examples instead of random volume.
5. Re-run the smallest useful experiment.
6. Stop when marginal gains are no longer worth the maintenance cost.

## Production Readiness Questions

Before shipping a tuned model, ask:

- How will we version the dataset?
- How will we detect drift?
- What happens when the taxonomy changes?
- How much does retraining cost in time and money?
- Can we roll back quickly if quality drops?

Fine-tuning is not a one-time trick. It creates an ongoing asset that must be maintained.

## Final Experiment Memo Template

Your final memo should contain:

- task and business goal
- baseline setup
- data summary
- training configuration
- quantitative results
- qualitative failures
- cost estimate
- recommendation: ship, iterate, or abandon

That memo is often more valuable than the tuned checkpoint because it shows judgment.

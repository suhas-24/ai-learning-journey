# Chapter 4 - Evaluation And Iteration

A tuned model is not "better" because the training loss went down. It is better only if it performs better than the baseline on the task you care about.

Evaluation means checking the model against examples you did not train on. That is how you find out whether the improvement is real or just memorized.

The word `held-out` means "kept aside and not used for training."

## Baselines First

Always compare at least:

- prompt-only baseline
- prompt plus validation or post-processing baseline, if relevant
- tuned model

If the task needs private or fresh knowledge, also compare a retrieval-augmented baseline.

A baseline is the simple version you compare against. Without it, you do not know whether the training run actually helped.

## What To Measure

Choose metrics that match the task:

- classification: accuracy, macro F1, confusion matrix
- extraction: exact match, field-level precision and recall
- structured generation: schema validity and task-specific correctness
- summarization or rewriting: human rubric plus constrained checks

Accuracy means "how often was it right overall?" Macro F1 is a score that gives each class equal weight so one common class does not hide problems in smaller classes. Schema validity means "did the output follow the format we asked for?"

Avoid single-metric thinking. A tuned model that improves accuracy but breaks output format may still be worse in production.

This is why evaluation is about behavior, not just one score.

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

Error analysis is the part where you ask, "Why did it fail this way?" That question usually points to the real fix.

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

The scorecard is not just a report. It is a compact explanation of what improved and what still needs work.

## Iteration Loop

Use this loop after every run:

1. Compare held-out scores.
2. Inspect confusing examples manually.
3. Revise label policy if it was ambiguous.
4. Add targeted examples instead of random volume.
5. Re-run the smallest useful experiment.
6. Stop when marginal gains are no longer worth the maintenance cost.

Iteration is how you avoid both overconfident shipping and endless tuning.

## Production Readiness Questions

Before shipping a tuned model, ask:

- How will we version the dataset?
- How will we detect drift?
- What happens when the taxonomy changes?
- How much does retraining cost in time and money?
- Can we roll back quickly if quality drops?

Fine-tuning is not a one-time trick. It creates an ongoing asset that must be maintained.

That is why the "should we ship this?" question matters just as much as the training run itself.

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

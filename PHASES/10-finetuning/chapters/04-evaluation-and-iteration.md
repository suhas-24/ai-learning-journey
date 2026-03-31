# Chapter 4 - Evaluation And Iteration

A tuned model is not better just because the training loss went down.
It is better only if it performs better than the baseline on the task you care about.

Here are the words we need first:

- `evaluation` means checking a model on examples it did not train on
- `baseline` means the simple version you compare against
- `held-out` means kept aside and not used for training
- `metric` means the score you use to measure quality

## Baselines First

Always compare at least:

- a prompt-only baseline
- a prompt-plus-processing baseline, if you have one
- the tuned model

If the task needs fresh or private knowledge, compare a retrieval-based baseline too.

Without a baseline, you do not know whether the tuning run actually helped.

## What To Measure

Choose metrics that match the task:

- classification: accuracy, macro F1, confusion matrix
- extraction: exact match, field precision, field recall
- structured generation: schema validity and task correctness
- summarization or rewriting: human rubric plus format checks

Accuracy tells you how often the model was right overall.
Macro F1 gives each class equal weight so one common class does not hide problems in smaller classes.
Schema validity tells you whether the output followed the format you asked for.

## Error Analysis

After scoring, group the failures:

- confusion between two labels
- formatting problems
- missing fields
- overly long answers
- edge cases that break the policy
- out-of-domain inputs

For each group, ask what the real fix is:

- better data
- clearer policy
- stronger baseline
- smaller task scope
- a different model choice

Error analysis is where you ask, "Why did it fail this way?"

## Example Scorecard

Use a scorecard like the one in [snippets/eval-scorecard.md](../snippets/eval-scorecard.md).

```text
Baseline macro F1: 0.81
Tuned macro F1: 0.88
Baseline schema validity: 0.95
Tuned schema validity: 0.99
Most improved class: account_access
Worst remaining weakness: feature_request vs other
```

The scorecard should make the decision easy to explain later.

## Iteration Loop

Use this loop after every run:

1. Compare held-out scores.
2. Read the confusing examples.
3. Fix the label policy if it was unclear.
4. Add targeted examples instead of random volume.
5. Re-run the smallest useful experiment.
6. Stop when the improvement is no longer worth the maintenance cost.

## Production Readiness Questions

Before shipping a tuned model, ask:

- how will we version the dataset
- how will we detect drift
- what happens when the label set changes
- how much will retraining cost
- can we roll back quickly

Fine-tuning creates an ongoing asset, not a one-time trick.

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

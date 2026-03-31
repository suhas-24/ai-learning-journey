# Fine-Tuning Troubleshooting

When something goes wrong, first name the broken part:

- the task
- the data
- the training setup
- the evaluation

That keeps the fix focused.

## Symptom: Training Loss Improves But Test Results Do Not

Likely causes:

- too many repetitive examples
- test data too different from train data
- the baseline prompt was already strong

What to do:

- inspect hard examples by hand
- remove duplicate examples
- clarify the label policy
- add boundary cases

## Symptom: Output Format Breaks After Tuning

Likely causes:

- inconsistent answers in the training data
- schema not reinforced in every example
- eval prompt different from training style

What to do:

- normalize the answer format
- add more schema-faithful examples
- add validation after generation

## Symptom: One Class Dominates Predictions

Likely causes:

- class imbalance
- weak class definitions
- biased data collection

What to do:

- review class counts
- tighten the label definitions
- add more examples for the confused classes

## Symptom: The Demo Looks Better But Scores Worse

Likely causes:

- cherry-picked examples
- the metric does not match the demo flow
- a good-looking demo hides systematic errors

What to do:

- trust the held-out set first
- expand the gold set
- write down why the metric and demo disagree

## Symptom: The Pipeline Keeps Breaking

Likely causes:

- malformed JSONL
- sequence length too high
- tokenizer, base model, or adapter mismatch

What to do:

- validate the data line by line
- run a tiny smoke test first
- save the config for every run

## Recovery Rule

When a run fails, do not change five things at once.
Change one thing, rerun the smallest useful experiment, and write down why.

Small changes are easier to understand than big messy ones.

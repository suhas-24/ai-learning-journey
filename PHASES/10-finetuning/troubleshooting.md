# Fine-Tuning Troubleshooting

## Symptom: Training Loss Improves But Test Results Do Not

Likely causes:

- overfitting to repetitive examples
- evaluation set too different from training data
- baseline prompt is stronger than the dataset policy

What to do:

- inspect hard examples manually
- reduce duplicate examples
- improve label policy clarity
- add targeted boundary cases

## Symptom: Output Format Breaks After Tuning

Likely causes:

- assistant outputs were inconsistent in training data
- schema was not reinforced in every example
- eval prompt differs from training style

What to do:

- normalize answer format in the dataset
- add validation checks to post-processing
- include more examples that emphasize schema compliance

## Symptom: One Class Dominates Predictions

Likely causes:

- class imbalance
- vague class boundary
- baseline data collection bias

What to do:

- review class counts
- tighten label definitions
- add high-quality examples for confused classes

## Symptom: The Tuned Model Feels Better In Demo But Scores Worse

Likely causes:

- easy cherry-picked examples
- score metric does not match the demo scenario
- qualitative impressions masking systematic errors

What to do:

- trust the held-out set first
- expand the gold set with business-critical examples
- document why the metric and demo diverge

## Symptom: Training Pipeline Keeps Breaking

Likely causes:

- malformed JSONL
- sequence length too high
- environment mismatch between tokenizer, base model, and adapter setup

What to do:

- validate data line by line
- run a tiny smoke test before the full job
- save config files for every run

## Recovery Rule

When a run fails, do not immediately change five variables. Change one variable, rerun the smallest useful experiment, and log the reason.

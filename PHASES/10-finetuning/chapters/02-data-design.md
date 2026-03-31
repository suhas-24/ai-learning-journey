# Chapter 2 - Data Design

Most tuning failures are data failures wearing a model hat.

Before you collect anything, here is the simplest way to think about the moving parts:

- a dataset is a set of examples the model learns from
- a label is the answer you want the model to produce
- train data teaches the model
- validation data helps you adjust the experiment
- test data is kept aside for the final check

If you see `JSONL`, it means "JSON lines": one JSON object per line in a text file.

## The Dataset Is The Product

When you fine-tune, you are not only training a model. You are encoding a policy. Every inconsistency in the dataset becomes an inconsistency the model may learn confidently.

That is why dataset work comes before training code.

If the examples are sloppy, the model learns sloppy habits. If the examples are clear, consistent, and realistic, the model has a much better chance of learning the right pattern.

## Build A Label Policy First

Your label policy should answer:

- what counts as a positive example
- what counts as a negative example
- how to handle ambiguous cases
- how to label borderline inputs
- when a human should abstain instead of guessing

For the support routing example, a weak label policy says "route tickets to the right team." A strong policy defines each class with inclusion and exclusion rules.

Inclusion rules explain what belongs in a label. Exclusion rules explain what does not belong there.

## Dataset Splits

Use three splits:

- train: used for learning
- validation: used while tuning
- test: used only for final comparison

The test set must stay untouched. Do not relabel it after peeking at errors unless you are fixing a true annotation mistake and documenting the change.

This separation matters because you want one honest final check. If you keep changing the test set, the final score stops being trustworthy.

## Example Format

Many supervised fine-tuning pipelines use instruction-style JSONL. A simple example:

```json
{"messages":[
  {"role":"system","content":"You classify support tickets into one of: billing, product_bug, account_access, feature_request, other. Return JSON only."},
  {"role":"user","content":"I was charged twice for my monthly plan after upgrading yesterday."},
  {"role":"assistant","content":"{\"label\":\"billing\",\"reason\":\"duplicate charge after upgrade\"}"}
]}
```

Good examples are:

- realistic
- internally consistent
- close to production inputs
- balanced across easy and hard cases

If you are new to tokenization, remember this simple idea: the model reads your examples after they have been split into small pieces called tokens. That is why example length and wording matter.

## Coverage Matters More Than Volume

A dataset with 500 carefully chosen examples often beats 5,000 lazy examples.

Make sure your dataset covers:

- obvious examples
- ambiguous phrasing
- short inputs
- long noisy inputs
- typo-heavy user language
- class boundary cases
- adversarial or misleading wording

The goal is not to make the data look beautiful. The goal is to make it honest.

## Common Data Mistakes

- duplicate near-identical examples
- synthetic data that does not resemble real traffic
- labels written by multiple people with no policy
- hidden leakage from eval into train
- over-cleaning user inputs until they no longer resemble production

## Data Audit Checklist

Before training, ask:

1. Can a human reviewer explain every label?
2. Are class counts wildly imbalanced?
3. Do we have enough hard examples?
4. Are train and test examples clearly separated?
5. Does the assistant output format exactly match production needs?

If a human cannot explain the label policy, the model probably will not learn it cleanly either.

## Minimal Audit Script

Even without a full pipeline, you can check label distribution:

```python
import json
from collections import Counter

counter = Counter()
with open("train.jsonl") as f:
    for line in f:
        row = json.loads(line)
        answer = row["messages"][-1]["content"]
        counter[answer] += 1

print(counter)
```

The point is not just counting labels. The point is discovering bad data before paying to train on it.

This is a little like checking ingredients before cooking. Bad ingredients usually lead to a bad meal.

## Gold Set Design

Create a small gold set of difficult examples that you review manually every time:

- 10 obvious examples
- 10 boundary examples
- 10 historically confusing examples
- 10 business-critical examples

This becomes your sanity set across all experiments.

The gold set is the small set of examples you trust most. It helps you see whether the model really improved on the tricky cases.

## Chapter Exercise

Using [snippets/support-routing-train.jsonl](../snippets/support-routing-train.jsonl), write down:

- what the label policy probably is
- which classes look underrepresented
- one example you would add to catch a boundary case

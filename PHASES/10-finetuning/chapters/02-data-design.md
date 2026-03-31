# Chapter 2 - Data Design

Most tuning problems are really data problems.

This chapter starts with the basic words:

- a `dataset` is a group of examples stored together
- an `example` is one input and one correct answer
- a `label` is the answer you want the model to choose
- `train data` is used to teach the model
- `validation data` is used while you are choosing settings
- `test data` is kept aside for the final check

If you see `JSONL`, it means one JSON object per line in a text file.

## Why Data Comes First

Fine-tuning does not create a new policy out of nowhere.
It teaches the model the pattern in your examples.

If the examples are sloppy, the model learns sloppy habits.
If the examples are clear, consistent, and realistic, the model has a better chance of learning the right pattern.

## Build The Label Policy First

Before you write the dataset, write the label policy.

That policy should answer:

- what each label means
- what does not belong in each label
- what to do with ambiguous cases
- when a human should abstain instead of guessing

For support routing, a strong policy says exactly when to use `billing`, `account_access`, `product_bug`, `feature_request`, or `other`.

## Train, Validation, Test

Use three splits:

- train: examples the model learns from
- validation: examples you use while tuning
- test: examples you never touch until the end

The test set must stay separate. If you keep peeking at it and changing things, the final score stops being honest.

## A Simple Example Format

Many fine-tuning pipelines use instruction-style JSONL:

```json
{"messages":[
  {"role":"system","content":"Classify support tickets into billing, product_bug, account_access, feature_request, or other. Return JSON only."},
  {"role":"user","content":"I was charged twice after upgrading my plan."},
  {"role":"assistant","content":"{\"label\":\"billing\",\"reason\":\"duplicate charge after upgrade\"}"}
]}
```

Why this matters:

- the input looks like the real task
- the answer follows one fixed format
- the label is easy to check

## Coverage Matters More Than Volume

A dataset with 200 careful examples often beats 2,000 careless ones.

Make sure your data includes:

- obvious cases
- boundary cases
- short messages
- long noisy messages
- typo-heavy examples
- confusing wording
- cases that are hard to label

The goal is not pretty data. The goal is honest data.

## Common Data Mistakes

- duplicate examples
- labels that mean different things to different people
- synthetic examples that do not look like real traffic
- train and test leakage
- over-cleaning the input until it no longer feels real

## Data Audit Checklist

Before training, check:

1. Can a human explain every label?
2. Are the classes balanced enough to learn from?
3. Do we have enough difficult examples?
4. Are train and test separate?
5. Does the answer format match the production need?

If a human cannot explain the labels, the model will not learn them cleanly either.

## Gold Set Design

Create a small gold set of hard examples that you review every time:

- obvious examples
- boundary examples
- historically confusing examples
- business-critical examples

This gold set helps you see whether the model really improved on the tricky cases.

## Chapter Exercise

Using [snippets/support-routing-train.jsonl](../snippets/support-routing-train.jsonl), write down:

- what the label policy appears to be
- which labels look overrepresented or underrepresented
- one hard example you would add
- one rule you would clarify

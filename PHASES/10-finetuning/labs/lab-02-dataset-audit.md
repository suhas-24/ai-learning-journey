# Lab 2 - Dataset Audit

This lab exists because most model improvements are blocked by dataset clarity, not optimizer magic.

An audit is just a careful check before you spend time and money training.

## Goal

Audit a candidate fine-tuning dataset before any training run.

## Inputs

- a train split
- a validation split
- a fixed label policy
- 10 to 20 examples that you suspect are difficult

## Audit Procedure

### 1. Check Label Consistency

Read 25 random examples and ask:

- would two reviewers choose the same label?
- does the answer format match production needs?
- are there labels that feel overloaded?

### 2. Check Distribution

Count examples per class. If one class dominates, decide whether that reflects real traffic or lazy collection.

### 3. Check Boundary Cases

Find examples that could plausibly belong to multiple classes. These are the examples that teach the model the policy boundary.

### 4. Check Leakage

Make sure no examples from the test set or gold set leaked into training.

### 5. Check Realism

Confirm the inputs still look like production data:

- typos
- shorthand
- missing context
- inconsistent formatting

If every example looks too clean, your model may overfit to a fantasy version of the task.

## Output Template

```text
Dataset version:
Reviewer:
Task:

Strengths:
- ...

Risks:
- ...

Immediate fixes:
- ...

Do not train until:
- ...
```

## Pass Condition

You are allowed to move on only when:

- the label policy is explicit
- the distribution is understood
- the hard examples are intentional
- the test set is protected

If you can explain why the data is trustworthy, the rest of the experiment becomes much easier to believe.

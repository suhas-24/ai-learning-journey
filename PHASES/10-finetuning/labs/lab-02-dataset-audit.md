# Lab 2 - Dataset Audit

This lab exists because dataset clarity usually matters more than optimizer tricks.

An `audit` is a careful check before you spend time and money training.

## Goal

Inspect a candidate fine-tuning dataset before any training run.

## Inputs

- a train split
- a validation split
- a label policy
- 10 to 20 examples that seem difficult

## Audit Procedure

### 1. Check Label Consistency

Read 25 random examples and ask:

- would two reviewers choose the same label
- does the answer format match the goal
- are any labels overloaded

### 2. Check Distribution

Count examples per class.
If one class dominates, decide whether that reflects real traffic or lazy collection.

### 3. Check Boundary Cases

Find examples that could belong to more than one class.
These are the examples that teach the model the policy boundary.

### 4. Check Leakage

Make sure no test examples leaked into train.

### 5. Check Realism

Confirm the inputs still look like real data:

- typos
- shorthand
- missing context
- inconsistent formatting

If every example looks too clean, the model may learn a fantasy version of the task.

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

You can move on only when:

- the label policy is explicit
- the distribution is understood
- the hard examples are intentional
- the test set is protected

If you can explain why the data is trustworthy, the rest of the experiment becomes easier to trust too.

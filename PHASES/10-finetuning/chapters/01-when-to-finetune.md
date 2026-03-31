# Chapter 1 - When To Fine-Tune

This chapter answers three beginner questions:

- what is fine-tuning
- why would anyone use it
- when should you not use it

## First Principles

Here are the words we need first:

- a `model` is a program that learns patterns from examples
- a `base model` is the model before you customize it
- a `prompt` is the instruction you give at run time
- `retrieval` means finding outside information and adding it to the model's context
- `fine-tuning` means training the model again on your own examples so it learns a new default habit

## What Fine-Tuning Changes

Prompting changes the instructions.
Retrieval changes the information the model can see.
Fine-tuning changes the model's learned behavior.

That difference matters because each one solves a different problem.

- If the model is confused by the wording of the task, improve the prompt.
- If the model needs fresh facts, improve retrieval.
- If the model keeps making the same narrow mistake, fine-tuning may help.

## Good Reasons To Fine-Tune

Fine-tuning is worth considering when all of these are true:

- the task is narrow
- the task happens often
- the answer format is stable
- prompt-only results are still inconsistent
- you can collect good examples
- you can measure success honestly

Examples:

- support tickets sorted into fixed buckets
- contract fields pulled into a fixed form
- meeting notes rewritten into one company template
- documents labeled into a small set of categories

These work well because the job is repeated, the right answer is checkable, and the output does not change every day.

## Bad Reasons To Fine-Tune

Do not fine-tune just because:

- the model does not know recent facts
- you want the model to read a private document set
- your prompt is still messy
- your labels are inconsistent
- you do not know how to measure improvement

If the issue is fresh knowledge, use retrieval.
If the issue is unstable formatting, try better prompts and validation first.

## A Simple Decision Rule

Ask these questions in order:

1. Is the problem caused by unclear instructions?
2. Is the problem caused by weak examples?
3. Is the problem caused by missing source material?
4. Is the model still inconsistent after you fix the first three?

Only the last question points strongly toward fine-tuning.

## Worked Example: Support Routing

Suppose you want to route support tickets into five queues:

- billing
- product bug
- account access
- feature request
- other

You try a few prompt versions and still see the same mistakes:

- similar tickets bounce between `product bug` and `other`
- the model overuses `feature request`
- small wording changes cause different answers

This is a good fine-tuning candidate because:

- the task is narrow
- the labels are fixed
- examples can be reviewed by a human
- the output is short and easy to score

## What A Good Task Spec Looks Like

Write the task spec before collecting data:

```text
Task: classify incoming support tickets
Input: raw ticket text
Output: one label from a fixed set
Allowed labels: billing, product_bug, account_access, feature_request, other
Rule: choose the single best label
Success metric: macro F1 on a held-out test set
Business goal: reduce manual triage time
```

The spec is the promise you make before training. It keeps the work focused.

## Fine-Tuning Modes You Should Recognize

- supervised fine-tuning: learn from input and correct answer pairs
- instruction tuning: improve how well the model follows instructions
- preference tuning: learn from preferred answers and rejected answers
- LoRA: train a small set of adapter weights instead of the whole model
- QLoRA: use a smaller memory footprint so tuning is easier on limited hardware

You do not need the math to use these methods well. What matters is whether the method fits the task, the hardware, and the time you have.

## Chapter Exercise

Pick one task from your own work and write:

- the task in one sentence
- the exact output format
- the business reason it matters
- one reason not to fine-tune
- one baseline you would compare against

If that feels hard, the task is probably still too vague.

# Chapter 1 - When To Fine-Tune

The first advanced skill in fine-tuning is refusing to do it when it is the wrong tool.

## What Fine-Tuning Changes

Prompting changes instructions at runtime.
RAG changes what information is provided at runtime.
Fine-tuning changes the model's learned behavior so the model is more likely to produce a certain style, structure, or decision pattern even before long prompting.

That difference matters because it changes both capability and maintenance burden.

## Good Reasons To Fine-Tune

Fine-tuning becomes a serious option when all of the following are true:

- the task is narrow and repeated often
- the output format is stable
- prompt-only performance is inconsistent in ways that matter
- you can collect high-quality examples of the exact task
- you have a held-out evaluation set and a clear success metric

Examples:

- support ticket routing into a fixed taxonomy
- extracting contract fields into a strict schema
- rewriting messy meeting notes into a fixed team format
- classifying documents into internal workflow buckets

## Bad Reasons To Fine-Tune

Do not fine-tune because:

- the model lacks recent knowledge
- you want the model to read a private corpus
- prompts are messy and you have not cleaned them up
- your labels are inconsistent
- you do not yet know what "better" means

If the issue is knowledge freshness, use retrieval. If the issue is output structure, consider validation plus retries before training.

## Decision Framework

Ask these questions in order:

1. Is the failure due to unclear instructions?
2. Is the failure due to missing examples?
3. Is the failure due to missing source material?
4. Is the failure due to model behavior remaining inconsistent after 1 to 3 are fixed?

Only question 4 points strongly toward fine-tuning.

## Worked Example: Support Routing

Suppose you want to route incoming support tickets into one of five queues:

- billing
- product bug
- account access
- feature request
- other

You try three prompt versions and still see problems:

- similar tickets bounce between "product bug" and "other"
- the model overuses "feature request"
- wording changes cause unstable routing

This is a classic fine-tuning candidate because:

- the task is narrow
- the label set is fixed
- examples can be labeled consistently
- the output is short and easy to score

## What A Tuning-Worthy Spec Looks Like

Write the task spec before collecting data:

```text
Task: classify inbound support tickets
Input: raw ticket text
Output: one label from a fixed taxonomy
Rules:
- choose "billing" for invoices, charges, refunds, payment failure
- choose "account access" for login, password, MFA, locked account
- choose "product bug" for malfunction, crash, incorrect behavior
- choose "feature request" for desired future behavior
- choose "other" only if none of the above apply
Success metric: macro F1 on a held-out test set
Business goal: reduce manual triage time by 40 percent
```

Without this spec, your dataset and evaluation drift immediately.

## Fine-Tuning Modes You Should Recognize

- Supervised fine-tuning: learn from input-output pairs
- Instruction tuning: improve task-following on instruction-style examples
- Preference tuning: optimize toward preferred answers over rejected ones
- LoRA: train low-rank adapter weights instead of the full model
- QLoRA: pair quantization with LoRA to reduce memory needs

For most personal experimentation, start with supervised fine-tuning plus LoRA or a managed provider workflow. That path is easier to run, easier to repeat, and easier to reason about.

## Chapter Exercise

Take one use case from your own work and write:

- the task definition
- the fixed output format
- the business metric
- the baseline you would compare against
- one reason not to fine-tune

If you cannot do that in 10 minutes, keep refining the task before touching a training pipeline.

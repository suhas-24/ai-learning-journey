# Phase 10 - Fine-Tuning

**Status:** 🔴 Not Started  
**Started:** Not started yet  
**Completed:** Not completed yet  
**Estimated Duration:** 3-4 weeks

---

## Why This Phase Matters

Fine-tuning is optional for most projects, which is exactly why it needs disciplined study. It is easy to romanticize. The real question is not "Can I fine-tune a model?" but "Is fine-tuning the best answer to this problem after trying better context engineering, RAG, and few-shot prompting?"

This phase exists to teach judgment, not just technique.

---

## Concept Map

Fine-tuning changes the model itself, while prompting and RAG change what the model sees at runtime.

- prompting changes instructions
- RAG changes knowledge access
- fine-tuning changes behavior and prior tendency

That is why fine-tuning should be the last step in the ladder, not the first.

---

## Decision Ladder

1. improve context engineering
2. add or improve retrieval
3. try few-shot prompting
4. fine-tune only when consistency on a narrow task still matters enough to justify the cost
5. combine fine-tuning with RAG only when both behavior and knowledge need stronger control

---

## Core Ideas To Master

### Fine-Tuning Concepts

- supervised fine-tuning: teach the model with input-output pairs
- RLHF: human preference feedback that shapes behavior at scale
- DPO: a preference-learning alternative that avoids some RL complexity
- LoRA: adapt a small number of low-rank parameters instead of the whole model
- QLoRA: combine quantization and LoRA so larger models can be adapted on modest hardware
- instruction tuning: make the model follow a task's pattern more reliably
- adapter tuning: attach trainable modules instead of rewriting the whole network

### When Fine-Tuning Is Worth It

Fine-tuning is usually worth exploring when:

- the task is narrow and repeated often
- the output format must be highly consistent
- prompting alone still produces too much variation
- the data is stable enough to justify maintaining a training set

It is usually not worth it when:

- the problem needs fresh knowledge every week
- the main failure is retrieval, not behavior
- the organization cannot maintain data and evals over time
- the model is already "good enough" with prompt and context improvements

### Dataset Discipline

- task definition before data collection
- train and validation separation
- contamination avoidance
- consistent formatting
- clear evaluation targets
- coverage across easy, medium, and hard examples

### Data Quality Rules

- examples should reflect the real production task
- outputs should be consistent in voice and structure
- ambiguous labels should be resolved before training starts
- the evaluation set should stay untouched by training

If the dataset is sloppy, fine-tuning just makes the sloppiness more confident.

### Tooling

- HuggingFace PEFT
- Unsloth
- Axolotl
- platform APIs when I want the easiest managed route

---

## Phase Project: Narrow Task Fine-Tuning Experiment

**Project goal:** fine-tune a small model for one narrow task and compare it against a strong prompt baseline.  
**Planned repo:** dedicated Phase 10 experiment repo  
**Current project status:** planned, not started

### Good candidate tasks

- support ticket classification
- code review comment style normalization
- structured summarization in one strict format
- document labeling or routing
- response-style normalization for one internal workflow

### Experiment Design

The experiment should compare at least three things:

1. a prompt-only baseline
2. a retrieval-augmented baseline if facts matter
3. the fine-tuned model on the same held-out test set

That comparison is what turns tuning into evidence instead of belief.

### What the project must prove

- whether fine-tuning delivers a measurable quality improvement
- how expensive data creation really is
- whether the operational cost is justified compared with prompt engineering alone
- whether the tuned model improves enough to justify the ongoing maintenance cost

---

## Exit Criteria

- I can explain what fine-tuning changes and what it does not.
- I can create a clean training dataset with a validation split.
- I can compare tuned and untuned models using a real evaluation method.
- I can say honestly whether the experiment was worth the complexity.

---

## Common Traps To Avoid

- fine-tuning before exhausting easier options
- collecting too much mediocre data
- evaluating on examples that leaked into training
- assuming a tuned model automatically stays better in production
- treating a better benchmark score as automatic product value
- forgetting that the data pipeline becomes part of the system after tuning
- tuning for novelty instead of for a repeated task with real value

---

## Resources For This Phase

| Resource | Why it matters | How I should use it |
| --- | --- | --- |
| PEFT docs | Best entry point for efficient tuning | Focus on LoRA concepts first |
| Unsloth guides | Makes practical experimentation easier | Use for small-model experiments |
| Raschka's book | Strong mental model for model internals | Read selectively, not cover to cover |
| Provider fine-tuning docs | Practical managed options | Compare hosted ease with open-source flexibility |

---

## Questions I Want To Answer During This Phase

- What exact failure mode am I trying to fix with fine-tuning?
- How much labeled data would be enough for a meaningful experiment?
- Does the tuned model actually outperform a careful prompt plus retrieval baseline?
- What maintenance cost does tuning add over time?

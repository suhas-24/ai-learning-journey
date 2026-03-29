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

## Decision Ladder

1. improve context engineering
2. add or improve retrieval
3. try few-shot prompting
4. fine-tune only when consistency on a narrow task still matters enough to justify the cost
5. combine fine-tuning with RAG only when both behavior and knowledge need stronger control

---

## Core Ideas To Master

### Fine-Tuning Concepts

- supervised fine-tuning
- RLHF and why it matters conceptually even if I do not implement it
- DPO as a preference-learning alternative
- LoRA and QLoRA for efficient adaptation
- why narrow, high-quality examples beat huge sloppy datasets

### Dataset Discipline

- task definition before data collection
- train and validation separation
- contamination avoidance
- consistent formatting
- clear evaluation targets

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

### What the project must prove

- whether fine-tuning delivers a measurable quality improvement
- how expensive data creation really is
- whether the operational cost is justified compared with prompt engineering alone

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

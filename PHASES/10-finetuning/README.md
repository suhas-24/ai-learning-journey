# Phase 10 - Fine-Tuning

This phase answers a simple question: when should you teach a model a new habit instead of giving it better instructions?

Before we go further, here are the plain-English words we will use:

- a `model` is a program that turns input into output by using patterns it learned earlier
- a `base model` is the starting model before you customize it
- `training` means showing the model examples so it can adjust its internal settings
- an `example` is one input and one correct answer
- a `label` is the answer you want the model to choose
- `loss` is a score that tells you how far the model's answer is from the correct answer
- a `weight` is one of the internal settings the model uses when it makes a prediction
- `inference` means using the model after training to make a real prediction
- a `dataset` is a group of examples stored together

`Fine-tuning` means training a base model again on your own examples so it becomes more reliable on one narrow task. That is different from prompting, where you change the instructions at runtime, and different from retrieval, where you change what information the model can see at runtime.

The main lesson in this phase is not "train everything." The main lesson is "decide carefully whether training is the right fix."

## What This Phase Is Really About

If a model is missing facts, fine-tuning is usually not the answer.
If a model keeps making the same kind of mistake on the same narrow task, fine-tuning might help.

This phase teaches fine-tuning as an engineering decision. By the end, you should know how to:

- define a narrow task clearly
- prepare a clean dataset
- run a small tuning experiment
- compare the tuned model to a strong baseline
- decide whether the change was worth the cost

## Outcomes

By the end of this phase, you should be able to:

- explain the difference between prompting, retrieval, and fine-tuning
- write a task spec with one clear output format
- build train, validation, and test splits
- prepare a small supervised fine-tuning dataset
- choose between LoRA, QLoRA, or no fine-tuning, where LoRA-style methods train a small add-on part instead of changing the whole model
- evaluate a tuned model against the same baseline and held-out set
- write a short decision memo that names both gains and tradeoffs

## Prerequisites

You should already be comfortable with:

- Python scripts and virtual environments
- calling an LLM API and reading structured output
- basic retrieval and evaluation ideas from earlier phases
- command-line work, Git, and simple notes about experiments

If any of those terms feel fuzzy, that is okay. The chapters below restate them in simpler words before building on them.

## What You Will Build

You will run a small fine-tuning experiment for one narrow task, such as support routing, document labeling, or structured summarization.

The goal is not to train a giant model. The goal is to prove whether a tuned model is actually better than a careful prompt baseline on one useful job.

## Recommended Study Order

1. Read [chapters/01-when-to-finetune.md](./chapters/01-when-to-finetune.md).
2. Read [chapters/02-data-design.md](./chapters/02-data-design.md).
3. Read [chapters/03-training-strategies.md](./chapters/03-training-strategies.md).
4. Read [chapters/04-evaluation-and-iteration.md](./chapters/04-evaluation-and-iteration.md).
5. Complete the labs in order.
6. Finish [checkpoints.md](./checkpoints.md) and use [troubleshooting.md](./troubleshooting.md) when results look odd.

## Directory Map

```text
10-finetuning/
├── README.md
├── chapters/
│   ├── 01-when-to-finetune.md
│   ├── 02-data-design.md
│   ├── 03-training-strategies.md
│   └── 04-evaluation-and-iteration.md
├── labs/
│   ├── lab-01-baseline-vs-tuned.md
│   └── lab-02-dataset-audit.md
├── snippets/
│   ├── support-routing-train.jsonl
│   ├── lora-config.yaml
│   └── eval-scorecard.md
├── checkpoints.md
└── troubleshooting.md
```

## Mental Model

Use this ladder when you are tempted to fine-tune too early:

```text
bad output
  -> fix the task definition
  -> improve the prompt
  -> improve the examples
  -> improve retrieval or validation
  -> only then test fine-tuning
```

Fine-tuning changes what the model tends to do by default. It is not the right tool for adding fresh facts every day.

If the problem is missing knowledge, use retrieval.
If the problem is unstable behavior on one narrow task, tuning may help.

## Time Budget

- Week 1: choose the task and write the spec
- Week 2: collect and audit the dataset
- Week 3: run a small training experiment
- Week 4: evaluate, analyze errors, and decide what to do next

## Phase Deliverable

Write a short experiment report that answers:

1. What exact problem were you trying to fix?
2. What baseline did you compare against?
3. What data did you use, and how did you keep test data separate?
4. Where did the tuned model improve?
5. Where did it still fail?
6. Was the improvement worth the maintenance cost?

# Phase 10 - Fine-Tuning

Fine-tuning is the phase where you stop asking "Can I train a model?" and start asking "What failure mode am I fixing that prompting and retrieval did not fix?" If you cannot answer that question in one sentence, you are not ready to tune yet.

This phase teaches fine-tuning as an engineering decision, not a prestige move. By the end, you should be able to define a narrow task, assemble a clean dataset, run a small LoRA-style experiment, and decide with evidence whether the tuned model is actually better than a strong prompt baseline.

## Outcomes

By the end of this phase, you should be able to:

- explain the difference between prompt engineering, RAG, and fine-tuning in operational terms
- define a tuning-worthy task with stable labels and measurable outputs
- prepare supervised fine-tuning data in production-like formats
- choose between full fine-tuning, LoRA, QLoRA, or "do not fine-tune"
- evaluate tuned and untuned systems on the same held-out set
- write an honest experiment report that includes cost, quality, and maintenance tradeoffs

## Prerequisites

You should already be comfortable with:

- Python scripting and virtual environments
- calling LLM APIs and saving structured outputs
- retrieval and eval basics from earlier phases
- command-line workflows, Git, and simple experiment tracking

## What You Will Build

You will run a narrow-task fine-tuning experiment around a realistic business task such as support routing, document labeling, or structured summarization. The project in this phase is not "train a giant model." The project is "prove whether a tuned model beats a careful baseline on a task that matters."

## Recommended Study Order

1. Read [chapters/01-when-to-finetune.md](./chapters/01-when-to-finetune.md).
2. Read [chapters/02-data-design.md](./chapters/02-data-design.md).
3. Read [chapters/03-training-strategies.md](./chapters/03-training-strategies.md).
4. Read [chapters/04-evaluation-and-iteration.md](./chapters/04-evaluation-and-iteration.md).
5. Complete the labs in order.
6. Finish [checkpoints.md](./checkpoints.md) and use [troubleshooting.md](./troubleshooting.md) when results look suspicious.

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

Use this ladder every time you feel tempted to fine-tune:

```text
Bad output -> inspect task definition
          -> improve instructions
          -> improve examples
          -> improve retrieval/context
          -> add structured validation
          -> only then test fine-tuning
```

Fine-tuning is about changing the model's default behavior. It is not the right tool for giving the model fresh facts every day. If the failure comes from missing knowledge, fix retrieval. If the failure comes from inconsistent behavior on the same narrow task, tuning may help.

## Time Budget

- Week 1: task selection, baseline creation, label policy
- Week 2: dataset preparation and audit
- Week 3: first tuning run and held-out evaluation
- Week 4: error analysis, iteration, final decision memo

## Phase Deliverable

Write a short experiment report that answers:

1. What exact failure mode did you target?
2. What baseline did you compare against?
3. What data did you use, and how did you keep train and eval separate?
4. Where did the tuned model improve?
5. Where did it still fail?
6. Was the gain worth the maintenance cost?

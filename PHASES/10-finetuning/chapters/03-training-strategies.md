# Chapter 3 - Training Strategies

Once the task and dataset are stable, the next question is how much of the model you need to change.

Here are the words we need first:

- `training` means showing the model examples so it can adjust its behavior
- a `weight` is one of the model's internal settings
- `loss` is a score that measures how far the model's answer is from the correct answer
- `inference` means using the model after training to make predictions
- `quantization` means using a smaller numeric representation so the model uses less memory

## Full Fine-Tuning Versus LoRA

Full fine-tuning updates all model weights.
That can be expensive and memory-heavy.

LoRA, short for low-rank adaptation, trains a smaller set of `adapter` weights while keeping most of the base model frozen. An `adapter` is a small extra component added so you can teach a new habit without rewriting the whole model.

For a beginner, the key idea is simple:

- full fine-tuning changes a lot of the model
- LoRA changes a smaller add-on part of the model

## Why LoRA Matters

LoRA is popular because it often gives you a practical middle ground:

- lower memory use
- faster experiments
- easier swapping between task-specific adapters
- lower cost for narrow tasks

Think of the base model as a general machine and the LoRA adapter as a small extra part that teaches one new habit.

## When QLoRA Helps

QLoRA combines quantization with LoRA so the base model takes less memory.

Choose it when:

- your hardware is limited
- you want to try a larger base model
- a small loss in training precision is acceptable

QLoRA is a memory trick, not a magic quality trick. It helps you fit the experiment, but it does not fix bad data or a weak task spec.

## Training Pipeline Stages

1. Choose a base model.
2. Format train and validation data.
3. Tokenize the examples consistently.
4. Choose LoRA or full fine-tuning.
5. Train for a small number of passes.
6. Evaluate on validation and gold examples.
7. Save the adapter or tuned checkpoint.
8. Compare the tuned model with the baseline on held-out data.

`Tokenize` here means splitting text into the small pieces the model processes.

## Configuration Concepts

You should understand these knobs:

- batch size: how many examples are processed at one time
- learning rate: how quickly the model changes
- epochs: how many times the model sees the training data from start to finish
- sequence length: the maximum number of tokens in one example
- gradient accumulation: a way to simulate larger batches when memory is tight
- target modules: which parts of the model receive adapters

You do not need the math to use these settings well. You only need to know which ones affect memory, speed, and how quickly the model learns.

Example LoRA config:

```yaml
base_model: mistral-7b-instruct
method: lora
r: 16
alpha: 32
dropout: 0.05
target_modules:
  - q_proj
  - v_proj
learning_rate: 0.0002
epochs: 3
micro_batch_size: 4
gradient_accumulation_steps: 4
max_seq_length: 2048
```

See [snippets/lora-config.yaml](../snippets/lora-config.yaml) for the same idea in a commented file.

If names like `q_proj` and `v_proj` look strange, do not worry about the math yet. They are internal names for selected parts of the model where the adapters are attached.

## Start Small

Your first run should be intentionally small:

- a subset of the data
- a low epoch count
- one baseline
- one scorecard

The goal of the first run is not greatness. The goal is to prove the pipeline works.

## Managed Providers Versus Open Source

Managed provider fine-tuning:

- easier setup
- faster first result
- less control over the stack

Open-source local workflow:

- more control
- more setup and debugging
- deeper understanding of the pieces

There is no moral winner here. Pick the path that matches what you are trying to learn.

## What To Log Every Run

- base model
- dataset version
- split version
- config values
- runtime
- cost
- validation scores
- gold-set failures

Here, a `checkpoint` is a saved version of the tuned model at one moment in training.

If you cannot reconstruct what changed between runs, you are not doing experiments. You are guessing.

## Chapter Exercise

Write a one-page run sheet for your first experiment:

- chosen base model
- why you chose LoRA or QLoRA
- training budget
- expected failure mode
- exact comparison baseline

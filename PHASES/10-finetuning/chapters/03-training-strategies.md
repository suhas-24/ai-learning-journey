# Chapter 3 - Training Strategies

Once the task and dataset are stable, the next question is how much of the model you need to change.

At this point, "train" simply means "show the model lots of examples so it can adjust its behavior." The training method decides how much of the model changes and how expensive that change is.

## Full Fine-Tuning Versus Parameter-Efficient Tuning

Full fine-tuning updates all model weights. That is expensive, memory-heavy, and often unnecessary for narrow tasks.

Parameter-efficient methods such as LoRA train a much smaller set of weights while keeping the base model mostly frozen. This is why LoRA is the default starting point for many practical projects.

Think of model weights as learned settings inside the model. Full fine-tuning changes many of those settings. LoRA changes a smaller add-on set of settings.

## Why LoRA Matters

LoRA works by injecting small trainable matrices into selected layers. You do not need to derive the linear algebra to use it well, but you should know the operational effect:

- less memory usage
- faster experimentation
- easier swapping between task adapters
- lower cost for narrow-task experiments

For a beginner, the main point is simple: LoRA is a cheaper way to try a custom training idea without rebuilding the whole model.

## When QLoRA Helps

QLoRA quantizes the base model to reduce memory usage and then trains LoRA adapters on top. Choose it when:

- your hardware is limited
- you want to test a larger base model
- a small loss in training precision is acceptable

Avoid treating QLoRA as magic. It makes experiments more accessible, but it does not fix bad data or a bad task definition.

It is a memory trick, not a quality trick.

Quantization means using a smaller, more compact representation of the model so it uses less memory while it runs.

## Training Pipeline Stages

1. Choose a base model.
2. Format train and validation data.
3. Tokenize the dataset consistently.
4. Configure LoRA or full-tuning parameters.
5. Train for a small number of epochs.
6. Evaluate on validation and gold examples.
7. Save the adapter or tuned checkpoint.
8. Run held-out test comparisons against the baseline.

Tokenization appears here because the training tool needs to turn each example into tokens before the model can learn from it. Tokenization is just the step where text gets split into the small units the model processes.

## Configuration Concepts

You should understand these knobs:

- batch size: how many examples per update
- learning rate: how aggressively weights change
- epochs: how many passes through the training set
- sequence length: maximum token length per example
- gradient accumulation: simulates larger batches when memory is tight
- target modules: which model layers receive adapters

You do not need to become a math expert to use these settings. You only need to know which ones affect memory, speed, and how quickly the model learns.

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

See [snippets/lora-config.yaml](../snippets/lora-config.yaml) for a fuller version.

## Practical Rule: Start Small

Your first run should be intentionally small:

- subset of data
- low epoch count
- one baseline
- one held-out scorecard

The goal of run one is not excellence. It is pipeline proof. You want to verify that formatting, training, saving, loading, and evaluation all work before burning time on bigger runs.

Small runs are kinder to beginners because they make mistakes cheaper and easier to debug.

## Managed Providers Versus Open Source

Managed provider fine-tuning:

- easier setup
- faster path to first result
- less infrastructure control

Open-source local workflow:

- more control
- better understanding of the stack
- more setup and debugging burden

There is no moral winner here. Pick the path that matches what you are trying to learn.

If your learning goal is deep operational understanding, do at least one open workflow. If your product goal is speed, a managed workflow may be enough.

## What To Log Every Run

- base model
- dataset version
- split version
- config values
- wall-clock runtime
- cost
- validation scores
- gold-set failures

If you cannot reconstruct what changed between runs, you are not doing experiments. You are gambling.

Good experiment notes are a form of memory. They let future-you understand what happened without guessing.

## Chapter Exercise

Write a one-page run sheet for your first experiment:

- chosen base model
- why you chose LoRA or QLoRA
- training budget
- expected failure mode
- exact comparison baseline

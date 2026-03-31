# Model Internals And Finetuning

This guide is for the phase where you need to understand what is happening inside the model itself. The goal is not to become a researcher overnight. The goal is to stop treating model behavior as a black box.

If you are new to this, `fine-tuning` means teaching an already-trained model with extra examples so it behaves differently on a task. It is not the same as writing a better prompt. It changes the model's learned settings, which are often called `weights`.

## How To Use This Guide

- Start here when you want to understand why a model behaves the way it does.
- Read the book as a map of internal parts, not as a race to the end.
- Return to the concept list after each chapter and explain it in simple language.

## Build A Large Language Model (from Scratch) by Sebastian Raschka

### What this book teaches

This book explains the mechanics behind transformer-style models: how text becomes vectors, how attention mixes information, how optimization updates weights, and why training data shapes capability.

In plain English, the model reads text in small pieces, turns those pieces into numbers, mixes the numbers to decide what matters, and then predicts the next piece of text. Fine-tuning changes what the model tends to do by updating its learned numbers.

### Core topics and subtopics

- Neural building blocks: layers, activations, parameters, and representation learning.
- Token and embedding flow: how discrete text becomes continuous signals.
- Attention: how the model selects and combines contextual information.
- Transformer structure: blocks, residual paths, normalization, and stacking.
- Training loops: loss, gradients, optimization, and why training is expensive.
- Inference behavior: next-token prediction, decoding, and generation dynamics.
- Fine-tuning intuition: how modifying weights differs from steering with prompts.

### When to use it

- Best in Phase 10.
- Useful earlier only if retrieval, embeddings, or generation keep feeling mystical.

### What to extract

- Why embeddings carry meaning instead of just storing words.
- Why attention is a routing mechanism, not magic.
- Why data quality and task framing matter so much in fine-tuning.
- Why evaluation still matters after adaptation. A fine-tuned model can become better on one task while getting worse elsewhere.

### Watch for

- This book is easy to treat like pure theory. The useful habit is to keep asking how each internal idea changes a real product choice.

### Best companion resources

- [../people/model-builders-and-research-explainers.md](../people/model-builders-and-research-explainers.md)
- [../newsletters/technical-analysis-and-research-interpretation.md](../newsletters/technical-analysis-and-research-interpretation.md)
- [../by-phase.md](../by-phase.md)

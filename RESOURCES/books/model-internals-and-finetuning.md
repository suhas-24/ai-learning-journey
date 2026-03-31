# Model Internals And Finetuning

This guide is for the phase where you need to understand what is happening inside the model itself. The goal is not to become a researcher overnight. The goal is to stop treating model behavior as a black box.

## Build A Large Language Model (from Scratch) by Sebastian Raschka

### What this book teaches

This book teaches the mechanics behind transformer-style models: how text becomes vectors, how attention mixes information, how optimization updates weights, and why training data shapes capability.

### Major topics and subtopics

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

### Best companion resources

- [../people/model-builders-and-research-explainers.md](../people/model-builders-and-research-explainers.md)
- [../newsletters/technical-analysis-and-research-interpretation.md](../newsletters/technical-analysis-and-research-interpretation.md)
- [../by-phase.md](../by-phase.md)

## What To Extract From This Book

- Why embeddings carry meaning instead of just storing words.
- Why attention is a routing mechanism, not magic.
- Why data quality and task framing matter so much in fine-tuning.
- Why evaluation still matters after adaptation. A fine-tuned model can become better on one task while getting worse elsewhere.

## Warning For This Phase

Do not read model internals as an escape from product work. The point of this guide is to improve intuition for adaptation, evaluation, and tradeoffs, not to postpone shipping.

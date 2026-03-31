# ML Foundations And Systems Thinking

This guide covers the books that give you the vocabulary and judgment needed to understand model-based systems without hand-waving. These books matter because they make later phases less magical and more explainable.

## The Hundred-Page Machine Learning Book

### What this book teaches

This book teaches the shortest useful map of machine learning. It does not make you an ML researcher, but it gives you the language to understand training, evaluation, bias, generalization, and model error.

### Major topics and subtopics

- Supervised learning: inputs, labels, fitting, and prediction.
- Unsupervised learning: clustering, dimensionality reduction, and pattern discovery.
- Generalization: overfitting, underfitting, bias, variance, and why a model fails on new data.
- Evaluation basics: train-test splits, metrics, and interpretation mistakes.
- Practical intuition: why model quality depends on data, framing, and measurement.

### When to use it

- Best in Phase 1 as orientation.
- Useful again in Phase 2 when ML vocabulary shows up in API, embedding, and evaluation discussions.

### Best companion resources

- [../tools/python-foundation-tools.md](../tools/python-foundation-tools.md)
- [../by-phase.md](../by-phase.md)

## Designing Machine Learning Systems by Chip Huyen

### What this book teaches

This book teaches how ML systems fail after deployment and how a team designs around those failures. It is less about one model architecture and more about the system around the model.

### Major topics and subtopics

- Problem design: setting the right objective, constraints, and business framing.
- Data strategy: collection, labeling, quality control, and feedback loops.
- Training and validation: split design, metric choice, and hidden leakage risks.
- Deployment tradeoffs: online versus batch patterns, latency, cost, and rollback planning.
- Monitoring: drift, data quality, changing user behavior, and incident response.
- Iteration loops: how observations become new datasets, evals, and system changes.

### When to use it

- Best in Phase 9 for evaluation and observability.
- Useful in Phase 11 when you need to explain a project as an evolving system rather than a one-time demo.

### Best companion resources

- [../courses/evals-and-mlops-courses.md](../courses/evals-and-mlops-courses.md)
- [../tools/evals-observability-tools.md](../tools/evals-observability-tools.md)
- [../people/systems-thinkers.md](../people/systems-thinkers.md)

## How To Use These Books Well

- Learn the terms well enough to explain them without jargon.
- Rephrase each concept in the context of a project you are building.
- If a tool or framework tutorial starts making strong claims, use these books to ask better questions about data, evals, and failure modes.

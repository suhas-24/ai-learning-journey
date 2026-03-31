# Mental Models

These are the conceptual frames that make the whole curriculum easier to understand.

## Model Versus System

The model is not the product. The model is one component inside a larger system that decides:

- what the model sees
- what tools it can use
- what happens when it fails
- how its outputs are validated

## Prompt, Context, Harness

Think of the stack as three nested layers:

- prompt: the instruction itself
- context: all information currently visible to the model
- harness: the system around the model that manages decisions, state, retries, and control

## Retrieval Versus Fine-Tuning

Use retrieval when the knowledge changes. Use fine-tuning when the behavior needs to be more consistent. When both knowledge and behavior matter, the system may need both.

## Demo Versus Production

A demo proves the idea can work once. A production system proves it can work repeatedly, measurably, and safely.

## Code As External Memory

Notes, specs, logs, and tests are all forms of memory. Good engineering externalizes memory so the system is understandable a week later, not just today.

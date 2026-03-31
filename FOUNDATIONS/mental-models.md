# Mental Models

These are the conceptual frames that make the whole curriculum easier to understand.

## A Tiny First-Pass Picture

When you use an AI app, a few things happen in order:

1. You type a prompt.
2. The app turns your text into tokens.
3. The model reads those tokens along with any other context it was given.
4. The model predicts the next tokens.
5. The surrounding software may look things up, call tools, check rules, or ask for approval.
6. The app turns the result back into text you can read.

That is the simplest useful picture. The rest of the repo teaches each part in more detail.

## Model Versus System

The model is not the product. The model is one component inside a larger system that decides:

- what the model sees
- what tools it can use
- what happens when it fails
- how its outputs are validated

If the surrounding system is poor, even a strong model can behave poorly.

## Prompt, Context, Harness

Think of the stack as three nested layers:

- prompt: the instruction itself
- context: all information currently visible to the model
- harness: the software around the model that manages decisions, state, retries, and control

If the prompt is the question, the context is the surrounding facts, and the harness is the machinery that keeps the whole thing usable.

## Retrieval Versus Fine-Tuning

Use retrieval when the knowledge changes. Use fine-tuning when the behavior needs to be more consistent. When both knowledge and behavior matter, the system may need both.

In simpler words:

- retrieval = look something up when you need it
- fine-tuning = teach the model a new pattern through examples

## Demo Versus Production

A demo proves the idea can work once. A production system proves it can work repeatedly, measurably, and safely.

## Code As External Memory

Notes, specs, logs, and tests are all forms of memory. Good engineering externalizes memory so the system is understandable a week later, not just today.

That matters because people forget, but files can remember.

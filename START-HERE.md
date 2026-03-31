# Start Here

If you open this repository and feel overwhelmed, start on this page. The goal of this file is to turn the repository from a pile of notes into a guided study path.

## What This Repository Is

This repository is a self-paced AI engineering curriculum that is meant to do three things at the same time:

1. teach core concepts clearly
2. give you structured practice
3. turn your learning into public proof through real projects

It is not a certificate course, a random bookmark dump, or a chat transcript archive. It is a working study system.

## The First Words

If this is all new, start with these simple meanings:

- `LLM` means large language model. It is software trained on lots of text so it can predict and generate text.
- `token` means a small piece of text the model reads or writes.
- `tokenization` means breaking text into tokens so the model can process it.
- `context window` means the amount of text the model can see at one time.

You do not need to memorize those words immediately. You only need a safe starting point. The [FOUNDATIONS/glossary.md](./FOUNDATIONS/glossary.md) page explains them more slowly.

## The Fastest Way To Begin

1. Read [README.md](./README.md) for the high-level purpose of the repository.
2. Read [FOUNDATIONS/glossary.md](./FOUNDATIONS/glossary.md) if words like `LLM` or `token` are new to you.
3. Read [FOUNDATIONS/prerequisites.md](./FOUNDATIONS/prerequisites.md) to understand what you need before Phase 1.
4. Read [FOUNDATIONS/mental-models.md](./FOUNDATIONS/mental-models.md) so the later phases fit into one coherent map.
5. Read [LEARNING_PATH.md](./LEARNING_PATH.md) to see how the full curriculum unfolds.
6. Start with [PHASES/01-python/README.md](./PHASES/01-python/README.md).

## How To Study A Phase

Each phase should eventually contain the same teaching contract:

- `README.md`: what the phase is, why it matters, and how the pieces fit together
- `chapters/`: concept teaching in smaller units
- `labs/` or `exercises/`: guided practice
- `snippets/`: copyable code or command examples
- `checkpoints.md`: review questions and completion checks
- `troubleshooting.md`: common mistakes and how to recover from them

Use the phase in this order:

1. read the phase `README.md`
2. work through the `chapters/` in order
3. run the `labs/` or `exercises/`
4. steal and adapt the `snippets/`
5. answer the `checkpoints.md`
6. use `troubleshooting.md` when you get stuck

## What To Do Every Week

- choose one concept to understand deeply
- build one small thing that uses it
- record what worked in [WINS/README.md](./WINS/README.md)
- record what failed in [STUCK/README.md](./STUCK/README.md)
- update [PROGRESS.md](./PROGRESS.md)

## If You Are Completely New

Do not jump straight to agents, RAG, or LangGraph because those terms are trendy. Start with Phase 1. The first real bottleneck in AI engineering is not model access. It is weak fundamentals:

- not understanding Python data structures
- not understanding APIs
- not knowing how files, logs, and tests work
- not being able to debug terminal output

If even the word `LLM` feels strange right now, that is okay. The Foundations pages are there so the rest of the curriculum does not assume too much.

## If You Already Know Some Python

Skim [PHASES/01-python/README.md](./PHASES/01-python/README.md), do one lab to prove you still remember the basics, then move faster into Phase 2.

## The Rule For Every Phase

If you cannot explain the concept in plain language and build a tiny version of it, you do not know it well enough yet.

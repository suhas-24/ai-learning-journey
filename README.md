# My AI Engineering Journey

> Started: 2026-03-29  
> Target Role: AI Engineer / LLM Application Developer  
> Pace: 12-15 months of steady, project-first learning  
> Current Stage: Phase 1 setup and fundamentals

This repository is the working notebook for the full journey from absolute beginner to production-capable AI engineer. It is intentionally practical: the goal is not to collect links or certificates, but to build real systems, document what breaks, and turn each phase into proof of skill.

If words like `LLM`, `token`, or `tokenization` feel unfamiliar, that is completely fine. A large language model, or LLM, is a program trained on lots of text so it can predict and generate text. A token is a small piece of text the model works with. Tokenization is the step that breaks text into those pieces. The repo explains those ideas from zero, so you do not need to arrive already fluent.

The repository has been reorganized into a chapter-based curriculum with labs, snippets, checkpoints, and troubleshooting so it can teach directly instead of behaving like a long outline.

The files in this repo should not be treated like a passive reading list. They are meant to behave like a learning operating system:

- `START-HERE.md` gives the quickest entry ramp
- `LEARNING_PATH.md` shows the full dependency chain
- `FOUNDATIONS/` explains shared terms, assumptions, and mental models from zero
- `PHASES/README.md` is the curriculum index
- `PROJECTS/README.md` is the portfolio build index
- `RESOURCES/README.md` explains how to use the reference library
- `README.md` tells me how to use the repository
- `PROGRESS.md` captures the weekly learning loop
- `PHASES/` contains the actual study notes
- `PROJECTS/` contains the build plans for the portfolio pieces
- `RESOURCES/` explains what each resource teaches
- `WINS/` and `STUCK/` turn experience into memory

## Learning Principles

- Build more than you watch. The roadmap is roughly 20% reading and 80% building.
- Learn the "why" before the framework. Raw concepts come first, convenience layers later.
- Break things on purpose. Debugging is part of the curriculum, not a side effect.
- Keep notes close to code. Each phase should produce artifacts, not just opinions.
- Treat agent behavior like software. Specs, evals, observability, and safety all matter.
- Define a new term before you rely on it. If a word feels fuzzy, pause and write down what it means in plain language.

## Overall Progress

```text
Phase 1  ░░░░░░░░░░  0%   Python + Dev Tooling
Phase 2  ░░░░░░░░░░  0%   Raw LLM APIs + Context Engineering
Phase 3  ░░░░░░░░░░  0%   Spec-Driven Development
Phase 4  ░░░░░░░░░░  0%   MCP + CLI + A2A Protocols
Phase 5  ░░░░░░░░░░  0%   Advanced RAG + GraphRAG + Memory
Phase 6  ░░░░░░░░░░  0%   Agentic IDEs + Coding Agents
Phase 7  ░░░░░░░░░░  0%   Orchestration + Harness Engineering
Phase 8  ░░░░░░░░░░  0%   Guardrails + Security + Governance
Phase 9  ░░░░░░░░░░  0%   Evals + Observability + EDD
Phase 10 ░░░░░░░░░░  0%   Fine-Tuning (optional)
Phase 11 ░░░░░░░░░░  0%   Portfolio + Job Readiness
```

**Overall:** 0/11 phases complete  
**What is already done:** the roadmap tracker repo, this learning tracker repo, and the full module-based curriculum structure

## Current Focus

**Phase:** Phase 1 - Python + Dev Tooling  
**Week:** Week 1  
**Working on:** getting fluent with Python basics, terminal workflow, Git, Poetry, and the habit of writing notes while building

## Best Entry Points

- Start here: [START-HERE.md](./START-HERE.md)
- Full curriculum map: [LEARNING_PATH.md](./LEARNING_PATH.md)
- Shared concepts and assumptions: [FOUNDATIONS/README.md](./FOUNDATIONS/README.md)
- Phase index: [PHASES/README.md](./PHASES/README.md)
- Project index: [PROJECTS/README.md](./PROJECTS/README.md)
- Resource library: [RESOURCES/README.md](./RESOURCES/README.md)

## Weekly Operating Loop

1. Read the current phase `README.md` and pick one chapter to study deeply.
2. Build one small thing that uses that concept.
3. Update `PROGRESS.md` with what happened, what got stuck, and what comes next.
4. If something went well, log it in `WINS/README.md`.
5. If something confused me or slowed me down, log it in `STUCK/README.md`.
6. Add one note to the active phase module so the material gets richer over time.

The loop matters because the curriculum gets longer than memory does. Notes need to become external memory.

## How This Repo Should Be Used

| Folder | How I will use it |
| --- | --- |
| `PHASES/` | Chapter-based learning modules with teaching notes, labs, snippets, checkpoints, and troubleshooting |
| `PROJECTS/` | Detailed build guides for the three portfolio-grade systems this roadmap requires |
| `RESOURCES/` | Curated books, courses, tools, people, and newsletters with notes on what each one teaches |
| `WINS/` | Visible proof of progress, especially on slow weeks |
| `STUCK/` | Debugging journal that turns confusion into reusable knowledge |
| `PROGRESS.md` | Weekly review cadence, goals, outcomes, and next moves |

## What A Phase Module Should Contain

Each phase module should explain the topic, not just name it. A good phase module usually has:

- why the phase exists
- the main concepts and subtopics
- the order to learn them in
- what to build while learning
- the traps and misunderstandings that tend to appear
- what success looks like before moving on

That structure is important because AI engineering concepts build on one another. If I cannot explain one layer clearly, the next layer becomes noisy.

In practice, each phase module should look like:

- `README.md` for the big picture and study order
- `chapters/` for direct teaching
- `labs/` or `exercises/` for guided practice
- `snippets/` for reusable code and command examples
- `checkpoints.md` for self-review
- `troubleshooting.md` for common failure modes

## Definition Of A Good Week

- I touched code, not just notes.
- I wrote down at least one thing I understood better than before.
- I captured one win and one sticking point.
- I can explain a concept in simple words, not just repeat jargon.
- I moved one project artifact closer to something worth showing publicly.

## What Success Looks Like By The End

- Three public projects that prove depth in RAG, orchestration, and production safety
- A GitHub profile with clean READMEs, evaluation evidence, and honest engineering notes
- Enough fluency with Python, LLM APIs, MCP, LangGraph, and guardrails to build without hand-holding
- A personal library of wins, failures, fixes, and design decisions I can talk through in interviews

## Notes On Pace

This journey should be steady rather than heroic. A good week is one where I learned something concrete, built something small, and left behind a clearer trail than I started with. The goal is compounding understanding, not sprinting through material and forgetting it a week later.

## Related Repositories

- Roadmap source of truth: [ai-trends-tracker](https://github.com/suhas-24/ai-trends-tracker)
- Learning tracker: [ai-learning-journey](https://github.com/suhas-24/ai-learning-journey)

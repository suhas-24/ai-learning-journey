# Resources Reference System

This folder is the reference layer for the learning journey. It is not a pile of links. It is a set of study guides that explain what each resource teaches, which ideas inside it are worth extracting, and when that resource becomes useful in the roadmap.

If some of the words in this repo feel new, that is normal. A few basics will show up everywhere:

- An `LLM` is a large language model, which means a model trained on lots of text so it can predict and generate text.
- A `token` is a small piece of text the model actually works with. A word may be one token or several tokens.
- `Tokenization` means splitting text into those small pieces.
- An `embedding` is a list of numbers that stands in for meaning, so similar text ends up with similar number patterns.
- A `retrieval system` finds useful information from a collection before the model answers.
- An `eval` is a test or measurement that tells you how well the system is doing.
- `Fine-tuning` means changing the model's internal weights with training data so it behaves differently.
- An `orchestration loop` is the step-by-step path a system follows when it plans, calls tools, checks results, and decides what to do next.

## How To Use This Layer

- Start with [by-phase.md](./by-phase.md) when you want the shortest path for your current phase.
- Use the category guides when you want depth:
  - [books/README.md](./books/README.md)
  - [courses/README.md](./courses/README.md)
  - [tools/README.md](./tools/README.md)
  - [people/README.md](./people/README.md)
  - [newsletters/README.md](./newsletters/README.md)
- Treat every resource as a teaching aid for a build decision. If a resource is not changing how you design, debug, evaluate, or ship, it is background noise.

## What This Reference Layer Tries To Solve

- Books are usually strong at mental models, tradeoffs, and systems thinking.
- Courses are usually strong at compressing a concept into a guided first pass.
- Tools become valuable when you understand the problem boundary they solve.
- People and newsletters help you keep your judgment current without turning learning into endless scrolling.

Think of the folder this way:

- books help you understand the idea
- courses help you get a quick first pass
- tools help you turn the idea into a working system
- people help you hear how experienced builders explain the same idea
- newsletters help you notice what is changing without chasing every headline

## Recommended Reading Order

1. Use [by-phase.md](./by-phase.md) to find the smallest useful set.
2. Read one concept guide from [books](./books/README.md) or [courses](./courses/README.md).
3. Pair it with the matching [tools](./tools/README.md) guide.
4. Use [people](./people/README.md) and [newsletters](./newsletters/README.md) only to reinforce judgment, not to replace hands-on work.

## Fast Start Paths

- If you are in early foundations, begin with [books/ml-foundations-and-thinking.md](./books/ml-foundations-and-thinking.md) and [tools/python-foundation-tools.md](./tools/python-foundation-tools.md).
- If you are learning model APIs, begin with [courses/prompting-and-api-basics.md](./courses/prompting-and-api-basics.md) and [tools/model-api-tools.md](./tools/model-api-tools.md).
- If you are building retrieval systems, begin with [books/ai-engineering-and-llm-systems.md](./books/ai-engineering-and-llm-systems.md), [courses/rag-and-retrieval-courses.md](./courses/rag-and-retrieval-courses.md), and [tools/retrieval-data-tools.md](./tools/retrieval-data-tools.md).
- If you are working on orchestration or agent systems, begin with [courses/orchestration-and-agents-courses.md](./courses/orchestration-and-agents-courses.md) and [tools/agent-orchestration-tools.md](./tools/agent-orchestration-tools.md).
- If you are focusing on reliability, guardrails, or evals, begin with [books/ai-engineering-and-llm-systems.md](./books/ai-engineering-and-llm-systems.md), [courses/evals-and-mlops-courses.md](./courses/evals-and-mlops-courses.md), and [tools/evals-observability-tools.md](./tools/evals-observability-tools.md).

## Navigation

- [by-phase.md](./by-phase.md)
- [books/README.md](./books/README.md)
- [courses/README.md](./courses/README.md)
- [tools/README.md](./tools/README.md)
- [people/README.md](./people/README.md)
- [newsletters/README.md](./newsletters/README.md)

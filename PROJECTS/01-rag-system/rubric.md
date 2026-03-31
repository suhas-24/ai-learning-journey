# Rubric - Production RAG System

Use this rubric as a quick honesty check.

Here, a `rubric` is just a scoring guide with clear criteria.

Score each area from 1 to 5.

## Problem Framing

- 1: a vague “chat with documents” idea
- 3: a clear corpus and user need
- 5: a realistic problem with scope and constraints

## Retrieval Design

Here, `vector search` means meaning-based search, `chunking` means splitting documents into smaller pieces, and `reranking` means sorting the found evidence again so the strongest items rise to the top.

- 1: vector search only, with no explanation
- 3: chunking and retrieval choices are documented
- 5: hybrid retrieval and reranking are justified with evidence

## Grounding

- 1: answers sound plausible but have no proof
- 3: citations exist
- 5: citations are reliable, inspectable, and part of the evaluation

## Evaluation

- 1: only screenshots or anecdotes
- 3: basic metrics are reported
- 5: there is a repeatable eval set, metrics, and error analysis

## Communication

- 1: the README is too thin to help a beginner
- 3: the architecture and setup are understandable
- 5: the repo feels portfolio-ready and interview-ready

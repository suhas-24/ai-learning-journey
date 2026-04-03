# Build Plan - Production RAG System

This plan moves from an empty folder to a system that can answer with evidence.

If the key words are new:

- `RAG` means retrieval-augmented generation, which is a pattern where the system finds evidence before answering
- a `corpus` is the document collection you want to search
- `ingestion` means reading those documents into a form your system can use
- `retrieval` means finding the most useful evidence
- `reranking` means sorting the results again to improve quality

Quick meanings for the terms used below:

- a `metadata schema` is a simple description of the fields stored with each chunk, such as source name, page, date, or section
- `top-k` means "the first k results," such as the top 5 or top 10 search results
- `rank fusion` means combining multiple search scores into one ranking
- `reranking` means sorting the first results again so the strongest evidence rises to the top
- an `answer schema` is the expected shape of the answer, such as answer text plus citations
- `abstention` means refusing to answer when the evidence is too weak

The order matters. A beginner can save a lot of time by proving that each step works before adding the next one.
If `abstention` feels unusual, think of it as the system saying, "I do not have enough proof yet."

## Milestone 1 - Corpus And Ingestion

Deliverables:

- document inventory
- chunking strategy note
- ingestion script
- metadata schema

Why this step exists:

- before the system can search, it needs a clean way to read documents

Definition of done:

- rerunning ingestion produces stable, inspectable outputs

## Milestone 2 - Baseline Retrieval

Deliverables:

- retrieval script or endpoint
- top-k inspection report
- 20 manual test queries

Why this step exists:

- you need a simple baseline before you can improve anything

Definition of done:

- you can inspect which chunks were retrieved and why

## Milestone 3 - Hybrid Retrieval And Reranking

Deliverables:

- keyword retrieval
- rank fusion logic
- reranking stage
- side-by-side comparison report

Why this step exists:

- different search methods solve different problems

Definition of done:

- at least one class of queries improves in a visible way

## Milestone 4 - Answer Generation

Deliverables:

- answer prompt or schema
- citation formatter
- abstention behavior for weak context

Why this step exists:

- the model should only answer from evidence that can be inspected

Definition of done:

- answers include traceable citations and avoid unsupported claims

## Milestone 5 - Evaluation

Deliverables:

- eval dataset with reference answers or expected sources
- automated metrics
- manual review sheet
- experiment report

Why this step exists:

- improvement only matters if you can prove it

Definition of done:

- a reviewer can see how quality is measured over time

## Milestone 6 - Demo And Packaging

Deliverables:

- polished README
- architecture diagram
- short demo or recording
- lessons learned section

Why this step exists:

- the project should feel like something another engineer could reuse

Definition of done:

- the repo reads like a shippable engineering artifact

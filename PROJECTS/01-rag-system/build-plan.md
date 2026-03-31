# Build Plan - Production RAG System

## Milestone 1 - Corpus And Ingestion

Deliverables:

- document inventory
- chunking strategy note
- ingestion script
- stored metadata schema

Definition of done:

- rerunning ingestion produces stable, inspectable outputs

## Milestone 2 - Baseline Retrieval

Deliverables:

- vector retrieval endpoint or script
- top-k inspection notebook or report
- 20 manual test queries

Definition of done:

- you can inspect which chunks were retrieved and why

## Milestone 3 - Hybrid Retrieval And Reranking

Deliverables:

- lexical retrieval
- rank fusion logic
- reranking stage
- side-by-side comparison report

Definition of done:

- you can show at least one class of queries that improved

## Milestone 4 - Answer Generation

Deliverables:

- answer prompt or schema
- citation formatter
- abstention behavior for weak context

Definition of done:

- answers include traceable citations and avoid unsupported claims

## Milestone 5 - Evaluation

Deliverables:

- eval dataset with gold answers or references
- automated metrics
- manual review sheet
- experiment report

Definition of done:

- a reviewer can see how system quality is measured over time

## Milestone 6 - Demo And Packaging

Deliverables:

- polished README
- architecture diagram
- short demo or screen recording
- lessons learned section

Definition of done:

- the project reads like a shippable engineering artifact

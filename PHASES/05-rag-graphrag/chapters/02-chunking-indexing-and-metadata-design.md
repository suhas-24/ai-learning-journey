# Chapter 2 - Chunking, Indexing, and Metadata

A `chunk` is a small piece of a document.

That piece is what the system searches, ranks, and cites. If the piece is too big, it may mix unrelated ideas. If it is too small, it may lose the meaning.

## Why We Split Documents At All

The model cannot search a whole large document in one giant block forever. The system needs smaller pieces so it can compare them with the question.

Chunking is just the process of deciding how those pieces should be made.

## Chunking Choices

### Fixed-size chunking

This means splitting text into equal-sized pieces.

Use it when:

- you need a quick baseline
- the documents are messy

Weakness:

- it can split a thought in half

### Structure-aware chunking

This means splitting by headings, sections, or natural boundaries.

Use it when:

- the documents already have structure
- you want the chunks to preserve meaning

Examples:

- Markdown by heading
- HTML by section
- code by function

### Semantic chunking

This means using meaning to decide where one chunk should end and the next should begin.

Use it when:

- the text is long and narrative
- you can afford extra preprocessing

Weakness:

- it is harder to debug
- it is less predictable than heading-based chunking

## Metadata

`Metadata` is extra information attached to a chunk.

Think of it like a label on a box.

Useful metadata includes:

- `source_path`
- `doc_type`
- `topic`
- `team`
- `effective_date`

Why it matters:

- it lets you filter before expensive ranking
- it helps you know where the evidence came from
- it makes debugging much easier

## Indexing

An `index` is the search structure that helps the system find chunks quickly.

A `vector database` is a place that stores embeddings and helps the system find chunks with similar meaning.

Three simple patterns matter here:

- dense index: good for meaning-based search
- sparse index: good for exact words, names, and error codes
- hybrid index: uses both

## Example

Suppose you have:

- design docs
- runbooks
- postmortems

A good setup might:

- chunk runbooks by step
- chunk postmortems by section
- add `doc_type` everywhere
- filter to `doc_type=runbook` when the question is "how do I fix this?"

## Simple Rule

Choose chunking and metadata together.

If the chunks are bad, the index cannot rescue them. If the metadata is missing, the search will be harder to control.

Next: [Chapter 3](./03-hybrid-retrieval-reranking-and-evaluation.md).

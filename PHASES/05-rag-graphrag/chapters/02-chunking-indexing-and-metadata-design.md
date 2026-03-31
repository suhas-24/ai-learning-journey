# Chapter 2 - Chunking, Indexing, and Metadata Design

Chunking is one of the most underestimated retrieval decisions. A chunk is the unit your system can remember, compare, rerank, and cite. If the unit is wrong, the rest of the pipeline works with damaged inputs.

## Chunking Strategies

### Fixed-size chunking

Useful when:

- documents are messy or unstructured
- you need a quick baseline

Weakness:

- can split concepts across boundaries

### Structure-aware chunking

Useful when:

- documents have headings, sections, tables, or code blocks
- you care about preserving meaning inside boundaries

Examples:

- Markdown by heading
- HTML by semantic section
- code by function or class

### Semantic chunking

Useful when:

- you can afford more preprocessing
- the corpus has long narrative sections

Weakness:

- harder to reason about
- may be less predictable for debugging

## Metadata Design

Metadata is not decoration. It is how retrieval gets narrowed before expensive ranking happens.

Strong metadata examples:

- `source_path`
- `doc_type`
- `product`
- `team`
- `effective_date`
- `security_level`

Weak metadata examples:

- generic tags with no operational use
- dozens of low-quality labels that never drive filtering

## Worked Example

Suppose you index:

- design docs
- runbooks
- incident postmortems
- architecture diagrams

Good retrieval design:

- chunk runbooks by procedure step
- chunk postmortems by section
- attach `doc_type` metadata everywhere
- filter to `doc_type=runbook` for "how do I recover" questions

## Indexing Patterns

### Dense vector index

Best when:

- semantic similarity matters most
- users ask natural-language questions

### Sparse keyword index

Best when:

- product names, error codes, and identifiers matter
- exact terminology must be preserved

### Hybrid index

Best when:

- both semantic and lexical cues matter
- your query set mixes fuzzy and exact-match needs

See [../snippets/chunking-config.json](../snippets/chunking-config.json) for a sample configuration.

## Design Rule

Choose chunking and metadata together. A beautiful vector index cannot rescue bad chunk units or missing metadata fields.

Continue to [Chapter 3](./03-hybrid-retrieval-reranking-and-evaluation.md).

# Metrics, Rubrics, and Score Interpretation

Metrics are useful only when they match the failure mode you care about.

A `metric` is a number or label that helps summarize behavior. A `rubric` is a scoring guide that explains what different scores mean. You use both because numbers alone can be misleading.

## First words

- `score` means a simple way to compare results
- `interpretation` means what the score tells you in plain English
- `judge model` means another model helping score outputs

## Why this matters

A high score can hide the wrong kind of success. The system may sound good while still missing facts, ignoring evidence, or taking unsafe actions.

## Separate the layers

For a retrieval system, at least three layers matter:

- retrieval quality
- generation quality
- task outcome

A response can sound polished while being poorly grounded. That is why one score is rarely enough.
Think of it like checking a meal for taste, temperature, and cleanliness. One check does not tell you everything.

## Common metrics

| Metric | What it measures | Typical failure signal |
| --- | --- | --- |
| Faithfulness | whether output stays grounded in context | hallucinated claims |
| Answer relevance | whether the output addresses the question | vague or off-topic answer |
| Context precision | whether retrieved chunks were useful | noisy retrieval |
| Context recall | whether the right evidence was found | missing key facts |
| Task success rate | whether the user goal was completed | workflow failure |
| Tool success rate | whether tool calls returned useful results | broken integration |
| Refusal correctness | whether unsafe requests were handled correctly | over-permissive or over-blocking behavior |

More examples live in [Metrics Catalog](../snippets/metrics-catalog.md).

## Rubrics

A rubric makes qualitative judgment more consistent.

Example rubric for a policy-grounded answer:

```yaml
rubric:
  grounded_in_sources:
    score_0: makes unsupported claims
    score_1: mostly grounded but includes one weak claim
    score_2: every important claim is source-backed
  completeness:
    score_0: misses major requested parts
    score_1: covers most requested parts
    score_2: covers all requested parts clearly
  safety:
    score_0: exposes restricted details
    score_1: avoids unsafe content but is clumsy
    score_2: safely responds and remains useful
```

## Sample scorecard

```text
run_id: eval_2026_04_11_a12
faithfulness: 0.84
answer_relevance: 0.91
context_precision: 0.52
tool_success_rate: 0.67
overall: investigate retrieval noise and tool adapter failures
```

Interpretation:

- the answer sounds relevant
- retrieval is noisy
- tool execution is unstable

Do not conclude "system is good" from one high number.

## Judge models and their limits

An LLM can be used as a judge to help score outputs, but that judge is still a model with biases of its own. In other words, the scorer is not magically perfect just because it is another model.

Use it well by:

- providing a structured rubric
- anchoring with examples
- spot-checking with human review
- comparing trends, not worshipping single numbers

Continue with [Observability, Traces, and Runtime Signals](./03-observability-traces-and-runtime-signals.md).

# Chapter 4 - Cost, Latency, and Failure Analysis

Good AI systems are not judged only by answer quality. They are also judged by speed, consistency, and cost.

## 1. Token Cost Is a Design Constraint

Every extra instruction, document, and tool result increases input size. Longer outputs increase output cost.

That means architecture choices affect money:

- large prompts cost more
- repeated retries cost more
- verbose tool output costs more

## 2. Latency Has Layers

When a model call feels slow, the delay may come from:

- network round-trip
- model generation time
- tool execution time
- your own code waiting on sequential steps

The fix depends on the layer. Do not blame the model for a slow file search.

## 3. Failure Analysis Mindset

When a result is bad, ask which layer failed:

- prompt or instruction layer
- context selection layer
- model selection layer
- tool execution layer
- post-processing or validation layer

This prevents emotional debugging.

## 4. Worked Example

Imagine the model returned invalid JSON.

Possible root causes:

- you asked for prose and JSON at the same time
- you forgot to validate and retry cleanly
- a tool result inserted too much unstructured text
- temperature was higher than the task needed

Notice how "the model is dumb" is not a useful diagnosis.

## 5. Lightweight Logging to Add Early

Track at least:

- request id
- model name
- elapsed time
- whether a tool was called
- whether validation succeeded

That small amount of data makes debugging far easier.

## 6. What To Practice

- inspect one bad answer and write down three possible root causes
- time a structured call with and without a tool step
- reduce prompt size and compare quality

Next: do [Lab 1](../labs/lab-01-structured-answerer.md) and [Lab 2](../labs/lab-02-tool-augmented-research-loop.md).

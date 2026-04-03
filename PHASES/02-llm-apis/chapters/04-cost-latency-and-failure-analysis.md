# Chapter 4 - Cost, Latency, and Failure Analysis

Good AI systems are not judged only by answer quality. They are also judged by speed, consistency, and cost. Those three extra signals matter because a useful system must also be practical to run.

## 1. Tokens Affect Cost

A `token` is a small piece of text. More text usually means more tokens.

Every extra instruction, document, and tool result increases input size. Longer outputs increase output cost.

That means architecture choices affect money:

- large prompts cost more
- repeated retries cost more
- verbose tool output costs more

## 2. Latency Has Layers

`Latency` means how long one request takes from start to finish.

When a model call feels slow, the delay may come from:

- network travel time
- model generation time
- tool execution time
- your own code waiting on steps one by one

The fix depends on which layer is slow. Do not blame the model for a slow file search.

## 3. Failure Analysis

When a result is bad, ask which layer failed:

- instruction layer
- context selection layer
- model choice layer
- tool execution layer
- post-processing or validation layer

This keeps debugging calm and specific.

## 4. Worked Example

Imagine the model returned invalid JSON.

Possible root causes:

- you asked for prose and JSON at the same time
- you forgot to validate and retry cleanly
- a tool result inserted too much unstructured text
- the temperature was higher than the task needed

Notice how "the model is dumb" is not a useful diagnosis. A better diagnosis names the layer that failed.

## 5. Simple Logging To Add Early

Track at least:

- request id
- model name
- elapsed time
- whether a tool was called
- whether validation succeeded

That small amount of information makes debugging much easier.

## 6. What To Practice

- inspect one bad answer and write down three possible root causes
- time a structured call with and without a tool step
- reduce prompt size and compare quality

Next: do [Lab 1](../labs/lab-01-structured-answerer.md) and [Lab 2](../labs/lab-02-tool-augmented-research-loop.md).

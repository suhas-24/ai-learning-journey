# Phase 9 - Evals + Observability + EDD

**Status:** 🔴 Not Started  
**Started:** Not started yet  
**Completed:** Not completed yet  
**Estimated Duration:** 4 weeks

---

## Why This Phase Matters

An AI system that "felt good in testing" is not enough. Engineering means measuring quality, finding regressions, understanding failures, and proving that changes actually improved the system. This phase turns AI work from intuition-driven iteration into evidence-driven iteration.

EDD, or Evaluation-Driven Development, is the discipline that keeps improvements honest.

---

## Concept Map

This phase is built from four connected ideas:

1. decide what good looks like before building
2. create a dataset that represents the real task
3. score model behavior and retrieval behavior separately
4. trace production failures so they become new tests

If any one of those parts is missing, the system becomes harder to trust and harder to improve.

---

## Core Ideas To Master

### Evaluation-Driven Development

1. define success before building
2. build a golden dataset
3. run evals on every important change
4. turn failures into new test cases
5. never ship blind

### The Golden Dataset

A golden dataset is not a giant benchmark. It is a carefully chosen set of examples that represent the real shape of the task. It should include:

- everyday requests that ought to pass easily
- edge cases that expose weak assumptions
- confusing or adversarial inputs
- examples where the answer depends on retrieved evidence

The purpose is to remember what "good" means when the system starts drifting.

### Evaluation Types

- final answer scoring
- trajectory scoring for tool use and intermediate decisions
- RAG-focused metrics such as faithfulness and context precision
- LLM-as-judge with structured rubrics
- prompt A/B testing when multiple prompts compete

### What The Main Metrics Mean

- faithfulness: the answer stays grounded in the provided context
- answer relevance: the answer actually addresses the question
- context precision: the retrieval step brought back useful evidence instead of noise
- context recall: the retrieval step found the important evidence in the first place
- task success rate: the system completed the real user task
- tool call success rate: the tools returned the expected useful results

These metrics measure different failure modes. A system can sound good while retrieving badly, or retrieve well while generating a weak final answer.

### Observability

- trace every model call and tool call
- track token cost, latency, success rate, and failure clusters
- version prompts and compare results over time
- connect production failures back to reproducible examples

### Why Observability Matters

Observability turns a vague complaint like "the agent was weird" into a structured story:

- which prompt version was used
- which model was called
- what tool was chosen
- what the tool returned
- where the failure first appeared

Without that trail, improvement becomes guesswork.

---

## Metrics I Need To Care About

- time to first token
- tokens per second
- cost per task
- task success rate
- tool call success rate
- hallucination rate
- context precision and recall for retrieval systems

If I cannot measure the system, I cannot improve it reliably.

---

## Phase Project: Full Eval Suite + Observability Layer

**Project goal:** add a real measurement stack to the agent built in Phases 7 and 8.  
**Planned repo:** inside the main agent system or as a connected evaluation package  
**Current project status:** planned, not started

### Required outputs

- a golden dataset with representative tasks and edge cases
- automated evaluation runs
- trace dashboards for model and tool behavior
- failure thresholds that can block merges or deployments
- a feedback loop that turns production mistakes into eval cases

### Suggested Build Order

1. start with a tiny local eval script
2. run the same tasks before and after changes
3. score the outputs and save the results
4. add tracing so failures can be inspected later
5. move the checks into CI once the local loop is stable

### Tooling To Explore

- RAGAS
- Langfuse
- LangSmith
- PromptFoo or DeepEval

### How To Think About The Tooling

- RAGAS is strongest when retrieval quality matters
- LLM-as-judge is useful when you need scalable qualitative scoring
- tracing tools matter when you need to understand why a specific failure happened
- prompt-testing tools matter when you need controlled comparisons between variants

The point is not to adopt every tool. The point is to make measurement part of the workflow.

---

## Exit Criteria

- I can create a useful golden dataset instead of cherry-picking easy examples.
- I can measure RAG quality and task quality separately.
- I can trace a bad output back to the step that caused it.
- I can explain the difference between observability and evaluation.
- I can set a quality threshold that guards against regressions.

---

## Common Traps To Avoid

- only checking final answers and ignoring broken tool choices
- using tiny or overly easy evaluation sets
- trusting one judge model without thinking about its bias
- treating dashboards as success instead of using them to drive fixes
- changing prompts without versioning them
- measuring quality after deployment but not before merge
- confusing a cheap eval with a meaningful eval

---

## Resources For This Phase

| Resource | Why it matters | How I should use it |
| --- | --- | --- |
| RAGAS docs | Strong baseline for RAG evaluation | Start with faithfulness and relevance first |
| Langfuse docs | Good tracing and prompt versioning | Instrument one project end to end |
| PromptFoo or DeepEval docs | Helps compare prompt variants quickly | Use for controlled prompt experiments |
| LangSmith docs | Useful if LangGraph becomes central | Compare dataset and tracing workflows |

---

## Questions I Want To Answer During This Phase

- What failures matter most to real users?
- Which metrics are worth blocking a merge on?
- How do I keep evals cheap enough to run often?
- What is the smallest useful observability setup for an individual builder?

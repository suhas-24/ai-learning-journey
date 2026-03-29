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

## Core Ideas To Master

### Evaluation-Driven Development

1. define success before building
2. build a golden dataset
3. run evals on every important change
4. turn failures into new test cases
5. never ship blind

### Evaluation Types

- final answer scoring
- trajectory scoring for tool use and intermediate decisions
- RAG-focused metrics such as faithfulness and context precision
- LLM-as-judge with structured rubrics
- prompt A/B testing when multiple prompts compete

### Observability

- trace every model call and tool call
- track token cost, latency, success rate, and failure clusters
- version prompts and compare results over time
- connect production failures back to reproducible examples

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

### Tooling To Explore

- RAGAS
- Langfuse
- LangSmith
- PromptFoo or DeepEval

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

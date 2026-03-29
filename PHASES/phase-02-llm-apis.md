# Phase 2 - Raw LLM APIs + Context Engineering

**Status:** 🔴 Not Started  
**Started:** Not started yet  
**Completed:** Not completed yet  
**Estimated Duration:** 4 weeks

---

## Why This Phase Matters

Frameworks are helpful, but they can hide the most important parts of an AI system: request shape, conversation history, tool call payloads, token usage, and failure handling. This phase is where I learn how models behave before any framework smooths the rough edges away.

The second half of this phase is context engineering: deciding what information belongs in the model's working memory at each step. This is the real successor to "prompt engineering."

---

## Core Ideas To Master

### Raw API Mechanics

- how a `messages` array actually looks
- what `system`, `user`, and assistant content each do
- temperature, max tokens, stop sequences, and streaming
- tool calling and structured output without magical abstractions
- token usage and cost as first-class engineering constraints

### Context Engineering

- the model only knows what is inside the current context window
- too little context causes weak answers
- too much context causes confusion, waste, and slower responses
- progressive disclosure beats dumping every document into every prompt
- summaries, retrieval results, tool outputs, and memory all compete for space

### Model Selection

- pick the cheapest model that can reliably do the task
- judge models by trajectory quality, not just final-answer hype
- learn when a task needs reasoning depth versus fast throughput

---

## Study Sequence

1. Send direct API calls to one model and inspect the raw response structure.
2. Add multi-turn conversation history and see how memory is simulated.
3. Force structured output and validate it with Pydantic.
4. Implement at least one tool call by hand.
5. Measure token usage and cost per request.
6. Practice context design with short, medium, and overloaded prompts.

---

## Mini Experiments To Run

- ask the same task with three temperature settings and compare behavior
- stream a long answer token by token to understand perceived latency
- build a "bad context" prompt and a "good context" prompt for the same task
- compare a frontier model and a cheaper model on one extraction task and one reasoning task
- simulate a small agent loop: ask model -> get tool call -> run tool -> send tool result -> finish task

---

## Phase Project: Raw Research Agent

**Project goal:** build a direct-API research assistant before touching orchestration frameworks.  
**Planned repo:** a standalone repo created during Phase 2  
**Current project status:** concept defined, implementation not started

### What the project should do

- accept a research question
- call an LLM API directly
- optionally call simple tools such as web lookup or file search
- return a structured response with findings, sources, and next actions
- log model, token usage, and approximate cost

### What this project is really teaching

- how conversation state is represented
- what tool use looks like in raw JSON
- how much context quality changes final output quality

---

## Exit Criteria

- I can call Anthropic or OpenAI directly without relying on a framework.
- I can explain the structure of a tool call and handle it in code.
- I can force and validate JSON output.
- I can track usage and estimate cost for a task.
- I can explain why context engineering is broader than prompt engineering.

---

## Common Traps To Avoid

- hiding behind wrappers before understanding the base protocol
- assuming the model "remembers" anything that was not re-sent in context
- stuffing irrelevant documents into prompts
- ignoring token usage until costs become painful
- evaluating only the final answer and not the path the model took to get there

---

## Resources For This Phase

| Resource | Why it matters | How I should use it |
| --- | --- | --- |
| Anthropic docs and cookbook | Clear examples for messages, tools, and streaming | Rebuild examples by hand |
| OpenAI docs and cookbook | Good for cross-provider comparison | Compare response formats and tool flows |
| Model pricing pages | Cost discipline starts early | Track price differences for identical tasks |
| AI Engineering by Chip Huyen | Gives the systems view | Focus on API behavior and context design chapters |

---

## Questions I Want To Answer During This Phase

- What belongs in the system prompt versus retrieved context?
- When should a model use a tool instead of answering from context?
- How do I know whether a model failure is caused by prompt wording, missing context, or the wrong model choice?
- How much quality do I gain from extra context before returns start diminishing?

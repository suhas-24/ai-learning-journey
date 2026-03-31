# Phase 2 - Raw LLM APIs + Context Engineering

**Status:** 🔴 Not Started  
**Started:** Not started yet  
**Completed:** Not completed yet  
**Estimated Duration:** 4 weeks

---

## Why This Phase Matters

Frameworks are helpful, but they can hide the most important parts of an AI system: request shape, conversation history, tool call payloads, token usage, and failure handling. This phase is where I learn how models behave before any framework smooths the rough edges away.

The second half of this phase is context engineering: deciding what information belongs in the model's working memory at each step. This is the real successor to "prompt engineering."

If Phase 1 teaches me how to write code, Phase 2 teaches me how to talk to a model like an engineer instead of a user clicking around in a chat app.

---

## Chapter Map

### Chapter 1: The API Conversation Shape

An LLM API call is not magic. It is a structured request with a conversation, a system instruction, and generation settings. Understanding the request shape is the first step to understanding how the model is being guided.

### Chapter 2: Generation Controls

Temperature changes how random the model is. Max tokens changes how much it can say. Stop sequences tell it when to stop. Streaming lets me see tokens as they arrive instead of waiting for the whole answer.

### Chapter 3: Tool Calling

Tool calling is how the model asks for help from external systems. The model proposes a tool use, my code executes the tool, and the result goes back into the conversation. This is the basic pattern behind agents.

### Chapter 4: Context Engineering

The context window is the model's short-term memory. It contains the system prompt, history, retrieved content, and tool results. The hard part is deciding what to include, what to summarize, and what to leave out.

### Chapter 5: Model Selection And Cost

Different models have different strengths, prices, and tradeoffs. Some are better for extraction, some for reasoning, some for speed, and some for cost control. The right choice depends on the task, not hype.

---

## Topic Guide

### Message Structure

- `system` messages define the role and boundaries
- `user` messages define the task
- assistant messages represent model responses
- tool messages feed back external results

### Generation Settings

- `temperature` affects variability
- `max_tokens` controls output length
- `stop` sequences help end generation cleanly
- streaming lets me build responsive user experiences

### Structured Output

- use JSON-like output when the next step depends on machine-readable data
- validate the output with Pydantic or a schema
- do not trust the model just because the answer looks neat

### Tool Use

- define tools clearly, including names, inputs, and outputs
- keep tools small and well-scoped
- treat tool execution as normal program logic, not hidden model behavior

### Context Strategy

- include only what is relevant to the current step
- summarize old history instead of keeping everything forever
- retrieve documents when needed instead of dumping the whole corpus
- use tool results to update context incrementally

### Cost And Quality

- every token has cost
- every extra prompt chunk adds noise risk
- model choice should be based on task complexity and tolerance for error
- trajectory quality matters because agent workflows can fail before the final answer

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

## A Mental Model For This Phase

Think of the model as a reasoning engine sitting inside a controlled information environment. The code around it is not decoration. The code is what decides what the model sees, what actions it can request, and how much information it is allowed to carry from step to step.

Good context engineering answers four questions:

- What does the model need right now?
- What can be summarized?
- What should be retrieved?
- What should be left out entirely?

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

## Resource Notes

### Anthropic Docs And Cookbook

Focus on message formatting, tool use, streaming, and usage reporting. The cookbook is especially useful because it shows direct, practical request/response shapes.

### OpenAI Docs And Cookbook

Use this to compare provider conventions, especially around structured output and tool interfaces. The goal is cross-provider literacy, not brand loyalty.

### Model Pricing Pages

Costs shape design. A model that is "good enough" for an extraction step may be the right choice if it is much cheaper and faster.

### AI Engineering by Chip Huyen

Use this as the systems-thinking companion to the API work. The best chapters for this phase are the ones that explain deployment, evaluation, and the relationship between models and products.

---

## Questions I Want To Answer During This Phase

- What belongs in the system prompt versus retrieved context?
- When should a model use a tool instead of answering from context?
- How do I know whether a model failure is caused by prompt wording, missing context, or the wrong model choice?
- How much quality do I gain from extra context before returns start diminishing?

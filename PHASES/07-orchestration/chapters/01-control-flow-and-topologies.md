# Control Flow and Topologies

Orchestration is just a fancy word for "deciding the order of steps."

When a person cooks, they do not dump every ingredient into the pan at once. They decide what comes first, what comes second, and what should happen if something goes wrong. Orchestration is that same idea for software: a system decides the next step, watches the result, and chooses the following step.

A model can suggest an answer or next action, but reliable software needs rules around that suggestion.

## The core idea

A single-agent loop looks like this:

```text
read input -> ask model -> maybe call tool -> answer user
```

That is enough for simple tasks. It breaks down when we need:

- multiple steps with different rules
- durable progress across long runs
- retries and escalation
- separate roles with separate permissions
- visibility into which step failed

At that point we need explicit control flow.

`Control flow` means the path your program follows. Sometimes that path is straight. Sometimes it branches, repeats, pauses, or asks a human for help.

## Common orchestration topologies

### 1. Single agent with tools

Use this when one model can reason about the whole task and tools are short-lived.

Best for:

- FAQ bots
- one-shot retrieval and answer tasks
- low-risk automation with a tight scope

Failure mode:

- the loop silently retries bad ideas because there is no external state machine

### 2. Sequential pipeline

Each stage has a narrow job and passes structured output forward.

Example:

```text
ingest request -> retrieve evidence -> synthesize answer -> run validator -> return response
```

Best for:

- deterministic business workflows
- report generation
- document processing

Failure mode:

- brittle interfaces between stages if schemas are vague

### 3. Orchestrator with specialists

A coordinator chooses which worker should act next.

Example:

```text
coordinator -> researcher
coordinator -> analyst
coordinator -> writer
coordinator -> approval gate
```

Best for:

- tasks where specialization improves quality
- flows with branching and escalation

Failure mode:

- too many agents create more coordination cost than value

### 4. Graph execution

Graph orchestration models the workflow as nodes and edges with shared state.

In plain language, a graph is just a map of allowed next steps. Each box is a place the workflow can be, and each arrow is a choice for what can happen next.

Best for:

- retries with branching logic
- pause and resume
- loops with stop conditions
- human-in-the-loop checkpoints

Failure mode:

- the graph becomes unreadable if nodes are too granular

## Choosing the right topology

Use this decision table:

| Question | If yes | Prefer |
| --- | --- | --- |
| Is the task short and low-risk? | One reasoning loop is enough | Single agent with tools |
| Does each stage have a clear handoff? | Stages can be typed and validated | Sequential pipeline |
| Do different roles need different prompts or permissions? | Specialization matters | Orchestrator with specialists |
| Must the task survive restarts and support loops? | State must persist between steps | Graph execution |

## A practical mental model

Think of orchestration as air traffic control. The planes are model calls and tool calls. The controller does not fly the plane, but decides sequencing, spacing, escalation, and emergency handling.

If you let planes manage the tower, you get collisions.

## Example: research task with durable control flow

Suppose the user asks:

> Summarize the top three deployment options for a Python RAG service and include cost tradeoffs.

A naive loop may search, summarize, and answer. A better orchestrator would do this:

```yaml
steps:
  - name: collect_requirements
    output: scope
  - name: gather_sources
    output: raw_sources
  - name: score_sources
    output: ranked_sources
  - name: draft_summary
    output: draft
  - name: validate_citations
    output: validation_result
  - name: finalize_or_escalate
    output: final_answer
```

Each step can fail differently. That is the point. Once steps are explicit, failures become local and debuggable.

## What good looks like

A well-designed orchestrator has:

- named states
- typed handoffs
- explicit exit conditions
- budgets and timeouts
- clear escalation rules

Continue with [State, Checkpoints, and Resumability](./02-state-checkpoints-and-resumability.md).

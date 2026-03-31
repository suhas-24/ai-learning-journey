# State, Checkpoints, and Resumability

If orchestration is the traffic controller, state is the flight board. Without it, the system does not know where it is, what has already happened, or what can safely happen next.

## What belongs in orchestration state

Store facts that the runtime needs in order to continue correctly:

- current step
- completed steps
- tool outputs that matter later
- retry counts
- budgets consumed
- approval decisions
- last stable checkpoint

Do not store everything. Raw prompts, giant transcripts, and ephemeral formatting can live elsewhere if they are not needed for recovery.

## Example state document

```json
{
  "run_id": "run_2026_04_07_001",
  "task": "compare deployment options for a RAG service",
  "status": "awaiting_validation",
  "current_node": "validate_citations",
  "attempts": {
    "gather_sources": 1,
    "validate_citations": 2
  },
  "budget": {
    "max_usd": 1.5,
    "spent_usd": 0.82
  },
  "artifacts": {
    "ranked_sources_path": "artifacts/ranked_sources.json",
    "draft_path": "artifacts/draft.md"
  },
  "approval": {
    "required": false,
    "decision": null
  },
  "last_checkpoint_at": "2026-04-07T09:18:44Z"
}
```

Related reference: [State Schema](../snippets/state-schema.md).

## Checkpoints

A checkpoint is a known-good recovery point. It should capture enough information to resume work without repeating unsafe or expensive actions.

Checkpoint after:

- any expensive retrieval batch
- any irreversible user-facing action proposal
- any stage that fans out into multiple workers
- any step whose output is reused downstream

Avoid checkpointing after every token-level event. That creates noise and storage cost without improving recovery.

## Resume logic

When a run restarts, the harness should:

1. load the latest checkpoint
2. verify artifacts still exist
3. inspect retry counters and budget state
4. resume from the last incomplete safe node
5. emit a structured resume event to logs

Example resume policy:

```python
def choose_resume_node(state: dict) -> str:
    if state["status"] == "awaiting_human_approval":
        return "approval_gate"
    if state["budget"]["spent_usd"] >= state["budget"]["max_usd"]:
        return "stop_budget_exceeded"
    return state["current_node"]
```

## What usually goes wrong

### Mistake: state is just chat history

Why it fails:

- critical runtime variables are hidden inside prose
- retries cannot tell whether a tool already ran
- approval decisions get lost

Fix:

- split conversational context from operational state

### Mistake: state grows forever

Why it fails:

- recovery slows down
- debugging becomes harder because signal is buried in noise

Fix:

- keep operational state compact and archive verbose traces separately

## Failure walkthrough: crash after tool success

Scenario:

- node `gather_sources` calls a search API
- the API returns successfully
- the process crashes before the next node runs

Bad design:

- no checkpoint after the tool call
- restart repeats the expensive search

Good design:

- write tool output artifact
- update checkpoint with artifact path and node completion
- on restart, skip `gather_sources` and continue to `score_sources`

## The real lesson

Resumability is not only about uptime. It is about making behavior legible under stress.

Continue with [Harness Components and Runtime Policies](./03-harness-components-and-runtime-policies.md).

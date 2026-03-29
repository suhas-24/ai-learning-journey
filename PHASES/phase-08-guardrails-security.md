# Phase 8 - Guardrails + Security + Governance

**Status:** 🔴 Not Started  
**Started:** Not started yet  
**Completed:** Not completed yet  
**Estimated Duration:** 3 weeks

---

## Why This Phase Matters

Once an agent can send email, write files, call APIs, or spend money, safety stops being a nice-to-have. Prompt injection, sensitive data leakage, excessive autonomy, and unbounded cost are not theoretical problems. They are production realities.

This phase exists so I can build agents that are useful without being reckless.

---

## Core Ideas To Master

### Threat Model Basics

- prompt injection
- sensitive data disclosure
- insecure output handling
- excessive agency
- poisoned retrieval data
- system prompt leakage
- unbounded consumption of tokens, tools, and time

### Guardrail Layers

- input validation
- output validation
- tool input sanitization
- irreversible action approval
- sandboxed code execution
- audit logging and traceability

### Governance Patterns

- confidence thresholds
- value thresholds
- irreversible action gates
- least-privilege tool access
- human review for high-stakes actions

---

## What I Need To Understand Deeply

- safety is a system property, not a single prompt line
- refusal behavior must be designed, tested, and logged
- validators are useful, but they do not replace architecture decisions
- the strongest agent is not the one with the most power; it is the one with the right boundaries

---

## Phase Project: Guardrail Layer For The Phase 7 Agent

**Project goal:** add practical safety and governance controls to the orchestration system built in Phase 7.  
**Planned repo:** implemented inside the Phase 7 project or as a dedicated extension layer  
**Current project status:** planned, not started

### Required controls

- prompt-injection detection and handling
- validation of tool inputs and outputs
- approval gate for costly or irreversible actions
- sandboxing for code execution
- immutable audit log for actions and decisions

### Tooling To Explore

- NeMo Guardrails for behavior and policy control
- Guardrails AI for validation and re-ask flows
- Docker or similar isolation for untrusted code paths

---

## Exit Criteria

- I can explain the top agent security risks in plain language.
- I know where to put approval gates in a workflow.
- I can validate structured input and output at tool boundaries.
- I can describe how sandboxing changes the blast radius of a failure.
- I can produce an audit trail that would help investigate an incident later.

---

## Common Traps To Avoid

- assuming the system prompt alone is a sufficient defense
- giving an agent broad permissions before defining safe defaults
- validating the final answer but ignoring tool arguments
- treating observability as separate from security
- skipping explicit approval for destructive or external-facing actions

---

## Resources For This Phase

| Resource | Why it matters | How I should use it |
| --- | --- | --- |
| OWASP LLM guidance | Best risk vocabulary | Use it to frame concrete threats |
| NeMo Guardrails docs | Policy and safety patterns | Prototype a small policy set first |
| Guardrails AI docs | Validation patterns for Python systems | Focus on tool and schema boundaries |
| Security writeups on prompt injection | Helps avoid naive defenses | Turn examples into test cases |

---

## Questions I Want To Answer During This Phase

- Which safety checks should happen before a model call, after a model call, and before a tool call?
- How do I decide when an action needs human approval?
- What should my minimum audit log include for a production agent?
- What is the safest default permission model for agent tools?

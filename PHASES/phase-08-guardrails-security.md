# Phase 8 - Guardrails + Security + Governance

**Status:** 🔴 Not Started  
**Started:** Not started yet  
**Completed:** Not completed yet  
**Estimated Duration:** 3 weeks

---

## Why This Phase Exists

The moment an agent can do something real, safety becomes part of the design, not an afterthought. Sending an email, deleting a file, making an API request, or spending money all require boundaries. This phase is about making useful systems that do not turn reckless just because the model is confident.

---

## Chapter Map

### 8.1 Threat Modeling For LLM Systems

I need to understand how an attacker or a bad input can push an agent off course. The main risks are prompt injection, sensitive data leakage, insecure output handling, excessive agency, and poisoned retrieval.

### 8.2 Guardrail Layers

Safety works best as layers: validate input, validate output, sanitize tool arguments, gate irreversible actions, sandbox risky execution, and log everything important.

### 8.3 Governance Patterns

Governance is the policy layer above the tools. It decides when the agent can act, when it needs review, and when a human must be in the loop.

### 8.4 Safe Execution

Any place the agent can run code or issue destructive commands needs isolation and least privilege.

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

### Required Controls

- prompt-injection detection and handling
- validation of tool inputs and outputs
- approval gate for costly or irreversible actions
- sandboxing for code execution
- immutable audit log for actions and decisions

### What This Project Should Prove

- I can protect the agent without making it useless.
- I can explain where safety checks belong in the request lifecycle.
- I can reduce blast radius using policy, validation, and isolation together.

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

## Resources And What They Help Me Learn

| Resource | What It Teaches |
| --- | --- |
| OWASP LLM guidance | Concrete risk language for threat modeling |
| NeMo Guardrails docs | How policy rules and flow control fit together |
| Guardrails AI docs | Input/output validation and repair workflows |
| Security writeups on prompt injection | How attacks actually work and how to test for them |

---

## Questions I Want To Answer During This Phase

- Which safety checks belong before a model call, after a model call, and before a tool call?
- How do I decide when an action needs human approval?
- What should my minimum audit log include for a production agent?
- What is the safest default permission model for agent tools?

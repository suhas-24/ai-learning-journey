# Chapter 4 - Review and Change Management

If `review` and `change management` sound formal, the beginner version is simple:

- `review` means checking whether the spec really says what we want
- `change management` means changing behavior in a controlled way so surprises are less likely

Specs become valuable when they are treated as living contracts rather than one-time setup files.

## 1. Review Specs Like Code

When reviewing a spec change, ask:

- did the role become clearer or fuzzier?
- are the constraints testable?
- was a rule duplicated from somewhere else?
- does the done condition still match the real task?

## 2. Behavior Changes Should Leave a Trail

If an agent starts using a new tool, escalating differently, or changing output format, that should appear in a spec diff where reviewers can see it.

## 3. Worked Example

Bad pattern:

- change hidden prompt string in code
- no doc update
- teammates learn by surprise

Better pattern:

- update the behavior spec first
- review the intended change
- then update implementation if needed

## 4. A Small Review Checklist

- scope is explicit
- constraints are concrete
- escalation is present
- done condition is testable
- no duplicated rules across files

## 5. Common Confusion

### Stale specs

The code changed, but the spec still describes old behavior. Now the contract is misleading.

### Overfitted specs

The spec is so specific to one incident that it becomes fragile and hard to reuse.

## 6. What To Practice

- review one spec using the checklist above
- propose a behavior change by editing the contract first
- identify one duplicated rule and decide where it should really live

Next: complete the labs, then use [checkpoints.md](../checkpoints.md).

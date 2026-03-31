# Lab 02 - Build Safety Gates

This lab turns a vague "be safe" instruction into concrete controls.

## Why this matters

Safety gets real when you decide where the system must stop, where it must ask for help, and what it must log.

## Scenario

You have an agent with these abilities:

- search internal docs
- summarize results
- draft an email
- send the email

## Task 1: define each boundary

Write a guard for:

- user input
- retrieval results
- email tool arguments
- final send action

## Task 2: design a policy file

Include:

- allowed recipient domains
- max recipients
- which actions require approval
- which roles can access which tools

## Task 3: define one refusal response

Write what the system should say when a user asks for an unsafe action.

The response should:

- refuse clearly
- avoid leaking hidden policy text
- offer a safe alternative when possible

## Task 4: add audit fields

For each blocked or approved action, record:

- run id
- action
- reason
- approver if present
- timestamp

## Stretch task

Add a rule for suspicious retrieved instructions and explain whether the system should redact, label, or discard them.

Use [Troubleshooting](../troubleshooting.md) if your design starts blocking too much normal work.

If you can explain each gate in one sentence, you understand it well enough to use it in a real project.

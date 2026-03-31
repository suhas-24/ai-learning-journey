# Lab 01 - Build a Threat Model

This lab helps you practice threat modeling on a realistic AI workflow.

## Why this matters

You are learning how to spot trouble before the system ships. That is much easier than trying to fix a real incident after a user finds it.

## Workflow

Use this scenario:

> An internal assistant can search company notes, summarize findings, and draft an email to the leadership team.

## Step 1: list the assets

Write down at least five assets, such as:

- internal notes
- customer data
- API keys
- outbound email channel
- audit logs

## Step 2: list the trust boundaries

Include:

- user input
- retrieval corpus
- model context assembly
- tool adapters
- approval channel

## Step 3: name attack paths

Come up with at least four attack or misuse paths.

Examples:

- malicious note in the corpus causes prompt injection
- user asks for hidden system instructions
- outbound email goes to an external recipient
- looping retrieval burns budget

## Step 4: map a control to each path

For each attack path, specify:

- prevention control
- detection signal
- containment action

## Deliverable

A one-page risk register using [Risk Register Schema](../snippets/risk-register-schema.md).

If you are unsure whether something is an asset, ask: "Would we care if this got leaked, changed, or lost?"

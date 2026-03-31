# Style Guide For The Parallel Rewrite

## The Main Shift

The repository must stop behaving like a reading checklist and start behaving like a self-contained teaching notebook.

Bad pattern:

- "Read the docs"
- "Use this resource"
- "Build a project"

Good pattern:

- explain what the concept is
- explain why it exists
- break it into topics and subtopics
- explain what to learn first, second, and third
- show how it appears in real AI engineering systems
- describe mistakes, tradeoffs, and practical signals

## Content Expectations

Every rewritten content file should include, where relevant:

- concept explanation in plain language
- topic and subtopic breakdown
- concrete sequence for learning
- direct explanation of terminology
- practical mental models
- examples of where the concept shows up in AI engineering
- common traps, confusion points, or failure modes
- clear relationship to the roadmap phase

## Tone

- practical
- honest
- beginner-friendly without being simplistic
- no hype
- no empty motivational filler

## Formatting

- use short sections with clear headers
- prefer explanatory prose plus tight bullets
- keep Markdown clean and readable
- avoid placeholder text
- avoid leaving blank "to be filled later" sections unless absolutely necessary

## What To Remove

- stubs
- empty templates
- sections that only say "read this"
- vague statements with no explanation

## File-Specific Expectations

### Top-level docs

- should explain how the repository works and how the learner should use it week to week

### Phase files

- should teach the phase directly
- should contain a true topic map, not just objectives

### Project files

- should explain architecture, phases, validation, risks, and what "done" means

### Resource files

- should explain why each resource matters and where it fits
- should not be just a list of names

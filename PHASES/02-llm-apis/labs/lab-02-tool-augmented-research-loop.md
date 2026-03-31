# Lab 2 - Build a Tool-Augmented Research Loop

This lab teaches the handoff between model reasoning and outside evidence.

If the title feels dense, here are the words in plain language:

- a `tool` is a helper your program can run, such as reading a file
- `augmented` means "helped by something extra"
- a `loop` is a repeated pattern of steps
- `context` is the information the model can currently see

So a `tool-augmented research loop` is just a repeated pattern where the model can ask your program for outside information before answering.

## Goal

Create a small loop where:

- the user asks a question
- the model may request a file-reading tool
- your program executes the tool
- the tool result is added back into context
- the model gives a final answer

## Suggested Tool

`read_notes(path: str) -> str`

The tool can read a local text file instead of using the web. That keeps the lesson focused on the interaction pattern.

Here, `path` just means the location of the file on your computer.

## Important Design Rule

Do not let the model run the tool directly. The model requests. Your code decides whether and how to execute.

## Failure Cases To Test

- the tool path does not exist
- the tool result is too long for the next step
- the model asks for an unknown tool

## Stretch Goal

Add a context summary after the first loop so the final request stays small and clear.

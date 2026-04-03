# Chapter 2 - Structured Output and Tool Calling

This chapter shows two things:

1. how to ask for an answer in a shape code can read
2. how the model can ask your program for outside help

The big idea is that the model is useful, but your code still needs to keep the request and the result in a shape it can trust.

## 1. Structured Output

Sometimes you do not want a paragraph. You want a result with named pieces.

For example, if the model is classifying a support ticket, this is easier for code to use:

```json
{
  "priority": "high",
  "needs_human": true,
  "reason": "Payment issue affects checkout"
}
```

That shape is easier to check than a free-form paragraph. A **schema** is the set of rules that says what fields should exist and what type of data each field should hold.

### Why validation matters

The model can still make mistakes:

- it might leave out a key
- it might give the wrong type
- it might wrap the JSON in extra text

That is why your program validates the output before trusting it.

## 2. Tool Calling

Tool calling is a back-and-forth pattern between the model and your program.

Think of it like this:

1. your code sends the model a question and a list of helper tools
2. the model decides a tool would help
3. the model asks for that tool
4. your program decides whether to run it
5. your program runs it and gets the result
6. your program sends the result back to the model
7. the model writes the final answer

The model does not run tools by itself. Your program stays in charge. That separation is what keeps the system safe and inspectable.

## 3. Worked Example

User asks:

```text
What unfinished tasks are in notes.txt?
```

The model might ask for a file-reading tool:

```json
{
  "tool_name": "read_file",
  "arguments": {"path": "notes.txt"}
}
```

Your program reads the file, then returns the contents as a `tool` message.

After that, the model can answer using the actual text instead of guessing.

## 4. Good Tool Design

Good tools are:

- narrow in purpose
- explicit about inputs
- safe to run
- easy to test without a model

If a tool tries to do too many unrelated jobs, it becomes hard to trust and hard to debug. A beginner-friendly tool does one thing clearly.

## 5. Common Confusion

### Tool schema is vague

If the tool description is unclear, the model may send arguments that do not make sense.

### Tool output is too large

If a tool returns a huge amount of text, the next model step can become crowded. Summarize or chunk the result.

### Tool result is not checked

If a tool returns malformed data and you pass it onward without validation, the loop becomes brittle.

## 6. What To Practice

- design one tool with clear input and output fields
- simulate one tool call without using a real provider
- validate one structured response before trusting it

Next: [Chapter 3: Context Engineering](./03-context-engineering.md)

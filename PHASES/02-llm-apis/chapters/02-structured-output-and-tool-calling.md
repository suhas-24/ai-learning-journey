# Chapter 2 - Structured Output and Tool Calling

This chapter is about two useful ideas:

- asking the model for a shaped answer instead of a paragraph
- letting the model ask your program for outside help

## 1. Structured Output

Suppose you want the model to classify a support ticket. Free-form prose is awkward for code to read. A shape with named fields is easier.

Desired shape:

```json
{
  "priority": "high",
  "needs_human": true,
  "reason": "Payment issue affects checkout"
}
```

Now your code can check the fields before it acts.

### Why validation matters

A model can still produce:

- missing keys
- wrong data types
- extra words around the JSON

So you validate after generation. You do not trust the output just because it looks neat.

## 2. Tool Calling

Tool calling is not magic and it is not the model reaching out on its own. It is a simple loop:

1. your code sends the list of tools
2. the model decides one is needed
3. the model asks for that tool
4. your code runs the tool
5. your code sends the result back
6. the model writes the final answer

That loop is the backbone of many agent systems.

## 3. Worked Example

User asks:

```text
What unresolved tasks are left in notes.txt?
```

The model might ask for a file-reading tool:

```json
{
  "tool_name": "read_file",
  "arguments": {"path": "notes.txt"}
}
```

Your program runs the tool, gets the file content, and sends back something like:

```json
{
  "role": "tool",
  "content": "Task 1: add tests\nTask 2: fix docs"
}
```

Then the model can answer using the actual file instead of guessing.

## 4. Good Tool Design

Good tools are:

- narrow in purpose
- explicit about inputs
- safe to run
- easy to test without a model

If a tool tries to do too many unrelated jobs, it becomes hard to trust.

## 5. Common Confusion

### Tool schema is vague

If the tool description is unclear, the model may send unusable arguments.

### Tool output is too large

If a file reader returns a huge file, the next model step can become noisy. Summarize or chunk the result.

### Tool result is not checked

If a tool returns `None` or malformed data and you pass it onward, the loop becomes brittle.

## 6. What To Practice

- design one tool with clear input and output fields
- simulate a tool call without using a real provider
- validate one structured response before trusting it

Next: [Chapter 3: Context Engineering](./03-context-engineering.md)

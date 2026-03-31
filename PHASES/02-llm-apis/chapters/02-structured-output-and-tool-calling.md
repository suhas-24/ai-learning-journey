# Chapter 2 - Structured Output and Tool Calling

Once you stop asking only for prose, model integration becomes much more powerful. Structured output lets downstream code consume model results. Tool calling lets the model ask your program to fetch or compute something it does not know.

## 1. Structured Output

Suppose you want the model to classify a support ticket. Free-form prose is annoying to parse. A structured target is better.

Desired shape:

```json
{
  "priority": "high",
  "needs_human": true,
  "reason": "Payment issue affects checkout"
}
```

Now your program can validate fields before acting.

### Why validation matters

Models can still produce:

- missing keys
- wrong data types
- extra text around JSON

That is why you validate after generation rather than trusting the model by appearance.

## 2. Tool Calling as a Program Loop

Tool calling is not the model secretly using the internet. It is a handshake:

1. your code sends available tools
2. the model decides a tool is needed
3. the model returns a tool request
4. your code executes the tool
5. your code sends the tool result back
6. the model finishes the answer

That loop is the backbone of many agent systems.

## 3. Worked Example

User asks:

```text
What unresolved tasks are left in notes.txt?
```

The model might say:

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

Then the model can produce a final answer grounded in actual data.

## 4. Good Tool Design

Good tools are:

- narrow in purpose
- explicit about inputs
- safe to run
- easy to test without a model

Bad tools try to do too many unrelated jobs. If your tool is called `do_everything`, your design is already decaying.

## 5. Failure Cases

### Tool schema is vague

If the tool description is ambiguous, the model may supply unusable arguments.

### Tool output is too large

If a file reader returns a 50,000-line file, you may overwhelm the next model step. Summarize or chunk tool results before re-inserting them.

### Tool result is not validated

If a search tool returns `None` or a malformed object and you pass it onward blindly, the rest of the loop becomes brittle.

## 6. What To Practice

- design one tool with clear input and output fields
- simulate a tool call without using a real provider
- validate one structured response before trusting it

Next: [Chapter 3: Context Engineering](./03-context-engineering.md)

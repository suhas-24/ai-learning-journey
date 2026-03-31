# Phase 1 Troubleshooting

## "I keep getting indentation errors"

Python uses indentation as part of the language. One extra space can change what code belongs inside a block. Keep one editor setting and use it consistently.

## "My file works once and fails later"

Check the current working directory. Use `Path(...)` deliberately and print `Path.cwd()` if you are not sure where Python is looking.

## "Why is my loop not changing the original data?"

You may be changing a temporary name instead of the list or dictionary itself. Print the object before and after the loop to see what actually changed.

## "I wrote async code and it looks slower"

Async helps when work spends time waiting. It does not make CPU-heavy work magically faster. Test with I/O-like delays first, as in [async_batch_demo.py](./snippets/async_batch_demo.py).

## "Pydantic is throwing a validation error"

That usually means it is doing its job. Read the error path carefully. It tells you which field is wrong and why the input shape does not match the model.

## "I do not know how to debug without guessing"

Use this order:

1. Reproduce the failure with the smallest input possible.
2. Print or log the value right before the error.
3. Check the type and shape of the data.
4. Write down what you expected versus what happened.

If you follow that loop calmly, debugging gets much less emotional.

# Phase 1 Troubleshooting

## "I keep getting indentation errors"

Python uses indentation as syntax, not decoration. One extra space can change block structure. Keep one editor setting and use it consistently.

## "My file loads in one run and fails in another"

Check the current working directory. Use `Path(...)` deliberately and print `Path.cwd()` if you are unsure where Python is looking.

## "Why is my loop not changing the original data?"

You may be reassigning a local variable instead of updating the list or dictionary itself. Print the object before and after the loop to see what actually changed.

## "I wrote async code and it looks slower"

Async helps when work spends time waiting. It does not make CPU-heavy work magically faster. Test with I/O-like delays first, as in [async_batch_demo.py](./snippets/async_batch_demo.py).

## "Pydantic is throwing a validation error"

That usually means it is doing its job. Read the error path carefully. It tells you which field is wrong and why the input shape does not match the model.

## "I do not know how to debug without guessing"

Use this order:

1. reproduce the failure with the smallest input possible
2. print or log the value right before the error
3. check the type and shape of the data
4. write down what you expected versus what happened

If you follow that loop calmly, debugging gets much less emotional.

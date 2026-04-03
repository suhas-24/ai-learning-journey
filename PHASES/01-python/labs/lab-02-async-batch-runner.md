# Lab 2 - Build an Async Batch Runner

This lab teaches the first useful async idea without needing an API key or a real network call. It is about learning how waiting can happen more efficiently.

**Async** means the program can start waiting on one task and then work on other tasks while that waiting happens. A **network call** is a request to another computer, but we will only pretend here with timers.

## Goal

Simulate three slow jobs and run them together so the total runtime is closer to the slowest job, not the sum of all jobs.

That is the main win of async: waiting can overlap instead of happening one after another.

## Why This Matters

Later phases wait on APIs, tools, file lookups, and evaluation jobs. Async helps one task wait while another continues.

## Step 1 - Start From This Shape

```python
import asyncio


async def run_job(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name} finished in {delay} seconds"
```

`async def` creates an async function, and `await` means "pause here until this waiting task is done."

## Step 2 - Run Jobs Together

Use `asyncio.gather(...)` to start several jobs at once.

```python
results = await asyncio.gather(
    run_job("job-1", 1.0),
    run_job("job-2", 2.0),
    run_job("job-3", 1.5),
)
```

`gather` collects several async tasks and waits for all of them to finish.

## Step 3 - Compare Against Sequential Code

Run the same jobs one after another and compare the total time.

Sequential code means one task finishes before the next one starts.

## What To Notice

- async changes waiting behavior, not your business logic
- `await` appears inside `async def`
- `asyncio.run(...)` starts a standalone async program

`asyncio.run(...)` creates the event loop for this one program. An **event loop** is the manager that keeps track of which async task is waiting and which one can run next. You can picture it as the person in charge of the queue.

## Failure Cases To Trigger

- forget `await` and look at the warning
- call `asyncio.run(...)` from inside another event loop
- pass a normal function into `gather` and inspect the error

When those mistakes happen, they are showing you the boundaries of async in a very direct way.

These are not random mistakes. They show what async expects so you can recognize the shape of a correct program.

## Reference Snippet

Use [async_batch_demo.py](../snippets/async_batch_demo.py) after you try it yourself first.

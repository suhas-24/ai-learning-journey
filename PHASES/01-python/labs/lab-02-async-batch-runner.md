# Lab 2 - Build an Async Batch Runner

This lab teaches the first useful async mental model without needing a real API.

## Goal

Simulate three slow jobs and run them concurrently so total runtime is closer to the slowest task, not the sum of every task.

## Why This Matters

Later phases call APIs, tools, retrievers, and evaluation jobs. Those steps often wait on network responses. Async lets one task wait while another keeps moving.

## Step 1 - Start From This Shape

```python
import asyncio


async def run_job(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name} finished in {delay} seconds"
```

## Step 2 - Run Jobs Together

Use `asyncio.gather(...)` to start several jobs.

Expected pattern:

```python
results = await asyncio.gather(
    run_job("job-1", 1.0),
    run_job("job-2", 2.0),
    run_job("job-3", 1.5),
)
```

## Step 3 - Compare Against Sequential Code

Run the same jobs one after another and compare the total time.

## What To Notice

- async changes waiting behavior, not your business logic
- `await` appears inside `async def`
- `asyncio.run(...)` is the outer entry point for a standalone script

## Failure Cases To Trigger

- forget `await` and observe the coroutine warning
- call `asyncio.run(...)` from inside an already running event loop
- pass a normal function into `gather` and inspect the error

## Reference Snippet

Use [async_batch_demo.py](../snippets/async_batch_demo.py) as a working reference after you try it yourself first.

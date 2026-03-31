# Lab 2 - Build an Async Batch Runner

This lab teaches the first useful async idea without needing an API key or a real network call.

## Goal

Simulate three slow jobs and run them together so the total runtime is closer to the slowest job, not the sum of all jobs.

## Why This Matters

Later phases wait on APIs, tools, file lookups, and evaluation jobs. Async helps one task wait while another continues.

## Step 1 - Start From This Shape

```python
import asyncio


async def run_job(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name} finished in {delay} seconds"
```

## Step 2 - Run Jobs Together

Use `asyncio.gather(...)` to start several jobs at once.

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
- `asyncio.run(...)` starts a standalone async program

## Failure Cases To Trigger

- forget `await` and look at the warning
- call `asyncio.run(...)` from inside another event loop
- pass a normal function into `gather` and inspect the error

## Reference Snippet

Use [async_batch_demo.py](../snippets/async_batch_demo.py) after you try it yourself first.

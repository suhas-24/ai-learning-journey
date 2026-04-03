"""Show how async lets several waiting tasks overlap instead of running one by one."""

import asyncio
from time import perf_counter


async def run_job(name: str, delay: float) -> str:
    # Sleep is a simple stand-in for waiting on a slow outside task.
    await asyncio.sleep(delay)
    return f"{name} finished in {delay} seconds"


async def main() -> None:
    start = perf_counter()
    # Start all three jobs at the same time so waiting overlaps.
    results = await asyncio.gather(
        run_job("job-1", 1.0),
        run_job("job-2", 2.0),
        run_job("job-3", 1.5),
    )
    duration = perf_counter() - start

    # Print both the result and the total time so the benefit is visible.
    print("\n".join(results))
    print(f"Total runtime: {duration:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())

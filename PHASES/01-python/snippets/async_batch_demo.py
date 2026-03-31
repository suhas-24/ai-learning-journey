import asyncio
from time import perf_counter


async def run_job(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name} finished in {delay} seconds"


async def main() -> None:
    start = perf_counter()
    results = await asyncio.gather(
        run_job("job-1", 1.0),
        run_job("job-2", 2.0),
        run_job("job-3", 1.5),
    )
    duration = perf_counter() - start

    print("\n".join(results))
    print(f"Total runtime: {duration:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())

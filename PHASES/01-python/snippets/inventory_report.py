"""Load a JSON file, check the shape, and print a small inventory summary."""

import json
from pathlib import Path


def load_items(path: Path) -> list[dict]:
    # Check the file before reading so the error is easy to understand.
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")

    # Read the file as text, then turn the JSON text into Python data.
    data = json.loads(path.read_text(encoding="utf-8"))

    # This example expects a list at the top level.
    if not isinstance(data, list):
        raise ValueError("Expected a list of inventory records")

    return data


def summarize_items(items: list[dict]) -> dict[str, int]:
    in_stock = 0

    for item in items:
        # Treat missing counts as zero so one bad record does not crash the whole summary.
        if item.get("count", 0) > 0:
            in_stock += 1

    return {
        "total_items": len(items),
        "in_stock": in_stock,
        "out_of_stock": len(items) - in_stock,
    }


def main() -> None:
    # This is the file the program will read by default.
    inventory_path = Path("inventory.json")

    items = load_items(inventory_path)
    summary = summarize_items(items)

    # Print the final answer in a human-friendly shape.
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

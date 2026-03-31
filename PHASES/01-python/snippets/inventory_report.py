from pathlib import Path
import json


def load_items(path: Path) -> list[dict]:
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")

    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Expected a list of inventory records")
    return data


def summarize_items(items: list[dict]) -> dict[str, int]:
    in_stock = 0

    for item in items:
        if item.get("count", 0) > 0:
            in_stock += 1

    return {
        "total_items": len(items),
        "in_stock": in_stock,
        "out_of_stock": len(items) - in_stock,
    }


def main() -> None:
    inventory_path = Path("inventory.json")
    items = load_items(inventory_path)
    summary = summarize_items(items)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

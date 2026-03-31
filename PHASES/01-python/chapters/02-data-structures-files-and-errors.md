# Chapter 2 - Data Structures, Files, and Errors

Real AI scripts do not just calculate values in memory. They load config, read prompts, inspect API responses, and write results back to disk. This chapter connects Python data structures to real program behavior.

## 1. Lists, Dictionaries, Sets, and Tuples

### Lists

Lists are ordered collections.

```python
models = ["small", "medium", "large"]
print(models[0])  # small
```

Use a list when order matters or duplicates are allowed.

### Dictionaries

Dictionaries map keys to values.

```python
request = {
    "model": "reasoning-mini",
    "temperature": 0.2,
    "stream": True,
}
```

Use a dictionary when you want named fields instead of positions.

### Sets

Sets store unique values.

```python
tags = {"python", "llm", "python"}
print(tags)  # {"python", "llm"}
```

Useful for deduplication.

### Tuples

Tuples are ordered like lists but meant to stay unchanged.

```python
coordinate = (12.9, 77.6)
```

Use them when the position has stable meaning.

## 2. Reading and Writing JSON

JSON is everywhere in AI engineering: config files, request payloads, tool results, and logs.

```python
import json
from pathlib import Path

config_path = Path("config.json")

config = {
    "project_name": "habit-tracker",
    "retry_limit": 3,
}

config_path.write_text(json.dumps(config, indent=2), encoding="utf-8")

loaded = json.loads(config_path.read_text(encoding="utf-8"))
print(loaded["project_name"])
```

### Failure case: assuming the file exists

This crashes if the file is missing:

```python
Path("missing.json").read_text()
```

Safer version:

```python
path = Path("missing.json")
if not path.exists():
    print("Config file not found")
```

## 3. Exceptions Are Feedback

An exception means Python detected a problem it could not safely ignore.

```python
def divide(total: int, count: int) -> float:
    return total / count
```

If `count` is `0`, Python raises `ZeroDivisionError`.

That is good news. Silent wrong answers are worse than visible failures.

### Catch expected failures, not everything

```python
try:
    count = int(input("How many items? "))
except ValueError:
    print("Please enter a whole number.")
```

Avoid broad error handling like this:

```python
try:
    risky_code()
except Exception:
    pass
```

That hides useful debugging information.

## 4. Worked Example: Load Tasks from a File

```python
import json
from pathlib import Path


def load_tasks(path: Path) -> list[dict]:
    if not path.exists():
        raise FileNotFoundError(f"Task file not found: {path}")

    raw_text = path.read_text(encoding="utf-8")
    data = json.loads(raw_text)

    if not isinstance(data, list):
        raise ValueError("Task file must contain a list")

    return data
```

This function checks:

- file presence
- JSON parsing
- top-level shape

That pattern matters. In AI systems, data often arrives from outside your control. Validation is part of the feature, not extra polish.

## 5. Pathlib Is Better Than Hand-Built Strings

Use `Path` objects instead of manually stitching file paths.

```python
from pathlib import Path

project_dir = Path("reports")
report_file = project_dir / "summary.json"
```

This is clearer and safer than `"reports/" + filename`.

## 6. What To Practice Before Moving On

- create a JSON file, load it, and print one field
- write a function that rejects invalid data with a clear error
- use a set to remove duplicates from a list

Next: [Chapter 3: From Script to Project](./03-from-script-to-project.md)

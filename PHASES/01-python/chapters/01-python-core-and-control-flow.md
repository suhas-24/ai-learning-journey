# Chapter 1 - Python Core and Control Flow

This chapter is about learning how Python thinks. If you understand values, variables, conditions, loops, and functions, later AI code stops looking magical and starts looking mechanical.

## 1. Values and Variables

A value is data. A variable is a name attached to data.

```python
name = "Suhas"
task_count = 3
is_ready = False
```

Python does not force you to write types beside variables, but the value still has a type. That type affects what operations are allowed.

```python
task_count + 2      # valid
name.upper()        # valid
task_count.upper()  # error: integers do not have .upper()
```

The beginner skill is not memorizing every type. It is asking: "What kind of thing is this value, and what can I safely do with it?"

## 2. Conditions

Conditions let your program choose a path.

```python
score = 82

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
else:
    grade = "C"
```

Read this as: evaluate the first condition, then the next one only if the first failed, then fall back to `else`.

### Common failure case

This code crashes:

```python
age = "18"
if age >= 18:
    print("adult")
```

Why? Because `"18"` is a string and `18` is an integer. Convert first:

```python
age = int("18")
if age >= 18:
    print("adult")
```

## 3. Loops

Loops let you repeat work.

```python
tasks = ["read docs", "write notes", "run test"]

for task in tasks:
    print(task)
```

Use a `for` loop when you want to walk through a collection. Use a `while` loop when you want to repeat until a condition changes.

```python
countdown = 3

while countdown > 0:
    print(countdown)
    countdown -= 1
```

### Worked example: count completed tasks

```python
tasks = [
    {"title": "Read chapter", "done": True},
    {"title": "Run snippet", "done": False},
    {"title": "Take notes", "done": True},
]

completed = 0

for task in tasks:
    if task["done"]:
        completed += 1

print(f"Completed: {completed}/{len(tasks)}")
```

What this teaches:

- a list can hold dictionaries
- a loop can inspect one item at a time
- a condition can decide when to update a counter

## 4. Functions

Functions package logic into reusable steps.

```python
def format_task(title: str, done: bool) -> str:
    status = "done" if done else "todo"
    return f"[{status}] {title}"
```

Good beginner functions usually do one job:

- transform data
- decide a result
- print or return one meaningful output

### Failure case: printing instead of returning

This function is harder to reuse:

```python
def add(a, b):
    print(a + b)
```

This version is better:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Returned values can be tested, combined, or stored. Printed values are mostly for humans.

## 5. A Small Worked Program

```python
def summarize_scores(scores: list[int]) -> dict[str, float]:
    if not scores:
        raise ValueError("scores list cannot be empty")

    total = sum(scores)
    average = total / len(scores)
    highest = max(scores)

    return {
        "total": total,
        "average": average,
        "highest": highest,
    }


result = summarize_scores([78, 92, 85])
print(result)
```

This one function introduces:

- parameters
- a guard clause
- list processing
- returning a dictionary

## 6. What To Practice Before Moving On

- write a function that takes a list of names and returns only names longer than 5 characters
- write a loop that counts how many numbers are even
- make one bug on purpose, then explain why Python complains

Next: [Chapter 2: Data Structures, Files, and Errors](./02-data-structures-files-and-errors.md)

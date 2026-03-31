# Chapter 1 - Python Core and Control Flow

Python is a language for giving a computer small, exact instructions. This chapter starts with the smallest pieces: values, names, choices, repetition, and reusable steps.

## 1. Values and Variables

A **value** is a piece of data. A **variable** is a name that points to a value.

```python
name = "Suhas"
task_count = 3
is_ready = False
```

Here is the plain-language version:

- `"Suhas"` is text
- `3` is a whole number
- `False` is a true/false value

Python lets you store different kinds of values without writing a type label every time. That is convenient, but the value still has a type. A type tells Python what operations make sense.

```python
task_count + 2      # works because both sides are numbers
name.upper()        # works because text has uppercase methods
task_count.upper()  # does not work because numbers are not text
```

The beginner habit is to ask:

- what kind of value is this?
- what can I safely do with it?
- what will happen if I use it the wrong way?

## 2. Conditions

A **condition** lets a program choose between paths.

```python
score = 82

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
else:
    grade = "C"
```

Read that code slowly:

- check the first question
- if it is false, check the next one
- if none of the questions are true, use the `else` branch

### Common confusion

This fails:

```python
age = "18"
if age >= 18:
    print("adult")
```

Why? Because `"18"` is text and `18` is a number. Python does not guess your intent. Convert the text first:

```python
age = int("18")
if age >= 18:
    print("adult")
```

When Python throws an error here, it is helping you notice that your data type is wrong.

## 3. Loops

A **loop** repeats work.

```python
tasks = ["read docs", "write notes", "run test"]

for task in tasks:
    print(task)
```

Use a `for` loop when you want to visit each item in a collection. Use a `while` loop when you want to keep going until a condition changes.

```python
countdown = 3

while countdown > 0:
    print(countdown)
    countdown -= 1
```

### Worked example

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

This shows three useful ideas at once:

- a list can hold many items
- each item can itself be a dictionary
- a condition can decide whether to update a counter

## 4. Functions

A **function** is a named block of code that does one job.

```python
def format_task(title: str, done: bool) -> str:
    status = "done" if done else "todo"
    return f"[{status}] {title}"
```

Good beginner functions usually do one clear thing:

- transform data
- make a decision
- return a result

### Common confusion

This version is harder to reuse:

```python
def add(a, b):
    print(a + b)
```

This version is better:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Why? Because returned data can be stored, tested, or passed into another function. Printed output is mostly for people reading the screen.

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

This one function gives you the basic shape of many real programs:

- take input
- check that it is valid
- do the main work
- return structured output

## 6. What To Practice Before Moving On

- write a function that keeps only names longer than five characters
- write a loop that counts how many numbers are even
- make one bug on purpose and explain the error message in plain language

Next: [Chapter 2: Data Structures, Files, and Errors](./02-data-structures-files-and-errors.md)

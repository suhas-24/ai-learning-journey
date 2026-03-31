# Command Cheat Sheet

These are the commands that appear over and over in the learning journey.

The point is not to memorize these all at once. The point is to know where to look when you want the computer to tell you what is happening.

## Navigation

```bash
pwd
ls -la
cd /path/to/project
```

## Git

```bash
git status --short --branch
git add path/to/file
git commit -m "message"
git push
git pull --rebase
```

## Python

```bash
python3 --version
python3 script.py
python3 -m pip install package-name
```

## Poetry

```bash
poetry install
poetry add package-name
poetry run python script.py
poetry run pytest
```

## Search And Inspection

```bash
rg "pattern" .
rg --files
sed -n '1,200p' file.md
```

## Why These Matter

The point is not memorizing commands mechanically. The point is to reduce friction so the real learning energy can go into concepts and building.

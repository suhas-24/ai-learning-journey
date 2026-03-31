# Command Cheat Sheet

These are the commands that appear over and over in the learning journey.

The point is not to memorize them all at once. The point is to know where to look when you want the computer to tell you what is happening.

## Navigation

`pwd` shows your current folder. `ls -la` lists the files in the current folder. `cd /path/to/project` moves you into a folder.

```bash
pwd
ls -la
cd /path/to/project
```

## Git

Git is the tool that keeps track of file changes over time.

`git status --short --branch` shows what changed. `git add` stages a file. `git commit` saves a checkpoint. `git push` sends your commits to GitHub. `git pull --rebase` brings in newer changes while keeping history tidy.

```bash
git status --short --branch
git add path/to/file
git commit -m "message"
git push
git pull --rebase
```

## Python

Python is the programming language used throughout much of this repo.

`python3 --version` shows the installed version. `python3 script.py` runs a script. `python3 -m pip install package-name` installs a package.

```bash
python3 --version
python3 script.py
python3 -m pip install package-name
```

## Poetry

Poetry is a tool for managing Python projects.

`poetry install` installs dependencies. `poetry add package-name` adds a dependency. `poetry run python script.py` runs a script inside the project environment. `poetry run pytest` runs tests.

```bash
poetry install
poetry add package-name
poetry run python script.py
poetry run pytest
```

## Search And Inspection

`rg` searches text quickly. `rg --files` lists files. `sed -n '1,200p' file.md` prints part of a file so you can inspect it.

```bash
rg "pattern" .
rg --files
sed -n '1,200p' file.md
```

## Why These Matter

The point is not memorizing commands mechanically.

The point is to reduce friction so the real learning energy can go into concepts and building.

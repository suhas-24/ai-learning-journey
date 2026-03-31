# Problems And Solutions

This is the debugging handbook for the journey. Every useful engineer develops a private memory of failure modes; this file makes that memory explicit.

A good stuck entry is not a complaint log. It is a precise record of a mismatch between expectation and reality.

## What Belongs Here

- bugs that took time to understand
- environment issues that blocked progress
- conceptual confusion that became clear after a breakthrough
- mistakes caused by rushing, guessing, or skipping fundamentals

## What Makes A Good Stuck Entry

- the problem is specific enough that I could reproduce it later
- the attempts I made are recorded, not just the final fix
- the root cause is named, not hidden behind the solution
- the lesson is reusable in a future phase
- the entry helps future-me avoid wasting time again

## How To Write A Good Entry

Capture five things:

- the exact problem
- what you tried first
- what finally worked
- the root cause
- the lesson to carry into the next phase

---

## 2026-03-29 - GitHub publishing blocked by missing local setup
**Phase:** Pre-Phase 1  
**The Problem:** The machine had no working `gh` login flow ready, and the workspace was not a git repo yet.  
**What I Tried:** Checked for `gh`, checked auth status, inspected git config, and searched for existing GitHub credentials.  
**The Solution:** Installed `gh`, used a PAT for authenticated GitHub API calls, created the repos directly, then initialized and pushed both local repositories.  
**Root Cause:** Publishing was assumed to be "one command away," but the machine was missing part of the GitHub toolchain.  
**Lesson:** Before planning a publish flow, verify CLI availability, authentication, and repo state first.

### 2026-03-29 - Poetry was missing during validation
**Phase:** Pre-Phase 1  
**The Problem:** `poetry install` was required for validation, but Poetry was not installed on the machine.  
**What I Tried:** Checked `poetry --version` and confirmed the command was unavailable.  
**The Solution:** Installed Poetry with `python3 -m pip install poetry`, then re-ran validation successfully.  
**Root Cause:** The repo was created faster than the local Python tooling baseline.  
**Lesson:** Treat dependency managers as part of the project contract, not an optional convenience.

### 2026-03-29 - Python HTTPS requests failed with local SSL verification
**Phase:** Pre-Phase 1  
**The Problem:** Python's `urllib` calls to GitHub failed with certificate verification errors on this machine.  
**What I Tried:** Attempted authenticated API access through Python first.  
**The Solution:** Switched the GitHub API calls to `curl`, which used the system trust chain correctly.  
**Root Cause:** Local Python certificate configuration was not aligned with the system certificate store.  
**Lesson:** When a networking issue looks environmental, test the same request with another client before assuming the API is the problem.

### 2026-03-31 - Large curriculum updates need tighter module boundaries
**Phase:** Pre-Phase 1  
**The Problem:** The repository is growing large enough that editing everything in one window risks losing detail.  
**What I Tried:** Split the work into coordination files and separate module ownership.  
**The Solution:** Use parallel workers with clear ownership instead of one giant editing pass.  
**Root Cause:** Context compression becomes a real risk once the notes become rich.  
**Lesson:** The repo needs modular ownership as much as it needs content quality.

### 2026-03-31 - Local markdown links worked here but broke on GitHub
**Phase:** Pre-Phase 1  
**The Problem:** Some rewritten notes used absolute filesystem paths, which made links usable locally but broken in the hosted repository.  
**What I Tried:** Searched the repo for local path prefixes and traced them back to the generated markdown.  
**The Solution:** Replaced local absolute links with relative repo links and added index pages so navigation works both locally and on GitHub.  
**Root Cause:** Repo content inherited assistant-style file references instead of repository-style markdown links.  
**Lesson:** Files written into a repo must be validated for GitHub compatibility, not only local readability.

### 2026-03-31 - Beginner vocabulary needed to be defined before it appeared
**Phase:** Pre-Phase 1  
**The Problem:** The repo could still feel like it assumed terms such as `LLM` and `tokenization` were already known.  
**What I Tried:** Re-read the top-level docs from the point of view of someone with zero AI background and looked for first-use definitions.  
**The Solution:** Added plain-language definitions and a glossary path so the beginner can build vocabulary in order.  
**Root Cause:** It is easy for writing to drift into field shorthand once the structure is in place.  
**Lesson:** The first time a new term appears, it should be explained simply right there.

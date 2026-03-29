# Problems And Solutions

This is the debugging handbook for the journey. Every useful engineer develops a private memory of failure modes; this file makes that memory explicit.

## What Belongs Here

- bugs that took time to understand
- environment issues that blocked progress
- conceptual confusion that became clear after a breakthrough
- mistakes caused by rushing, guessing, or skipping fundamentals

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

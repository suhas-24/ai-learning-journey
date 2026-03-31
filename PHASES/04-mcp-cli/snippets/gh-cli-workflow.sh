#!/usr/bin/env bash
set -euo pipefail

# Keep the script flexible by letting the caller provide the repo, title, and body.
repo="${1:-OWNER/TEST_REPO}"
title="${2:-Lab: compare tool surfaces}"
body="${3:-Created through the CLI workflow.}"

# First confirm that the command-line tool is ready.
gh auth status >/dev/null
# Then create the issue with a bounded label list.
gh issue create \
  --repo "$repo" \
  --title "$title" \
  --body "$body" \
  --label "experiment"

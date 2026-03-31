#!/usr/bin/env bash
set -euo pipefail

repo="${1:-OWNER/TEST_REPO}"
title="${2:-Lab: compare tool surfaces}"
body="${3:-Created through the CLI workflow.}"

gh auth status >/dev/null
gh issue create \
  --repo "$repo" \
  --title "$title" \
  --body "$body" \
  --label "experiment"

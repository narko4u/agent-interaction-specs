#!/usr/bin/env bash
# Repo-specific checks for agent-interaction-specs (run by .github/scripts/validate.py)
set -euo pipefail

if [ -d aip/go ]; then
  ( cd aip/go
    unformatted="$(gofmt -l .)"
    if [ -n "$unformatted" ]; then
      echo "gofmt required for:"; echo "$unformatted"; exit 1
    fi
    go build ./...
    go vet ./...
    echo "go module builds, vets and is gofmt-clean"
  )
fi

PYTHONPATH=aci/py/src python3 -c "import aci, aci.schema; print('aci package imports OK')"

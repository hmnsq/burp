#!/usr/bin/env bash
# verify.sh: BURP's gate; nothing is released unless every test passes.
set -uo pipefail
cd "$(dirname "$0")/.."
PYTHONPATH="$PWD/src" python3 -m pytest -q tests

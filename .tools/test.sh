#!/bin/sh
set -e

cd "$(dirname "$0")/.."

(cd example && properdocs build -q --strict)
grep -q adjacent site/index.html

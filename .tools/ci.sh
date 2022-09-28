#!/bin/sh
set -e

cd "$(dirname "$0")/.."

with_groups() {
    echo "::group::$@"
    "$@" && echo "::endgroup::"
}

"$@" autoflake -i -r --remove-all-unused-imports --remove-unused-variables mkdocs_same_dir
"$@" isort -q mkdocs_same_dir
"$@" black -q mkdocs_same_dir

(cd example && "$@" mkdocs build -q --strict)
"$@" grep -q adjacent site/index.html

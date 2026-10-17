#!/usr/bin/env bash
set -euo pipefail

exclude=(".git")

is_excluded() {
    for e in "${exclude[@]}"; do
        [[ "$1" == "$e" ]] && return 0
    done
    return 1
}

for dir in */; do
    dirname="${dir%/}"
    if is_excluded "$dirname"; then
        continue
    fi
    rm -f "$dirname.skill" "$dirname.zip"
    # Do not package the user's private copy of the ASD-STE100 standard.
    zip -r "$dirname.zip" "./$dirname" \
        -x '*/references/official/ASD-STE100*' '*/__pycache__/*'
    mv "$dirname.zip" "$dirname.skill"
done

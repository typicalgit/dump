#!/bin/bash

if [ -z "$*" ]; then
  echo "No question passed"
  exit 1
fi

quest="$*"

ans="$(sgpt "$quest")"
echo "$ans"
espeak "$ans"

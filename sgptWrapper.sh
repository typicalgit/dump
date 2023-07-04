#!/bin/bash

if [ -z "$*" ]; then
  echo "no question asked"
  exit 0
fi

quest="$*"
echo "$quest"

ans=$(sgpt "$quest")
echo "$ans"

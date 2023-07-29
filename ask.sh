#!/bin/bash

q="$@"
q="'"$q"'"

a="$(tgpt -q "$q")"
echo "$a"
espeak "$a"

#!/bin/bash

# Check if two file names are provided as arguments
if [ $# -ne 2 ]; then
  echo "Usage: $0 <file1> <file2>"
  exit 1
fi

file1=$1
file2=$2

# Check if both files exist
if [ ! -f "$file1" ]; then
  echo "File '$file1' does not exist."
  exit 1
fi

if [ ! -f "$file2" ]; then
  echo "File '$file2' does not exist."
  exit 1
fi

# Combine the two files and remove duplicate lines
cat "$file1" "$file2" | sort -u > combined.txt

echo "Combined file created: combined.txt"

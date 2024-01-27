#!/bin/bash

# Check if a file name is provided as an argument
if [ $# -eq 0 ]; then
    echo "Please provide a file name as an argument."
    exit 1
fi

# Check if the file exists
if [ ! -f "$1" ]; then
    echo "File not found."
    exit 1
fi

# Create a temporary file to store the modified lines
temp_file=$(mktemp)

# Read each line from the input file, modify it, and write to the temporary file
while IFS= read -r line; do
    modified_line="($line)"
    echo "$modified_line" >> "$temp_file"
done < "$1"

# Replace the original file with the modified lines
mv "$temp_file" "$1"

echo "File modified successfully."

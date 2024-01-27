#!/bin/bash

# Path to the text file containing lines to search
search_file="path/to/search_file.txt"

# Path to the text file to search in
target_file="path/to/target_file.txt"

# Loop through each line in the search file
while IFS= read -r line; do
    # Search for the line as a substring in the target file
    if grep -q "$line" "$target_file"; then
        echo "Substring '$line' found in target file"
    else
        echo "Substring '$line' not found in target file"
    fi
done < "$search_file"

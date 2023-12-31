#!/usr/bin/env python3
import sys
import random

# Check if arguments are passed
if len(sys.argv) < 2:
    print("Please provide arguments to choose from.")
    sys.exit(1)

# Get the list of arguments
arguments = sys.argv[1:]

# Choose a random argument
random_argument = random.choice(arguments)

# Print the randomly chosen argument
print("Randomoice:", random_argument)

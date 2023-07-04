#!/bin/bash

# Get the current time in minutes
MINUTES=$(date +%M)

# Round the minutes to the nearest 5
ROUNDED=$(( (MINUTES + 2) / 5 * 5 ))

# Convert the rounded minutes to words
case $ROUNDED in
    0|60) TIME="$(date +%l)";;
    5) TIME="five past $(date +%l)";;
    10) TIME="ten past $(date +%l)";;
    15) TIME="quarter past $(date +%l)";;
    20) TIME="twenty past $(date +%l)";;
    25) TIME="twenty-five past $(date +%l)";;
    30) TIME="half past $(date +%l)";;
    35) TIME="twenty-five to $(date -d '+1 hour' +%l)";;
    40) TIME="twenty to $(date -d '+1 hour' +%l)";;
    45) TIME="quarter to $(date -d '+1 hour' +%l)";;
    50) TIME="ten to $(date -d '+1 hour' +%l)";;
    55) TIME="five to $(date -d '+1 hour' +%l)";;
esac

espeak -g 7 "its $TIME"

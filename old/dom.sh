#!/bin/bash

day=$(date +%-d)

if [[ ${day: -1} -eq 1 && ${day} -ne 11 ]]; then
  suffix="${day}st"
elif [[ ${day: -1} -eq 2 && ${day} -ne 12 ]]; then
  suffix="${day}nd"
elif [[ ${day: -1} -eq 3 && ${day} -ne 13 ]]; then
  suffix="${day}rd"
else
  suffix="${day}th"
fi
echo $suffix

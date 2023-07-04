#!/bin/bash
# SPEAK THE DATE
# THE FIRST ARGUMENT SHOULD BE THE VOLUME
# VOLUME IS 0-200, 100 IS DEFAULT

vol=$1

#IF NO VOLUME USE DEFAULT
if [ "$vol" == '' ]
  then vol=100
fi

day=$(date +%-d)
month=$(date +%B)

#GET CORRECT SUFFIX FOR DAY OF MONTH. E.G "st"
if [[ ${day: -1} -eq 1 && ${day} -ne 11 ]]; then
  suffix="${day}st "
elif [[ ${day: -1} -eq 2 && ${day} -ne 12 ]]; then
  suffix="${day}nd"
elif [[ ${day: -1} -eq 3 && ${day} -ne 13 ]]; then
  suffix="${day}rd"
else
  suffix="${day}th"
fi

#SPEAK THE DAY OF MONTH AND THE MONTH
# -g SETS WORD SPACING, -a SETS AMPLITUDE
espeak -v mb-en1 -g 6 -a $vol "its the $suffix of $month"


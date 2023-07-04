#!/usr/bin/env bash
vol="$1"

if [ "$vol" == '' ]
  then vol=100
fi

espeak -g 8 -a $vol "its $(date +%H:%M)"

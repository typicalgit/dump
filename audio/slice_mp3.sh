#!/bin/bash

infile="$1"
start="$2"
time="$3"
outfile="$4"

if [ $time = 0 ]; then
  ffmpeg -ss $start -i $infile -acodec copy $outfile
else
  ffmpeg -ss $start -i $infile -t $time -acodec copy $outfile

fi


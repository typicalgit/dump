#!/bin/bash

inFile="$1"
start="$2"
end="$3"
outFile="$4"

ffmpeg -i $inFile -ss $start -t $end $outFile

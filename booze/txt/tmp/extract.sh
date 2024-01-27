#!/bin/bash

start_line=$1
end_line=$(($2 - 1))
filename=$3

sed -n "${start_line},${end_line}p" "$filename"

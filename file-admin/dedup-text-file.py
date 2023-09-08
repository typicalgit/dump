#!/bin/python3
import sys

file_path = sys.argv[1]

with open(file_path,"r") as file:
  file_lines = file.readlines()
file.close

with open(file_path + ".dedup","w") as file_out:
  dedup = []
  for file_line in file_lines:
    dupe_flag = 0
    for uniq_line in dedup:
      if uniq_line == file_line:
        dupe_flag = 1
    if dupe_flag == 0:
      dedup.append(file_line)
  file_out.writelines(dedup)
file_out.close

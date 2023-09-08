#!/bin/python3
import glob
import os

cwd = os.getcwd()

sorted_files = sorted(
  glob.glob(cwd + '/*'), key=os.path.getmtime)

for i, f in enumerate(sorted_files, 1):
  try:
    head, tail = os.path.split(f)            
    if tail[1] == ' ':
      os.rename(f, os.path.join(head,"0" + tail))
  except OSError:
    print('Invalid operation')


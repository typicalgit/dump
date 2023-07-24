import os

directory = os.fsencode(directory_in_str)
    
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".asm") or filename.endswith(".py"): 
         # print(os.path.join(directory, filename))
         continue
     else:
         continue

#RECURSIVE
from pathlib import Path

pathlist = Path(directory_in_str).glob('**/*.asm')
for path in pathlist:
  # because path is object not string
  path_in_str = str(path)
  # print(path_in_str)

Use rglob to replace glob('**/*.asm') with rglob('*.asm')
This is like calling Path.glob() with '**/' added in front of the given relative pattern:

from pathlib import Path

pathlist = Path(directory_in_str).rglob('*.asm')
for path in pathlist:
  # because path is object not string
  path_in_str = str(path)
  # print(path_in_str)


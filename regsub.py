#!/bin/python
import argparse
import re
import sys
import os

parser = argparse.ArgumentParser(  
prog = "rgxsub",
description = 'Search and replace using regex groups',
epilog = "I'm an epilepilepilog(ue)"
)
parser.add_argument(
  'mandArgs', 
  metavar='[input str] [search] [repl]', 
  type=str,
  nargs=3,
  help='the replacement pattern')
parser.add_argument(
  '-o', 
  default=sys.stdout, 
  type=argparse.FileType('w'), 
  help='the file where the output should be written')

args = parser.parse_args()

input = args.mandArgs[0]
find = args.mandArgs[1]
repl = args.mandArgs[2]

if os.path.exists(input):
  with open(input,"r") as file:
    input = file.read()
    file.close()

reFind = re.compile(find)

out = reFind.sub(repl,input)

args.o.write(out)
print()

args.o.close()


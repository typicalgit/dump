#!/bin/python
import subprocess
import argparse
import random
import sys
import math

minPwdLength = 0
maxPwdLength = 0
specialChars = 0
easySpecialChars = ["!","$","-",".",",",":"]
pwdLength = 0
options = ""

def FN_addEasySpecialChars(pwd):
  numSpecial = 0
  pwdLength = len(pwd)
  randDenom = random.randint(3,9)
  outPwd = pwd
  if pwdLength < 10:
    pwdLength = 10

  numSpecial = math.floor(pwdLength * ( 1 / randDenom ))
  for i in range(numSpecial):
    randPosition = random.randint(0,len(pwd))
    randChar = random.choice(easySpecialChars)
    seg1 = outPwd[:randPosition - 1]
    seg2 = outPwd[randPosition:]
    outPwd = seg1 + randChar + seg2
  return outPwd

parser = argparse.ArgumentParser(  
description='Generate a password and output to file'
)
parser.add_argument(
  '--min', 
  metavar='minimum length', 
  type=int,
  help='minimum password length')
parser.add_argument(
  '--max', 
  metavar='maximum length', 
  type=int,
  help='the maximum length of the password')
parser.add_argument(
  '--fixed', 
  metavar='exact password length', 
  type=int,
  help='specify a fixed length for your password')
parser.add_argument(
  '--special', 
  metavar='use special chars', 
  action='store_const',
  const=True,
  help='Add special characters. Any special characters may be used')
parser.add_argument(
  '--easy', 
  metavar='use more consistant special chars', 
  action='store_const',
  const=True,
  help='Add special characters that are the same between most devices on UK or US keyboard layouts')
parser.add_argument(
  '-o', 
  default=sys.stdout, 
  type=argparse.FileType('w'), 
  help='The file to output password into, if blank then stdout is used')

args = parser.parse_args()

minPwdLength = args.min
maxPwdLength = args.max
if args.fixed:
  pwdLength = args.fixed
elif args.min != None and args.max != None:
  pwdLength = random.randint(minPwdLength,maxPwdLength)
else:
  print("Buggeh, summat not rite... Maybeh you didn't add min and max lengths or a fixed length")
  exit

pwdLength = str(pwdLength)

if args.special:
  options = '-sy'
else:
  options = '-s'

pwd = subprocess.run(["pwgen",options,pwdLength,"1"],capture_output=True)

outPwd = pwd.stdout.decode("utf-8")
outPwd = outPwd.replace('\n','')

if args.easy:
  outPwd = FN_addEasySpecialChars(outPwd)

args.o.write(outPwd)
args.o.close()


#!/usr/bin/env python3
import os
import subprocess
import random
import math

maxLines = 0  # max tracks in lastPlayed list
cntTracks = 0 # count of mp3 files in dir
delLines = 0  # nr of lines above max => delete
tracks = ""   # mp3s in dir as output by ls
cwd = os.fsencode(os.getcwd())

#def FN_
#check empty file
#add line if not empty

def FN_randSelFromList(inList):
  listUB = len(inList) - 1
  itemNdx = random.randint(0,listUB)
  out = inList[itemNdx]
  return out

def FN_isItemInList(inList,inItem):
  found = 0
  for item in inList:
    if inItem in item:
      found = 1
  return found
  
def trackToUse(tracks):
  path = os.fsencode(os.getcwd() + "/lastPlayed")
  if not os.path.exists(path):
    with open("lastPlayed","w") as file:
      file.writelines(["1\n","2"])
      file.close()
  with open("lastPlayed","r") as file:
    lastPlayed = file.readlines()
    goodTrack = 0
    while goodTrack == 0:
      track = FN_randSelFromList(tracks)
      goodTrack = 1 - FN_isItemInList(lastPlayed,track)
    file.close()
  return track

def addToLastPlayed(track):
  maxLines = math.ceil(cntTracks * 0.8) 
  with open("lastPlayed","r") as file:
    lines = file.readlines()
    delLines = len(lines) - maxLines
    for i in range(delLines):
      lines.pop(0)
    lines.append(track + "\n")
    file.close()
  with open("lastPlayed","w") as file:
    file.writelines(lines)
  file.close()

def findMediaFiles(path=cwd, fileType="mp3",fileNameContains=""):
  out = []
  for file in os.listdir(path):
    fileName = os.fsdecode(file)
    if fileName.endswith(fileType):
      outFileName = str(fileName).replace("\n","")
      out.append(outFileName)
  return out

tracks = findMediaFiles()
cntTracks = len(tracks)

myTrack = trackToUse(tracks)
addToLastPlayed(myTrack)

tmp = "mpv -ss 61 " + myTrack
subprocess.run([tmp],shell=True)


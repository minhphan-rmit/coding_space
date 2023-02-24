# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022B
# Assignment: 4 - Final test
# Author: Kim Minsung (s3866724)
# Created date: 17/09/2022
# Last modified date: 17/09/2022
def count():
  with open("emma.txt", "r") as f:
    l = 0
    w = 0

    for line in f:
      line = line.strip("\n")
      words = line.split()
      l += 1
      w += len(words)
    return l,w

l,w = count()

print("number of lines: " + str(l) + " and " + "number of words: " + str(w))

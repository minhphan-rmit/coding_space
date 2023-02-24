# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022B
# Assignment: 4 - Final test
# Author: Kim Minsung (s3866724)
# Created date: 17/09/2022
# Last modified date: 17/09/2022

jp = open('eng2jp.txt', 'r')
j = jp.readlines()
japanese = {}
for l in j:
    l = l.replace('\n', '').split('\t')
    english = l[0].strip().lower()
    japanese_word = l[-1].strip().lower()
    japanese[english] = japanese_word

# Input from the user:
s = input('Enter a string: ')
r = s.split(' ')

result = ''
for i in r:
    i = i.lower()
    if i in japanese:
        result = result + japanese[i] + ' '
    else:
        result = result + i + ' '
print("Output:", result)
jp.close()

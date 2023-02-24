# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022B
# Assignment: 4 - Final test
# Author: Kim Minsung (s3866724)
# Created date: 17/09/2022
# Last modified date: 17/09/2022


def prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

l = [2, 3, 4, 5, 2, 6, 3, 2, 5, 7]
nl = []

for i in range(len(l)):
    if prime_num(l[i]) == True:
        nl.append(l[i])

nl = set(nl)
print(list(nl))

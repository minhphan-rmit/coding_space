# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: Individual - Timed Programming Lab Test 2 (25%)
# Author: Phan Nhat Minh (s3978598)
# Created date: 17/12/2022
# Last modified date: 17/12/2022
# IDE: Pycharm 2022.2.3 (Professional Edition)
# Python version: 3.11
# Question: 4

def factorial(n):
    """
    This function calculate the factorial of an integer number
    :param n: an integer input from user
    :return: the factorial of the integer n
    """

    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact


def rep_board(n, k):
    if k == 0:
        return 0
    else:
        return (factorial(n)/(factorial(k)*factorial(n-k))) + rep_board(n, k-1)


def print_result(stu, way):
    print(f"There are {way} way(s) to select representative board from {stu} students.")


# main program
stud = input("Enter the number of students: ")
ways = rep_board(stud, stud)
print_result(stud, ways)

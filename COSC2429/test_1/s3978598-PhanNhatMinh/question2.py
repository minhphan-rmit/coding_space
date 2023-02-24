# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: Individual - Timed Programming Lab Test 1 (25%)
# Author: Phan Nhat Minh (s3978598)
# Created date: 19/11/2022
# Last modified date: 19/11/2022
# IDE: Pycharm 2022.2.3 (Professional Edition)
# Python version: 3.11
# Question: 2


# function to find the factorial of a positive integer number
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


# main program
a = int(input("Enter an integer number: "))
# check the property of the input number
if a < 0:   # if a < 0 there is not factorial
    print("Factorial does not exist for negative number")
elif a == 0:    # if a = 0 then factorial = 1
    print(" The factorial of 0 is 1")
else:   # if a > 0 then call the function to calculate the factorial of a
    print("The factorial of ", str(a), " is ", str(factorial(a)))

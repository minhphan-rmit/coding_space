# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: Individual - Timed Programming Lab Test 1 (25%)
# Author: Phan Nhat Minh (s3978598)
# Created date: 19/11/2022
# Last modified date: 19/11/2022
# IDE: Pycharm 2022.2.3 (Professional Edition)
# Python version: 3.11
# Question: 4

def reverse_num(num):
    """
    This function is for creating a reverse number from the given number
    :param num: a number input from user
    :return: the reversed number
    """
    if int(num) < 0:
        rev_num = "-"+(num[-1:0:-1])
    else:
        rev_num = (num[::-1])
    return rev_num


# main program
a = input("Enter an integer number: ")
print("The reversed number is " + str(reverse_num(a)))

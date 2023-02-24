# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: Individual - Timed Programming Lab Test 1 (25%)
# Author: Phan Nhat Minh (s3978598)
# Created date: 19/11/2022
# Last modified date: 19/11/2022
# IDE: Pycharm 2022.2.3 (Professional Edition)
# Python version: 3.11
# Question: 1


# function to track the faulty items
def faulty_items_track(n):
    """
    This function track the 7th item that is a faulty item after 6 non-faulty items
    :param n: an integer from user input
    :return: print the number if it is divisible by 7
    """
    for i in range(n, 4*n):
        if i % 7 == 0:
            print(i)


# main program
a = int(input("Enter an integer number: "))
faulty_items_track(a)   # call the function

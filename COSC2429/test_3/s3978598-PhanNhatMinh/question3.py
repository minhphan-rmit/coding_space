# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: Assignment 4 - Test 3
# Author: Phan Nhat Minh (s3978598)
# Created date: 14/01/2023
# Last modified date: 14/01/2023
# IDE: Pycharm 2022.2.3 (Professional Edition)
# Python version: 3.11
# Question: 3


# functions
def investment_cal(data_file_name):
    """
    This function calculates the total investment amount from a data file
    :param data_file_name: file name that has .txt
    :return: the total investment amount in float
    """
    # empty list to store each line calculations
    total_invest = []

    # open and read the data file
    data = open(data_file_name, 'r')

    # loop through every line in the data file
    for line in data:
        # split the data into a list called line_data
        line_data = line.split(',')
        # take the numbers and multiply it and store it to a variable called line_invest
        line_invest = float(line_data[1]) * float(line_data[2])
        # append the multiplication above into the total_invest list
        total_invest.append(line_invest)

    # sum all the values in the total list
    result = sum(total_invest)
    # return the result
    return result


# main program
# ask the user to input the file name
f_name = input()
# call the function and assign it to a variable
total = investment_cal(f_name)
# print out the result with the correct format
print(f"The total investment amount is: {total}")

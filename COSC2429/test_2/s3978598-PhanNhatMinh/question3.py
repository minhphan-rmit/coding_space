# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: Individual - Timed Programming Lab Test 2 (25%)
# Author: Phan Nhat Minh (s3978598)
# Created date: 17/12/2022
# Last modified date: 17/12/2022
# IDE: Pycharm 2022.2.3 (Professional Edition)
# Python version: 3.11
# Question: 3


# function
def max_num(nums):
    """
    This function find the maximum number in a list of numbers and the index of that number in the list
    :param nums: given list of numbers by the user
    :return: the maximum value, and it's index
    """
    # turn the number sequence into list
    num_list = nums.split(' ')

    # covert the number in the sequence from string to float
    float_list = []
    for num in num_list:
        float_list.append(float(num))

    # find the max value in the list
    max_val = max(float_list)

    # find the indexes of that max number and store it in a list
    idx = []                                # create an empty list
    for i in range(len(float_list)):        # loop through indexes of the list of numbers
        if float_list[i] == max_val:        # if the number at that index = the max value
            idx.append(str(i))              # add that index to the list

    return max_val, idx                     # return 2 values: max number and the indexes of that number


def print_result(max_val, idx):
    """
    This is a non-fruitful function to print the result in the correct format
    :param max_val: max number
    :param idx: the indexes of that number
    :return: the correct format of message
    """
    print(f"The maximum number is {max_val} at position(s) {', '.join(idx)}")


# main program
numbers = input('Enter a sequence of numbers: ')    # get input from user
max_number, pos = max_num(numbers)                  # call the function and assign 2 values to 2 variables
print_result(max_number, pos)                       # call the print function to print the result

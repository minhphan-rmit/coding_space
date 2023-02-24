# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: Individual - Timed Programming Lab Test 2 (25%)
# Author: Phan Nhat Minh (s3978598)
# Created date: 17/12/2022
# Last modified date: 17/12/2022
# IDE: Pycharm 2022.2.3 (Professional Edition)
# Python version: 3.11
# Question: 1


# functions
def char_count(text: str):
    """
    This function counts occurrences of each letter in a string
    :param text: input string from user
    :return: the dictionary shows how many times the character occur
    """
    # correct the string format
    text = text.strip().lower()

    # create a dictionary to count the occurrences of letters, digits and symbols
    count = {
        'Letters': 0,
        'Digits': 0,
        'Symbols': 0,
    }

    # loop through characters in the string
    for char in text:
        if char.isalpha():              # if the character is letter add 1 to letters value in the dict
            count['Letters'] += 1
        elif char.isnumeric():          # if the character is number add 1 to digits value in the dict
            count['Digits'] += 1
        else:                           # if the character is not letter either number then add 1 to symbols
            count['Symbols'] += 1

    return count


def print_result(result):
    """
    This is a non-fruitful function to print out the result in the correct format
    :param result: a dictionary that counts occurrences of characters
    :return: the printed out result in the correct format
    """
    # loop through keys and print out keys with values
    for keys in result:
        print(str(keys) + ': ' + str(result[keys]))


# main program
str1 = input('Enter a string: ')        # ask user for the string
result1 = char_count(str1)              # generate the counting dictionary
print_result(result1)                   # call the function to print the result

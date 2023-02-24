# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: Assignment 4 - Test 3
# Author: Phan Nhat Minh (s3978598)
# Created date: 14/01/2023
# Last modified date: 14/01/2023
# IDE: Pycharm 2022.2.3 (Professional Edition)
# Python version: 3.11
# Question: 1


# functions
def remove_digits(text):
    """
    It loops through the string, adding letters to the no_digits list

    :param text: the string to remove digits from
    :return: A string with no digits.
    """
    no_digits = []
    # loop through the string, adding letters to the no_digits list
    for i in text:
        if not i[0].isdigit():
            no_digits.append(i)

    # return the joined string
    return ''.join(no_digits)


def reversed_text(text):
    """
    It reverses the order of a string

    :param text: a string
    :return: a reversed string
    """
    rev_text = text.split()        # convert the text in to a list of words
    rev_text.reverse()             # reverse the order of words in the list

    return ' '.join(rev_text)      # return a reversed string


# main program
# ask input string from user
mes = input('Enter a string with words and numbers: ')
# call the function to remove digits
no_dig_mes = remove_digits(mes)
# call the function and print out the reversed string
print(reversed_text(no_dig_mes))

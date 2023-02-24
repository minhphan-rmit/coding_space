# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: Individual - Timed Programming Lab Test 2 (25%)
# Author: Phan Nhat Minh (s3978598)
# Created date: 17/12/2022
# Last modified date: 17/12/2022
# IDE: Pycharm 2022.2.3 (Professional Edition)
# Python version: 3.11
# Question: 2


# function
def list_converter(text):
    """
    This function convert a string of words seperated by a comma into a list
    :param text: string of words given by user
    :return: the list of words in the string
    """
    return text.strip().split(',')


def vowel_filter(text):
    """
    This function filter words that does not start with a vowel
    :param text: a list of words seperated by a comma
    :return: filtered words
    """
    # convert the string of words into a list
    words_list = list_converter(text)

    # list of vowels
    vowels = ['u', 'e', 'o', 'a', 'i']

    # loop through the word in words list
    for word in words_list:
        low_word = str(word).lower()    # lower case the word
        if low_word[0] in vowels:       # if the word start with vowels then remove it from the list
            words_list.remove(word)
    return words_list                   # return the list of words that does not start with vowels


def print_result(words_list):
    """
    This is a non-fruitful function to print the result in the correct format
    :param words_list: the list of words that
    :return: the correct format of the result
    """
    # loop through words in the list and print that word out on a new line
    for word in words_list:
        print(word)


# main program
w_list = input('Enter the words seperated by comma: ')      # ask the user to input the words
print(list_converter(w_list))                               # print the list of words first
result = vowel_filter(w_list)                               # assign result to the vowel filter function
print_result(result)                                        # print out the result



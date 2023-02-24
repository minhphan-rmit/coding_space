# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: Assignment 4 - Test 3
# Author: Phan Nhat Minh (s3978598)
# Created date: 14/01/2023
# Last modified date: 14/01/2023
# IDE: Pycharm 2022.2.3 (Professional Edition)
# Python version: 3.11
# Question: 2

# import section
import test3_q2_2022C_dic as student


# functions
def remove_del_items(info: dict):
    """
    It loops through the original dictionary and adds the key-value pairs to a new dictionary if the
    value is not 'DELETED'
    
    :param info: dict
    :type info: dict
    :return: A dictionary with the key and value pairs that do not have the value 'DELETED'
    """
    # create an empty dict
    new_info = {}
    # loop through the original dictionary
    for keys, val in info.items():
        # if the value is not DELETED then add it to the new dictionary
        if val != 'DELETED':
            new_info[str(keys)] = val

    # return the new dictionary
    return new_info


def write_output(info):
    """
    It creates a new file called output.txt, loops through the dictionary, and writes the key and value
    pairs in the correct format
    
    :param info: a dictionary containing the information to be written to the file
    """
    # create and write on a new file
    # create a new file called output.txt
    out_file = open('output.txt', 'x')
    out_file = open('output.txt', 'w')      # write on a file called output.txt

    # loop through pair of keys and values in the dictionary
    for keys, val in info.items():
        # write the result in the correct format
        out_file.write(f"{keys}: {val}")
        out_file.write('\n')

    # close the file
    out_file.close()


# main program
# remove the deleted labelled items
del_info = remove_del_items(student)
# call the function to write the output file
write_output(del_info)

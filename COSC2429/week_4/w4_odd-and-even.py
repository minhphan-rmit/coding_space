"""
Write a function called is_even(n) that takes an integer as a parameter
and returns True if the parameter is an even number and False if it is odd.
This function is stored in the file even.py.

Write the function is_odd(n) that returns True when n is odd and False
otherwise. This function is stored in the file odd.py.

Modify is_odd so that it calls the function is_even
to determine if its parameter is an odd integer
"""


# function call from even.py
from odd import *


# main program
a = int(input())
print(is_odd(a))

"""
Write a function that takes a year as a parameter and determines
if it is a leap year. The function returns True if
the year is a leap year and False otherwise. A year is a leap year when:

It is divisible by 4 except when it is also divisible by 100

Except if the year is divisible also by 400 (it is a leap year then)
"""


# function to check leap year
def leap_check(y):
    """

    :param y: year
    :return: leap or not?
    """
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return True
    else:
        return False


# main program
year = int(input())
if leap_check(year):
    print("Is leap")
else:
    print("Is not leap")

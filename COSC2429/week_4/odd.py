# even.py call
from even import *


def is_odd(n):
    """

    :param n: an integer
    :return: odd or not?
    """
    odd_check = is_even(n)
    if odd_check is False:
        odd = True
    else:
        odd = False
    return odd

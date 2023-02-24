import math


def prime_check(n: int):
    """
    This function checks if the number is a prime or not
    :param n: an integer
    :return: True if the number is a prime and False if the number is not a prime
    """
    # if n is less or equal than 1 then it is not a prime
    if n <= 1:
        return False
    else:
        # check from 2 to square root of n to save memory
        for i in range(2, 1 + math.floor(math.sqrt(n))):
            # if found a number that divisible by n then it is not a prime
            if n % i == 0:
                return False
        # otherwise it is a prime
        return True

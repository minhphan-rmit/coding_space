# RMIT University Vietnam
# Author: Nhat Minh Phan
# Date created: 22/11/2022
# IDE: Pycharm 2022.2.3 (Professional Edition)
# Python version: 3.11


# function to returns the highest integer in the collatz sequence
def max_collatz(n):
    """
    This function returns the highest integer in the collatz sequence
    :param n: an integer
    :return: highest integer in the sequence
    """
    col = [n]   # set a list with the given integer
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            col.append(n)
        else:
            n = n * 3 + 1
            col.append(n)
    return int(max(col))


# main program
a = int(input("Input an integer: "))
# exception handle
while a < 0:
    a = int(input("Input a positive number: "))
# print out the result
print("The highest integer created by the Collatz Sequence of number ", a, " is ", max_collatz(a))

# RMIT University Vietnam
# Author: Nhat Minh Phan
# Date created: 22/11/2022
# IDE: Pycharm 2022.2.3 (Professional Edition)
# Python version: 3.11


# function
def pentagon_num(n):
    """
    This recursive function calculates the Nth pentagon number
    :param n: an integer
    :return: return the pentagon number of Nth
    """
    if n == 1:
        return 1
    else:
        return 5*(n-1) + pentagon_num(n-1)


# main program
a = int(input("Enter an integer: "))
while a < 0:
    a = int(input("Enter a positive integer: "))
print(pentagon_num(a))

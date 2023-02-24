"""
Apply divide-and-conquer strategy to write a program that asks
the user for a positive integer n and then print out a number pattern
base on n. For example, when n is 5, the pattern looks like this.

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

Hint: print(i, " ", end="") leaves one whitespace after printing
i and makes the cursor stay in the same line instead of going to a new line.
"""


# def recursive(n):
#     """
#     This function will print numbers by pattern.
#     :param n: input integer
#     :return: all the integers from the list which from the desginated pattern
#     """
#     num = [i + 1 for i in range(n)]
#     if n == 1:
#         return 1
#     print(" ".join(map(str, num)))
#     return recursive(n - 1)
#
# print(recursive(5))
# def number_pattern(n):
#     """
#     This is a non-fruitful function to print out pattern
#     :param n: a number (int)
#     :return: None
#     """
#     # for j in range(n):
#     while n > 0:
#         for i in range(1, n+1):
#             print(i, end=' ')
#         print()
#         n -= 1
#
# number_pattern(5)
def number_pattern(n):
    """
    This is a non-fruitful function to print out pattern 1 line
    :param n: a number (int)
    :return: None
    """
    for i in range(1, n + 1):
        print(i, end=' ')
def mul_line_pattern(n):
    """
    This is a non-fruitful function to print out pattern multiple lines
    :param n: a number (int)
    :return: None
    """
    for j in range(n, 0, -1):
        number_pattern(j)
        print()
mul_line_pattern(5)


# function to create the pattern
#def num_pat(n):
#    """
#    This function is for creating a number pattern
#    Input: an integer from user
#    Output: Create a tower-shape pattern base on the number given
#    """
#    for i in reversed(range(1, n+1)):
#        for j in range(1, i+1):
#            print(j, " ", end="")
#        print("")


# main program
#a = int(input("Input integer: "))
#print(num_pat(a))


# function to calculate the arithmetic sequence of an integer
def arithmetic(n):
    """
    This function calculates the total
    of an arithmetic sequence of an integer
    """
    if n == 1:
        return 1
    else:
        return n + arithmetic(n-1)


# function to print out the triangular numbers
def triangular_num(n):
    """
    This is a non-fruitful function to print out the
    triangular numbers from the given integer.
    """
    for i in range(1, n+1):
        print(i, " ", arithmetic(i))


# main program
a = int(input("Enter an integer: "))    # get input from user
# if the input number is less than 0 then request user for another input
while a < 0:
    a = int(input("Enter a positive integer: "))
# call the function
triangular_num(a)

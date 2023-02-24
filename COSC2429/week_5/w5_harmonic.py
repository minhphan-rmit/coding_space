# function to calculate the value of the harmonic from the given parameter
def harmonic(n):
    """
    This function calculates the harmonic of an integer number
    :param n: an integer
    :return: value of the harmonic series
    """
    if n == 1:
        return 1
    else:
        return 1/n + harmonic(n-1)


# main program
a = int(input())
while a < 0:
    a = int(input("Please re-enter a positive number: "))

print('{0:.3f}'.format(harmonic(a)))

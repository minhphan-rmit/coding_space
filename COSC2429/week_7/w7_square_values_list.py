def square_values(n):
    """

    :param n:
    :return:
    """
    sqr_list = [i**2 for i in list(range(1, n+1))]
    return sqr_list[-5:]


# main program
a = int(input('Input a integer: '))
print(square_values(a))



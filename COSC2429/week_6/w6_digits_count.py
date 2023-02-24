def digits_count(num):
    """
    This function counts the number of digits of a integer
    :param num: input number from user
    :return: number of digits
    """
    return len(str(num))


# main program
a = int(input())
print(digits_count(a))

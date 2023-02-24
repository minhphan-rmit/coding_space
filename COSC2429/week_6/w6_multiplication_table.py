def multi_table(n):
    """
    This non-fruitful function create a multiplication table using f-string and print function
    :param n: a given integer
    :return: a multiplication table from n
    """
    print(f"{'x' : >5}", end="")                    # print the 'x' symbol first
    for i in range(n+1):                            # this loop for printing the numbers for the first line
        print(f"{str(i) : >5}", end="")
    print()
    for j in range(n+1):                            # loop for creating n rows
        print(f"{str(j) : >5}", end="")
        for k in range(n+1):                        # loop for calculating values of n-th position in the row
            print(f"{str(j * k) : >5}", end="")
        print()
    return ''


print(multi_table(12))

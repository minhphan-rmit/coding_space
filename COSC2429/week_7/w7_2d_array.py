def two_dimensions_array(x, y):
    """
    This function creates a 2D array of x and y given by the user
    :param x: x rows
    :param y: y columns
    :return: 2D array from x and y which i-th row and j-th column is i*j
    i = 0, 1,..., x-1
    j = 0, 1,..., y-1
    """
    two_d_array = []                            # create an empty string to store the result
    for i in range(x):                          # loop for creating rows
        row = []                                # each row created, a new empty sub-list is created also
        for j in range(y):                      # loop for creating columns
            row.append(i*j)                     # append the values to the sub-list
        two_d_array.append(row)                 # append the sub-list to the main list
    result = '\n'.join(map(str, two_d_array))   # add new lines to the result for correct output format
    return result


# main program
a = int(input('Input a: '))             # get input from user
b = int(input('Input b: '))
print(two_dimensions_array(a, b))     # print the output

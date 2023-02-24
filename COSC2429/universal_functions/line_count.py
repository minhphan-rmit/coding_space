def line_count(text_file):
    """
    This function counts the line of a text file
    :param text_file: a text file with .txt extension
    :return: the number of lines
    """
    # open and read the text file
    text = open(text_file, 'r')

    # set count to 0
    count = 0

    # loop through lines in the source file
    for line in text:
        print('minh' + line)
        # increment count by 1 each time loop through a line
        count += 1

    # return the number of lines
    return count


print(line_count('test.txt'))

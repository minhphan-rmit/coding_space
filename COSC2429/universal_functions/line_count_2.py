def line_count(text_file):
    """
    This function counts the line of a text file
    :param text_file: a text file with .txt extension
    :return: the number of lines
    """
    # open and read the text file
    text = open(text_file, 'r')

    word_count = 0
    for line in text:
        for word in line.split():
            word_count += 1

    l_count = len(text.readlines())

    return word_count, l_count


print(line_count('test.txt'))

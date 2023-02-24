def word_count(text_file):
    """
    This function count words in a text file
    :param text_file: a text file with .txt extension
    :return: the number of words
    """
    # open and read the text file
    text = open(text_file, 'r')

    # set count to 0
    count = 0

    # loop through lines in the source file
    for line in text:
        print('im here' + line)
        # remove punctuations
        line = line.replace('_', ' ').replace('"', ' ').replace(',', ' ').replace('.', ' ')
        line = line.replace('?', ' ').replace('!', ' ').replace("'", " ").replace('--', ' ')
        line = line.replace('(', ' ').replace(')', ' ').replace(':', ' ').replace('[', ' ')
        line = line.replace(']', ' ').replace(';', ' ')
        line = line.replace("'s", " ")

        # loop through words in the line
        for word in line.split():
            count += 1

    # return the number of words
    return count


print(word_count('test.txt'))

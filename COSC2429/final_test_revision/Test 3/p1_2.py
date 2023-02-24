def count_word_line(text_file):
    """

    :param text_file:
    :return:
    """
    count = 0
    with open(text_file, 'r') as text:
        n_lines = 0
        n_words = 0

        for line in text:
            line = line.strip('\n')
            words = line.split()
            n_lines += 1
            n_words += len(words)
        return n_lines, n_words


l, w = count_word_line('emma.txt')
print(l, w)

def count_line(text_file):
    """

    :param text_file:
    :return:
    """
    with open(text_file, 'r') as text:
        num_lines = len(text.readlines())

    return num_lines


def count_word(text_file):
    """

    :param text_file:
    :return:
    """
    count = 0
    with open(text_file, 'r') as text:
        for line in text:
            for word in line.split():
                count += 1
        return count


n_words = count_word('emma.txt')
n_lines = count_line('emma.txt')
print(f"Words: {n_words} Lines: {n_lines}")
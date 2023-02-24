def str_sort(words: str):
    """
    This function reorder the given words in a string alphabetically
    :param words: input string from user
    :return: the sorted string
    """
    words_list = words.strip().split(',')
    return ','.join(sorted(words_list))


# main program
word = input('Input a list of words: ')
print(str_sort(word))

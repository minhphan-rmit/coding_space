def remove_letter(str1, letter):
    """
    This function removes all occurrences of a letter in a given string.
    :param str1: input string from user
    :param letter: input letter that user want to delete from the string
    :return: a new string that deleted the given letter
    """
    str1 = str1.strip().lower()
    letter = letter.strip().lower()
    if str1.find(letter) == 0:
        return str1
    else:
        new_string = str1.replace(letter, "")
        return new_string


# main program
input_string = input("Input a string: ")
input_letter = input("A letter you want to delete: ")
print(remove_letter(input_string, input_letter))

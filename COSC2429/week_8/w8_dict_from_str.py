def dict_from_str(text: str) -> dict:
    """
    This function counts occurrences of each letter in a string
    :param text: input string from user
    :return: the dictionary which keys are the letters and values are the occurrences of that letter
    """
    text = text.strip().lower()         # trim and lower the string
    char_dict = {}                      # create an empty dictionary for storing result
    for char in text:                   # loop through characters in the string
        if char in char_dict:           # if the character already in the dict
            char_dict[char] += 1        # add 1 to the value
        else:                           # if the character is not in the dict
            char_dict[char] = 1         # create a new key for that character

    return char_dict


# main program
str1 = input("Input string: ")          # ask the user to input a string
print(dict_from_str(str1))              # print out the result

def palindrome_str(str1):
    """
    This function checks if the string is palindrome or not
    :param str1: a given string from user
    :return: True if is the is palindrome and false if the string is not palindrome
    """
    str1 = str1.strip().lower()
    if str1[::1] == str1[::-1]:
        return True
    return False


# main program
str_t = input("Input a string: ")
if palindrome_str(str_t):
    print("Your string is palindrome")
else:
    print("Your string is not palindrome")

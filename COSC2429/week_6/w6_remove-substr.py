def remove_substr(main_str, sub_str):
    """

    :param main_str:
    :param sub_str:
    :return:
    """
    if main_str.find(sub_str) > 0:
        new_str = main_str.replace(sub_str, "")
        return new_str
    else:
        return main_str


# main program
print(remove_substr("hello", "el"))
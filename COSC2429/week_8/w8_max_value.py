def max_value(dict1: dict):
    """
    This function
    :param dict1:
    :return:
    """
    max_val = max(dict1.items())
    max_val = max_val[1]

    max_keys = []
    for keys in dict1:
        if dict1[keys] == max_val:
            max_keys.append(keys)

    if len(max_keys) == 1:
        result = f"The maximum value in dictionary is {max_val} of the key {max_keys[0]}"
    else:
        result = f"The maximum value in dictionary is {max_val} of the key {', '.join(max_keys)}"
    return result


d = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
print(max_value(d))
def dict_filter(in_dict: dict, thr_val: float) -> dict:
    """
    This function filters items in a dictionary according to a given threshold value
    :param in_dict: the original dictionary
    :param thr_val: the threshold (float)
    :return: the filtered dictionary
    """
    # create an empty dictionary for storing result
    new_dict = dict()

    # loop through keys in the original dict
    for keys in in_dict:
        if in_dict[keys] > thr_val:             # if the value of that key is larger than the threshold
            new_dict[keys] = in_dict[keys]      # add that pair of key and value to the new dictionary

    return new_dict


s_dict = {
    'Cierra Vega': 175,
    'Alden Cantrell': 180,
    'Kierra Gentry': 165,
    'Pierre Cox': 190
}
limit = 170
print(dict_filter(s_dict, limit))

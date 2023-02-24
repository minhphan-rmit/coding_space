def complete_message(text: str):
    print(text + ' was created successfully.')


def copy_file(file_name: str):
    """
    This function c
    :param file_name:
    :return:
    """
    # open and read the source file
    f = open(file_name, 'r')
    # set default values
    i = 0
    new_content = ''
    for line in f:  # loop through lines
        i += 1
        new_content += str(i) + line + '\n'

    new_file_name = 'new_' + file_name
    new_f = open(new_file_name, 'w')
    new_f.write(new_content)

    new_f.close()
    f.close()

    complete_message(new_file_name)

    return ''


# input
f_name = input('File name: ')
copy_file(f_name)

def eng_to_pirate(message: str):
    """
    This function translates a normal English message into pirate language
    :param message: input message from user
    :return: the translated message into pirate language
    """
    # open eng2pirate.txt file to create the pirate dictionary
    pirate = open('eng2pirate.txt', 'r')
    content = pirate.read()
    pirate.close()
    content = content.split()

    # create the pirate dictionary
    pirate_dict = dict()                        # create an empty dict
    for i in range(0, len(content), 2):         # for every pair of items (i-th and (i+1)-th)) is a pair key and value
        pirate_dict[content[i]] = content[i+1]

    # translation
    result = ''                                 # create an empty string for result
    message = message.strip().split()           # turn the message into list of words
    for word in message:                        # this loop goes through every word in the list
        if word.isalpha():
            # if the word = the key in the list then add the value of that key to result
            if word in pirate_dict:
                result += pirate_dict[word] + ' '
            else:
                result += word + ' '
        else:
            result += word + ' '

    # return the final result
    return result


# main program
mess = input("Message in English: ")
print(f"Your message in pirate language is {eng_to_pirate(mess)}")

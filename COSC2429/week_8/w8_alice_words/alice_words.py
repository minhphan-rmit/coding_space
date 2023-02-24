def word_count(text_file: str, destination_file: str, new_file: str):
    """
    This function counts the occurrences of every word in a text file
    :param text_file: a source file that has .txt extension
    :param destination_file: a destination file that stores the result
    :param new_file: create a new file if the answer is 'y'
    :return: result written in destination file from user
    """
    # open and read the source file
    text = open(text_file, 'r')

    # create an empty dictionary for storing result
    count = {}

    # loop through lines in the source file
    for line in text:
        # remove punctuations
        line = line.replace('_', ' ').replace('"', ' ').replace(',', ' ').replace('.', ' ')
        line = line.replace('?', ' ').replace('!', ' ').replace("'", " ").replace('--', ' ')
        line = line.replace('(', ' ').replace(')', ' ').replace(':', ' ').replace('[', ' ')
        line = line.replace(']', ' ').replace(';', ' ')
        line = line.replace("'s", " ")

        # loop through words in the line
        for word in line.split():

            # ignore case
            word = word.lower()

            # ignore numbers and words start with '-'
            if word[0].isalpha():
                if word in count:   # if word already appeared in count then increment the value by 1
                    count[word] = count[word] + 1
                else:               # if count does not have word then create a new key and value is 1
                    count[word] = 1

    # sort the keys in count alphabetically
    keys = count.keys()
    keys = sorted(keys)

    # find the longest word
    word_length = 0
    longest_word = ''
    for word in keys:
        if len(word) >= word_length:
            word_length = len(word)
            longest_word = word
        else:
            word_length = word_length
            longest_word = longest_word

    if new_file == 'n':
        # open the destination file for writing output
        output = open(destination_file, "w")
    else:
        output = open(destination_file, "x")

    # extended questions:
    output.write(f"The word Alice occur {count['alice']} times in the book.")
    output.write("\n")
    output.write(f"The longest word in the book is {longest_word}")
    output.write("\n")
    output.write(f"The longest word has {word_length} characters")
    output.write("\n")

    # creating header
    output.write(f"{'Word' : <20}")
    output.write(f"{'Count' : ^15}")
    output.write('\n')

    # write the result to the destination file
    for word in keys:  # use the sorted keys and take the value from count
        output.write(f"{word : <20}")
        output.write(f"{str(count[word]) : ^15}")
        output.write('\n')

    # close all the files
    output.close()
    text.close()

    return ''   # so that output won't print out None


# main program
input_file = input('Input file (only .txt file accepted): ')          # ask user the source file for counting words
while input_file[-4:] != '.txt':
    input_file = input('Please re-enter the correct file type: ')

n_file_ans = input('Do you want to create a new file [y/n]: ')
des_file = input('Destination file (only .txt file accepted): ')      # ask user the destination file for storing result
while des_file[-4:] != '.txt':
    des_file = input("Please re-enter the correct file type: ")

print(word_count(input_file, des_file, n_file_ans))                               # call the function

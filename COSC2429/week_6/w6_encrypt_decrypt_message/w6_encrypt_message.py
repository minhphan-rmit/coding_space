# global values
cipher_key = 'QTGABCDEFHIJKOMNLPRSUVZYXW'   # NOQA
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'     # NOQA


# function
def encrypt_message(message, enc_key):
    """
    This function encrypts a message from a custom key
    :param message: a given message from user
    :param enc_key: a custom encrypted key
    :return: encrypted message
    """
    message = message.upper()
    enc_str = ''
    for char in message:
        if char.isalpha():                  # if char is alphabet then encrypt it
            index = alphabet.find(char)
            enc_char = enc_key[index]
            enc_str += enc_char
        else:
            enc_str = enc_str + char        # if char is blank space or special character then add the original char
    return enc_str


# main program
mess = input("The original message: ")
print(encrypt_message(mess, cipher_key))

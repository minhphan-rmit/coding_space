# global values
cipher_key = 'QTGABCDEFHIJKOMNLPRSUVZYXW'   # NOQA
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'     # NOQA


# function
def decrypt_message(enc_mess, enc_key):
    """

    :param enc_mess:
    :param enc_key:
    :return:
    """
    enc_mess = enc_mess.upper()
    org_mess = ''
    for char in enc_mess:
        if char.isalpha():
            index = enc_key.find(char)
            og_char = alphabet[index]
            org_mess += og_char
        else:
            org_mess += char
    return org_mess


# main program
mess = input("The encrypted message: ")
print(decrypt_message(mess, cipher_key))

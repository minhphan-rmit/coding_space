import string


def encrypt_dict(enc_code): # NOQA
    enc_dict = {
        0: ' '
    }
    enc_alpha = enc_code
    i = 1
    for enc_keys in enc_alpha:
        enc_dict[i] = enc_keys
        i += 1
    return enc_dict


def decrypt_message(enc_str, enc_code):
    alphabet = ' ' + string.ascii_uppercase
    org_str = ''
    enc_alphabet = encrypt_dict(enc_code)
    for j in enc_str:
        for i in range(len(alphabet)):
            if enc_alphabet[i] == j:
                org_str += alphabet[i]
    return org_str

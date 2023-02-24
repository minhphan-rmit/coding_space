import string


def alphabet(): # NOQA
    # create dictionary for normal alphabet
    alpha = {
        0: ' '
    }
    alpha_str = string.ascii_uppercase
    k = 1
    for alpha_keys in alpha_str:
        alpha[k] = alpha_keys
        k += 1
    return alpha


def encrypt_message(org_str, enc_code):
    """
    This function create a substitution cipher for a given string
    """
    alpha = alphabet()
    enc_code = ' ' + enc_code
    enc_str = ''
    for j in org_str:
        for i in range(len(alpha)):
            if alpha[i] == j:
                enc_str += enc_code[i]
    return enc_str

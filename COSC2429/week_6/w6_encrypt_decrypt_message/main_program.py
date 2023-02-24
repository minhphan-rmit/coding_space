import decrypt
import encrypt


# main program
ans = input("Encrypt or decrypt (e/d): ").strip().lower()
while ans != 'e' and ans != 'd':
    ans = input("Please re-enter your answer: ").strip().lower()
if ans == 'e':
    str1 = input("The message: ").strip().upper()
    str2 = input("Encrypted alphabet: ").strip().upper()
    print("The encrypted message: ", encrypt.encrypt_message(str1, str2))
elif ans == 'd':
    str3 = input("The encrypted message: ").strip().upper()
    str4 = input("Encrypted alphabet: ").strip().upper()
    print("The decrypted message: ", decrypt.decrypt_message(str3, str4))


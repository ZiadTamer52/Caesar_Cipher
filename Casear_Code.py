'''
# Crypto With Python #
## Caeser cipher ##
'''

# INPUT
plaintext="hello"
alphabet ="abcdefghijklmnopqrstuvwxyz"

# PROCESS

def caeser_encrypt(plaintext, key):
    ciphertext = ""

    for state in plaintext:
        ciphertext += alphabet[(alphabet.index(state) + key) % 26 ]
    return ciphertext


def caser_decrypt(ciphertext, key):
    plaintext =""

    for state in ciphertext:
        plaintext += alphabet[(alphabet.index(state)- key) % 26 ]
    return plaintext

# HELPER FUNCTION
def char_to_int(char):
    return alphabet.index(char)

def int_to_char(int):
    return alphabet[int]

def bruteforce(ciphertext):
    for i in range(1,26):
        print(f"{i}: {caser_decrypt(ciphertext,i)}") 

# MAIN
key = 3
ciphertext=caeser_encrypt(plaintext, key)
plaintext= caser_decrypt(ciphertext, key)
print(f"*===* Caeser Cipher demo *===*")
print(f"=============Caser_encrypt ==")
print(f"Plaintext: {plaintext}\nciphertext: {ciphertext}")
print(f"=============Caser_decrypt ==")
print(f"ciphertext: {ciphertext}\nplaintext: {plaintext}")

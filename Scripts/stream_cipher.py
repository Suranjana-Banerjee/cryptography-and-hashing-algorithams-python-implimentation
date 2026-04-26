#Stream cipher
import random

def encrypt(msg, key):
    random.seed(key) 
    encryption= '' 
    for char in msg:
        encryption += chr(ord(char) ^ random.randint(0, 255))
    return encryption

def decrypt(encryption, key):
    random.seed(key)
    decryption= ''
    for char in encryption:
        decryption += chr(ord(char) ^ random.randint(0, 255))
    return decryption

msg = "Hello, World!"
key = "secretkey"

#Encryption
encrypted_msg = encrypt(msg, key) 
print("Encrypted Message:", encrypted_msg)
print("The original string is : " + str(msg))
keystream= random.randint(0, 255)
print("Keystream (generated random number between 0 to 255):", keystream)

#Decryption
decrypted_msg = decrypt(encrypted_msg, key)
print("Decrypted Message:", decrypted_msg)

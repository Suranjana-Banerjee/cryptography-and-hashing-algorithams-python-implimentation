import random
import string
char = string.punctuation + string.ascii_letters + string.digits + " "
char = list(char)
key = char.copy()
random.shuffle(key)

print(f"char: {char}")
print(f"key: {key}")

#Encryption
plain_text = input("Enter a message to encrypt:")
cipher_text = ""
for letter in plain_text:
    index = char.index(letter)
    cipher_text += key[index]
    
print(f" Original Message: {plain_text}")
print(f" Encrypted Message: {cipher_text}")

#Decryption
cipher_text = input("Enter a message to decrypt:")
plain_text = ""
for letter in cipher_text:
    index = key.index(letter)
    plain_text += char[index]

print(f" Encrypted Message: {cipher_text}")    
print(f" Original Message: {plain_text}")
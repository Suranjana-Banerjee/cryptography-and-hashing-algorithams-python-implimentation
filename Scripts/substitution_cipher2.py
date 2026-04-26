import random
import string
char = string.punctuation + string.ascii_letters + string.digits + " "
char = list(char)
key = char.copy()
random.shuffle(key)

#print(f"char: {char}")
#print(f"key: {key}")

#Encryption
def encryption(plain_text, shift_key):
    cipher_text = ""
    for letter in plain_text:
        index = char.index(letter)
        cipher_text += key[index]
        
    print(f" Original Message: {plain_text}")
    print(f" Encrypted Message: {cipher_text}")
    
#Decryption
def decryption(cipher_text, shift_key):
    plain_text = ""
    for letter in cipher_text:
        index = key.index(letter)
        plain_text += char[index]

    print(f" Encrypted Message: {cipher_text}")    
    print(f" Original Message: {plain_text}")
    
flag=False
while not flag:
    user_choice= (input('Type "e" for ENCRYPTION or "d" for DECRYPTION: ').lower())
    message= input(' Enter your Message: ')
    
    if user_choice == 'e':
        encryption(plain_text= message, shift_key= key)
    elif user_choice == 'd':
        decryption(cipher_text= message, shift_key= key)
        
    choice= (input('Type "yes" to continue or "no" to end: ').lower())
    if choice == 'no':
        flag=True
        print ('Have a Nice Day! Bye...!')
        
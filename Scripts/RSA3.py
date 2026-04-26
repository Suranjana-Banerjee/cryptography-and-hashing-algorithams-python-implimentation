from math import gcd
publickey = 0 
t = 0
#Encryption
def encryption(p, q, plaintext):
    global publickey, t
    ciphertext= ''
    n = p * q                   # calculating n
    t = (p - 1) * (q - 1)       # calculating totient, t
    for i in range (2, t):      # selecting public key, e
        if gcd(i, t) == 1:
            publickey = i
    # performing encryption
    ascii_value = [ord(char) for char in message]
    ciphertext = [pow(char, publickey, n) for char in ascii_value]     
    print(f"Encrypted message is {ciphertext}")
#Decryption   
def decryption(p, q, ciphertext):
    global publickey, t
    plaintext= ''
    n = p * q
    j = 0
    while True:
        if (j * publickey) % t == 1:
            privatekey = j
            break
        j += 1
        
    # performing decryption
    encoded_message = [pow(i, privatekey, n) for i in ciphertext]
    plaintext = ''.join(chr(i) for i in encoded_message)
    print(f"Decrypted message is {plaintext}")
    
#Select p, q (p and q both prime and p not equal to q)    
flag=False
while not flag:
    user_choice= (input('Type "e" for ENCRYPTION or "d" for DECRYPTION: ').lower())
    message= input('Type your Message:')

    if user_choice == 'e':
        encryption(p=3, q=7, plaintext= message)
    elif user_choice == 'd':
        decryption(p=3, q=7, ciphertext= message)
        
    choice= (input('Type "yes" to continue or "no" to end: ').lower())
    if choice == 'no':
        flag=True
        print ('Have a Nice Day! Bye...!')
    
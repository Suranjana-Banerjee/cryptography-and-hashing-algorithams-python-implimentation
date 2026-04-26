alphabate= ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plaintext, shift_key): # hello
    ciphertext=''
    for char in plaintext:
        if char in alphabate:
            position=alphabate.index(char) # position=7
            new_position=(position+shift_key)%26 # new_position= 7+3=10
            ciphertext +=alphabate[new_position] # ciphertext= k
        else:
            ciphertext += char
    print(f'The Encrypted message is:{ciphertext}')     
def decryption(ciphertext, shift_key): # khoor
    plaintext=''
    for char in ciphertext:
        if char in alphabate:
            position=alphabate.index(char)
            new_position=(position-shift_key)%26
            plaintext +=alphabate[new_position]
        else:
            plaintext += char
    print(f'The Decrypted message is:{plaintext}')

flag=False
while not flag:
    user_choice= input('Type "e" for ENCRYPTION or "d" for DECRYPTION: ')
    message= input('Type your Message:')
    key= int(input('Enter the shift key:'))
    
    if user_choice == 'e':
        encryption(plaintext= message, shift_key= key)
    elif user_choice == 'd':
        decryption(ciphertext= message, shift_key= key)
        
    choice= input('Type "yes" to continue or "no" to end: ')
    if choice == 'no':
        flag=True
        print ('Have a Nice Day! Bye...!')
        
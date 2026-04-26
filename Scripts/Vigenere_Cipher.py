alphabate= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

#Encryption
def encryption(plaintext, shift_key): 
    ciphertext=''
    temp=0
    for char in plaintext:
        if char in alphabate:
            position=alphabate.find(char) # index value of letters of plaintext
            if position!=-1:
                position= position+alphabate.find(shift_key[temp]) #index value of key added to plaintext
                new_position= position%len(alphabate) #cross checking the boundary
                ciphertext+= alphabate[new_position]
                temp+=1
                if temp==len(shift_key):
                    temp=0
        else:
            ciphertext+= char
    print(f'The Encrypted message is:{ciphertext}')   

#Decryption
def decryption(ciphertext, shift_key): 
    plaintext=''
    temp=0
    for char in ciphertext:
        if char in alphabate:
            position=alphabate.find(char) # index value of letters of plaintext
            if position!=-1:
                position= position-alphabate.find(shift_key[temp]) #index value of key added to plaintext
                new_position= position%len(alphabate) #cross checking the boundary
                plaintext+= alphabate[new_position]
                temp+=1
                if temp==len(shift_key):
                    temp=0
        else:
            plaintext+= char
    print(f'The Decrypted message is:{plaintext}')

flag=False
while not flag:
    user_choice= (input('Type "e" for ENCRYPTION or "d" for DECRYPTION: ').lower())
    message= input('Type your Message:')
    key= input('Enter the key:')
    
    if user_choice == 'e':
        encryption(plaintext= message, shift_key= key)
    elif user_choice == 'd':
        decryption(ciphertext= message, shift_key= key)
        
    choice= (input('Type "yes" to continue or "no" to end: ').lower())
    if choice == 'no':
        flag=True
        print ('Have a Nice Day! Bye...!')
        
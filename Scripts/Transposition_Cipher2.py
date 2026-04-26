import math

#Encryption
def encryption(plaintext, shift_key):
    t = 0
    for r in range(row):
      for c,ch in enumerate(message[t : t+ len_key]):
        matrix[r][c] = ch
      t += len_key

    # print(matrix)
    sort_order = sorted([(ch,i) for i,ch in enumerate(key)])  #to make alphabetically order of chars
    # print(sort_order)

    ciphertext = ''
    for ch,c in sort_order:
      for r in range(row):
        ciphertext += matrix[r][c]  
    print(f'The Encrypted message is:{ciphertext}')   

#Decryption
def decryption(ciphertext, shift_key):
    matrix_new = [ ['X']*len_key for i in range(row) ]
    key_order = [ key.index(ch) for ch in sorted(list(key))]  #to make original key order when we know keyword
    # print(key_order)

    t = 0
    for c in key_order:
      for r,ch in enumerate(message[t : t+ row]):
        matrix_new[r][c] = ch
      t += row
    # print(matrix_new) 

    plaintext = ''
    for r in range(row):
      for c in range(len_key):
        plaintext += matrix_new[r][c] if matrix_new[r][c] != 'X' else ''
    print(f'The Decrypted message is:{plaintext}')

flag=False
while not flag:
    user_choice= (input('Type "e" for ENCRYPTION or "d" for DECRYPTION: ').lower())
    message= input('Type your Message:')
    key= input('Enter the key:')
    
    len_key = len(key)
    len_plain = len(message)
    row = int(math.ceil(len_plain / len_key))
    matrix = [ ['X']*len_key for i in range(row) ]
    # print (matrix)
    
    if user_choice == 'e':
        encryption(plaintext= message, shift_key= key)
    elif user_choice == 'd':
        decryption(ciphertext= message, shift_key= key)
        
    choice= (input('Type "yes" to continue or "no" to end: ').lower())
    if choice == 'no':
        flag=True
        print ('Have a Nice Day! Bye...!')
        
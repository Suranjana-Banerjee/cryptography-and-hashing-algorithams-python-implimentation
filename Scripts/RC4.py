#key scheduling algorithm
def key_scheduling(key):
    schedule = [i for i in range(0, 256)]
    num = 0
    for i in range(0, 256):
        num = (num + schedule[i] + key[i % len(key)]) % 256
        temp = schedule[i]
        schedule[i] = schedule[num]
        schedule[num] = temp
    return schedule
    
#Pseudo-Random Generation Algorithm
def stream_generation(schedule):
    i = 0
    j = 0
    while True:
        i = (1 + i) % 256
        j = (schedule[i] + j) % 256
        temp = schedule[j]
        schedule[j] = schedule[i]
        schedule[i] = temp
        yield schedule[(schedule[i] + schedule[j]) % 256]        

#Encryption
def encryption(plaintext, key):
    plaintext = [ord(char) for char in plaintext]
    key = [ord(char) for char in key]
    schedule = key_scheduling(key)
    key_stream = stream_generation(schedule)
    ciphertext = ''
    for char in plaintext:
        encrypt = str(hex(char ^ next(key_stream))).upper()
        ciphertext += encrypt
    print(f'The Encrypted message is:{ciphertext}')
    
#Decryption
def decryption(ciphertext, key):
    ciphertext = ciphertext.split('0X')[1:]
    ciphertext = [int('0x' + c.lower(), 0) for c in ciphertext]
    key = [ord(char) for char in key]
    schedule = key_scheduling(key)
    key_stream = stream_generation(schedule)
    plaintext = ''
    for char in ciphertext:
        decrypt = str(chr(char ^ next(key_stream)))
        plaintext += decrypt
    print(f'The Decrypted message is:{plaintext}')


flag=False
while not flag:
    user_choice= (input('Type "e" for ENCRYPTION or "d" for DECRYPTION: ').lower())
    message= input('Type your Message:')
    key= input('Enter the key:')
    
    if user_choice == 'e':
        encryption(plaintext= message, key = key)
    elif user_choice == 'd':
        decryption(ciphertext= message, key = key)
        
    choice= (input('Type "yes" to continue or "no" to end: ').lower())
    if choice == 'no':
        flag=True
        print ('Have a Nice Day! Bye...!')
        
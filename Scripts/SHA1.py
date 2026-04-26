# importing the hashlib libraries
import hashlib

message = input('Type your Message:')
# encoding the message using the library function
output = hashlib.sha1(message.encode())
print(f"Hash of the input string: {output.hexdigest()}")

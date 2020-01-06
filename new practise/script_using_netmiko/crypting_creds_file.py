#!/usr/bin/env python
"""Encrypting and Decrypting contents of the file without using JSON"""

from simplecrypt import encrypt, decrypt
#import json
import csv
from getpass import getpass
from pprint import pprint

file = open('creds.csv','r')
cred = csv.reader(file)
cred_list = [credline for credline in cred]
password = getpass()

print("Un-encrypted credentials lists:\n")
pprint(cred_list)       #print unencrypted msg.
#cred_list_encrypt = encrypt(password,str(cred_list).encode('utf8'))   #'key first then message' this format is important else use library variable and assign value.encrypting
cred_list_encrypt = encrypt(password,str(cred_list))   #'key first then message' this format is important else use library variable and assign value.encrypting
#the data/payload to be encrypted must be in string format. Hence, we have converted above list in string and then contents gets encrypted.
print("\nEncrypted credentials data:\n")
pprint(cred_list_encrypt)
encrypted_cred = open('encrypted_cred','wb')
encrypted_cred.write(cred_list_encrypt)
#data must be in string type for normal write 'w' operation. We have used 'wb' to write data in 'bytes' type to the file.
encrypted_cred.close()

encrypted_cred_read = open('encrypted_cred','rb')
#data must be in string type for normal read 'r' operation. We have used 'rb' to read data in 'bytes' type in the file.
#decrypting the above encrypted data.
unencrypted_cred_list = decrypt(password,encrypted_cred_read.read())   #'key first then message' this format is important else use library variable and assign value.decrypting
print("\nDecrypted credentials list:\n")
pprint(unencrypted_cred_list)  #print decrypted string in bytes'b"'
encrypted_cred_read.close()

#!/usr/bin/env python
"""Encrypting and Decrypting contents of the file using JSON"""

from simplecrypt import encrypt, decrypt
import json
import csv
from getpass import getpass
from pprint import pprint

"""Importing the data from CSV file"""
file = open('creds.csv','r')
cred = csv.reader(file)
cred_list = [credline for credline in cred]
password = getpass()

print("Un-encrypted credentials lists:\n")
pprint(cred_list)       #print unencrypted msg.
print(type(cred_list))
#below json.dumps() command converts cred_list[] to string which is then encrypted using password as salt
cred_list_encrypt = encrypt(password,json.dumps(cred_list))
print("\nEncrypted credentials data:\n")
pprint(cred_list_encrypt)   #prints the encrypted data(byte-format)

"""Open a new file with "write,byte" permission"""
encrypted_cred = open('encrypted_cred','wb')
encrypted_cred.write(cred_list_encrypt)
encrypted_cred.close()

"""Open a encrypted data file with "read,byte" permission"""
encrypted_cred_read = open('encrypted_cred','rb')
#below json.loads() command converts encrypted_cred_read.read() bytes data to list which is then decrypted using password as salt
unencrypted_cred_list = json.loads(decrypt(password,encrypted_cred_read.read()))
encrypted_cred_read.close()

"""Verifying decrypted data"""
print("\nDecrypted credentials list:\n")
pprint(unencrypted_cred_list)
print(type(unencrypted_cred_list))

#For json.loads : parse the string/byte in JSON object // TypeError: the JSON object must be str, bytes or bytearray, not 'list'
#For json.dumps : parse the JSON object into string/byte.

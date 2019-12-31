from simplecrypt import encrypt, decrypt


plaintext1 = "Hello world unencrypted."     #msg to be encrypted.

print(plaintext1)       #print unencrypted msg.

key  = '123'        #salt or encryption key

ciphertext1 = encrypt(key,plaintext1.encode('utf8'))   #'key first then message' this format is important else use library variable and assign value.encrypting

print (ciphertext1)  #print encrypted string in bytes'b"'

unencrypted_cipher_demo = decrypt(key,ciphertext1)   #'key first then message' this format is important else use library variable and assign value.decrypting

print(unencrypted_cipher_demo)  #print decrypted string in bytes'b"'

print(unencrypted_cipher_demo.decode('utf8'))  #print decrypted string in bytes'b"'

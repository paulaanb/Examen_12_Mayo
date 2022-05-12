from cryptography.fernet import Fernet
key = Fernet.generate_key() 
  
with open('filekey.key', 'wb') as filekey: 
   filekey.write(key)

fernet = Fernet(key) 
  
with open('conversiones (4).csv', 'rb') as enc_file: 
    encrypted = enc_file.read() 
  
decrypted = fernet.decrypt(encrypted) 
  
with open('conversiones (4).csv', 'wb') as dec_file: 
    dec_file.write(decrypted) 

with open('navegacion (4).csv', 'rb') as enc_file: 
    encrypted = enc_file.read() 
  
decrypted = fernet.decrypt(encrypted) 
  
with open('navegacion (4).csv', 'wb') as dec_file: 
    dec_file.write(decrypted) 

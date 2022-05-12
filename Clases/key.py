# import required module
from cryptography.fernet import Fernet

#key generation
key = Fernet.generate_key()
  
# string the key in a file
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)
# using the key
fernet = Fernet(key)

# opening the encrypted file
with open('conversiones.csv', 'rb') as enc_file:
	encrypted = enc_file.read()

# decrypting the file
decrypted = fernet.decrypt(encrypted)

# opening the file in write mode and
# writing the decrypted data
with open('conversiones.csv', 'wb') as dec_file:
	dec_file.write(decrypted)


from encryption import encrypt_file, generate_key
from decryption import decrypt_file

inputFilePath = 'windmill.jpg'
outputFilePath = 'encrypted.enc'
password = 'windmillimage'
key = generate_key(password)

encrypt_file(inputFilePath, outputFilePath, key)
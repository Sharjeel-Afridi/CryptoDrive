from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os

def encrypt_file(inputFilePath, outputFilePath, key):
    chunk_size = 64*1024
    init_vector = os.urandom(16)
    encryptor = AES.new(key, AES.MODE_CBC, init_vector)

    with open(inputFilePath, 'rb') as inputFile:
        with open(outputFilePath, 'wb') as outputFile:
            outputFile.write(init_vector)

            while True:
                chunk = inputFile.read(chunk_size)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' '*(16 - len(chunk) % 16)

                outputFile.write(encryptor.encrypt(chunk))

def generate_key(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()



input_file_path = 'windmill.jpg'
output_file_path = 'encrypted_file.enc'
password = 'windmillimage'
key = generate_key(password)

encrypt_file(input_file_path, output_file_path, key)
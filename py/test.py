from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import os

def encrypt_file(input_file_path, output_file_path, password):
    key = PBKDF2(password, salt=get_random_bytes(16), dkLen=32)  # Derive a key from the password
    cipher = AES.new(key, AES.MODE_CBC)  # Create AES cipher in CBC mode
    init_vector = cipher.iv  # Get the initialization vector
    with open(input_file_path, 'rb') as input_file:
        with open(output_file_path, 'wb') as output_file:
            output_file.write(init_vector)  # Write the initialization vector to the output file
            while True:
                chunk = input_file.read(16)  # Read 16 bytes at a time
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:  # Pad the last chunk if necessary
                    chunk += b' ' * (16 - len(chunk) % 16)
                encrypted_chunk = cipher.encrypt(chunk)  # Encrypt the chunk
                output_file.write(encrypted_chunk)  # Write the encrypted chunk to the output file

def decrypt_file(input_file_path, output_file_path, password):
    with open(input_file_path, 'rb') as input_file:
        init_vector = input_file.read(16)  # Read the initialization vector from the input file
        key = PBKDF2(password, salt=get_random_bytes(16), dkLen=32)  # Derive a key from the password
        cipher = AES.new(key, AES.MODE_CBC, iv=init_vector)  # Create AES cipher in CBC mode with the initialization vector
        with open(output_file_path, 'wb') as output_file:
            while True:
                chunk = input_file.read(16)  # Read 16 bytes at a time
                if len(chunk) == 0:
                    break
                decrypted_chunk = cipher.decrypt(chunk)  # Decrypt the chunk
                output_file.write(decrypted_chunk)  # Write the decrypted chunk to the output file

# Example usage
input_file_path = 'windmill.jpg'
encrypted_file_path = 'encrypted_file.enc'
decrypted_file_path = 'decrypted_file.jpg'
password = 'windimage'

encrypt_file(input_file_path, encrypted_file_path, password)
decrypt_file(encrypted_file_path, decrypted_file_path, password)

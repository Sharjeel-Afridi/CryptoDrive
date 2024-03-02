from Crypto.Cipher import AES
from encryption import generate_key

def decrypt_file(inputFilePath, outputFilePath, key):
    chunk_size = 64 * 1024

    with open(inputFilePath, 'rb') as inputFile:
        init_vector = inputFile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, init_vector)

        with open(outputFilePath, 'wb') as outputFile:
            while True:
                chunk = inputFile.read(chunk_size)
                if len(chunk) == 0:
                    break
                decrypted_chunk = decryptor.decrypt(chunk)
                outputFile.write(decrypted_chunk)

input_file_path = 'encrypted_file.enc'
output_file_path = 'decrypted_file.jpg'
password = 'your_password_here'
key = generate_key(password)

decrypt_file(input_file_path, output_file_path, key)


input_file_path = 'encrypted_file.enc'
output_file_path = 'decrypted_file.jpg'
password = 'your_password_here'
key = generate_key(password)

decrypt_file(input_file_path, output_file_path, key)
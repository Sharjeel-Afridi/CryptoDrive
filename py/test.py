from cryptography.fernet import Fernet
import os

class Encryptor():

    def key_create(self):
        key = Fernet.generate_key()
        return key

    # def encrypt_keyVal(keyValue, password):
    #     key_bytes = password.encode('utf-8')
    #     message_bytes = keyValue.encode('utf-8')
    #     iv = get_random_bytes(AES.block_size)
    #     cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    #     padded_message = pad(message_bytes, AES.block_size)
    #     ciphertext_bytes = cipher.encrypt(padded_message)
    #     ciphertext = b64encode(iv + ciphertext_bytes).decode('utf-8')
    #     return ciphertext

    def key_write(self, key, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(key)

    def key_load(self, key_name):
        with open(key_name, 'rb') as mykey:
            key = mykey.read()
        return key

    # def decrypt_keyVal(ciphertext, password):
    #     key_bytes = password.encode('utf-8')
    #     ciphertext_bytes = b64decode(ciphertext)
    #     iv = ciphertext_bytes[:AES.block_size]
    #     cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    #     ciphertext_bytes = ciphertext_bytes[AES.block_size:]
    #     decrypted_bytes = cipher.decrypt(ciphertext_bytes)
    #     plaintext_bytes = unpad(decrypted_bytes, AES.block_size)
    #     plaintext = plaintext_bytes.decode('utf-8')
    #     return plaintext

    def file_encrypt(self, key, original_file, encrypted_file):
        
        f = Fernet(key)

        with open(original_file, 'rb') as file:
            original = file.read()

        encrypted = f.encrypt(original)

        with open (encrypted_file, 'wb') as file:
            file.write(encrypted)

    def file_decrypt(self, key, encrypted_file, decrypted_file):
        
        f = Fernet(key)

        with open(encrypted_file, 'rb') as file:
            encrypted = file.read()

        decrypted = f.decrypt(encrypted)

        with open(decrypted_file, 'wb') as file:
            file.write(decrypted)
 

if __name__ == '__main__':     
    encryptor = Encryptor()

    keyVal = encryptor.key_create()

    # encryptedKey = encryptor.encrypt_keyVal(keyVal, 'testkey')
    
    encryptor.key_write(keyVal, 'mykey.key')

    loaded_key = encryptor.key_load('mykey.key')

    # decryptedKey = encryptor.decrypt_keyVal(loaded_key, 'testkey')

    encryptor.file_encrypt(loaded_key, '/Users/avyuktsoni/Downloads/windmill.jpg', 'enc_image.txt')

    encryptor.file_decrypt(loaded_key, 'enc_image.txt', 'dec_image.jpg')
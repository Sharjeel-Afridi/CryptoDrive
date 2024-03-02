from cryptography.fernet import Fernet
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import os

class Encryptor():

    def key_create(self):
        key = Fernet.generate_key()
        return key

    def encrypt_keyVal(keyValue, password):
        key = base64.b64encode(password.encode())[:32]  # Use first 32 bytes of base64-encoded password as key
        iv = os.urandom(16)  # Generate random initialization vector
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        ciphertext = cipher.encrypt(pad(keyValue.encode(), AES.block_size))
        return base64.b64encode(iv + ciphertext).decode() 

    def key_write(self, key, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(key)

    def key_load(self, key_name):
        with open(key_name, 'rb') as mykey:
            key = mykey.read()
        return key

    def decrypt_keyVal(ciphertext, password):
        key = base64.b64encode(password.encode())[:32]  # Use first 32 bytes of base64-encoded password as key
        ciphertext = base64.b64decode(ciphertext.encode())  # Decode base64-encoded ciphertext
        iv = ciphertext[:16]  # Extract IV
        ciphertext = ciphertext[16:]  # Extract ciphertext
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        decrypted_text = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decrypted_text.decode()

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

    encryptedKey = encryptor.encrypt_keyVal(keyVal, 'testkey')
    
    encryptor.key_write(encryptedKey, 'mykey.key')

    loaded_key = encryptor.key_load('mykey.key')

    decryptedKey = encryptor.decrypt_keyVal(loaded_key, 'testkey')

    encryptor.file_encrypt(decryptedKey, '/Users/avyuktsoni/Downloads/windmill.jpg', 'enc_image.txt')

    encryptor.file_decrypt(decryptedKey, 'enc_image.txt', 'dec_image.jpg')
from flask import Flask, render_template, jsonify, request
from test import Encryptor
import os
import requests

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['image']

    upload_dir = '../static/'

    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # Save the uploaded file to the upload directory
    file_path = os.path.join(upload_dir, file.filename)
    file.save(file_path)
    # Do something with the file, such as saving it to a folder or processing it
    key = load_key('../mykey.key')
    # decryptedKey = encryptor.decrypt_keyVal(key, 'testkey')
    encryptor = Encryptor()

    encrypted_image = encryptor.file_encrypt(key,file_path, "enc_image.txt")

    return jsonify({'message': 'File uploaded successfully'})

def load_key(key_file):
    with open(key_file, 'rb') as mykey:
        key = mykey.read()
    return key

if __name__ == '__main__':
    app.run(debug=True)

# inputFilePath = 'windmill.jpg'
# outputFilePath = 'encrypted.enc'
# password = 'windmillimage'
# key = generate_key(password)

# encrypt_file(inputFilePath, outputFilePath, key)
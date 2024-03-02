from flask import Flask, render_template, jsonify, request
from encryptor import Encryptor
import os
import requests

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['image']

    upload_dir = '../static'

    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    file_path = os.path.join(upload_dir, file.filename)
    file.save(file_path)
    encryptor = Encryptor()
    keyVal = encryptor.key_create()
    encryptor.key_write(keyVal, '../mykey.key')
    loaded_key = encryptor.key_load('../mykey.key')

    encryptor.file_encrypt(loaded_key, file_path, './enc_image.txt')
    encryptor.file_decrypt(loaded_key, './enc_image.txt', 'dec_image.jpg')
    return jsonify({'message': 'File uploaded successfully'})


if __name__ == '__main__':
    app.run(debug=True)

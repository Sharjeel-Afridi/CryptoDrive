from flask import Flask, render_template, jsonify, request
from encryptor import Encryptor
from firebase_storage import upload_file_to_storage, download_file_from_storage
from firebase_init import blobs
import os
import requests

app = Flask(__name__)
name_list = []

for blob in blobs:
    name_list.append(blob.name)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['image']

    upload_dir = './static'

    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    file_path = os.path.join(upload_dir, file.filename)
    file.save(file_path)
    encryptor = Encryptor()
    keyVal = encryptor.key_create()
    encryptor.key_write(keyVal, './mykey.txt')
    loaded_key = encryptor.key_load('./mykey.txt')

    fileName = file.filename.split('.')[0]

    encryptor.file_encrypt(loaded_key, file_path, f'{fileName}.txt')
    upload_file_to_storage(f'./{fileName}.txt', f'{fileName}.txt')

    return "File Uploaded"
    # for blob in blobs:
    #     name_list.append(blob.name)

    # encryptor.file_decrypt(loaded_key, f'{trimmedFileName}.txt', f'{file.filename}_dec.jpg')

    

@app.route('/refresh', methods=['GET'])
def refresh():
    for blob in blobs:
        name_list.append(blob.name)


@app.route('/api/data', methods=['GET', 'POST'])
def get_data():
    
    data = {}
    data.update({"name": name_list})
    print(data)
    return data

@app.route('/send', methods=['POST'])
def send_data():
    
    filename = request.data.decode('utf-8')  # Assuming the filename is sent as a string
    # print('Received filename:', filename)
    # download_file_from_storage(f'{}.txt', )

    # return 'Filename received successfully', 200


if __name__ == '__main__':
    app.run(debug=True, port=8080)

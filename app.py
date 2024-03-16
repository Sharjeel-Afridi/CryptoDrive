from flask import Flask, jsonify, request
from flask_cors import CORS

from pyenc.encryptor import Encryptor

# from firebase_storage import upload_file_to_storage, download_file_from_storage

# from firebase_init import blobs
# from firebase_admin import storage
import os, os.path

from driveapi import auth
from uploadFile import upload_file_to_drive
from downloadFile import download_file_from_drive
from fileSearch import search_files_by_name
from allFileList import list_files

app = Flask(__name__)
CORS(app)

name_list = []

encryptor = Encryptor()

def update_name_list():
   
    return list_files()
   

@app.route('/login', methods=['GET'])
def login():
    auth()
    return "login";


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['image']

    upload_dir = './static/uploaded'

    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    file_path = os.path.join(upload_dir, file.filename)
    file.save(file_path)
    keyVal = encryptor.key_create()
    encryptor.key_write(keyVal, './mykey.txt')
    loaded_key = encryptor.key_load('./mykey.txt')

    encryptor.file_encrypt(loaded_key, file_path, f'./static/encryptedLocal/{file.filename}.enc')
    # upload_file_to_storage(f'./static/encryptedLocal/{file.filename}.enc', f'{file.filename}.enc')
    upload_file_to_drive(f'./static/encryptedLocal/{file.filename}.enc', f'{file.filename}.enc')

    return jsonify({'Result': 'File Uploaded Successfully'})


@app.route('/api/data', methods=['GET', 'POST'])
def get_data():
    name_list = update_name_list()
    data = {}
    data.update({"name": name_list})
    return data

@app.route('/send', methods=['POST','GET'])
def send_data():
    
    data = request.json

    filename = data.get('filename')
    fileName = filename.split('.')[0]+'.'+filename.split('.')[-2]
    # download_file_from_storage(f'{filename}', f'./static/encryptedCloud/enc_{fileName}')
    
    file_id = search_files_by_name(f'{filename}')
    
    download_file_from_drive(file_id, f'./static/encryptedDrive/enc_{fileName}')
    
    key_chk = data.get('input')
    print(key_chk)
    if len(key_chk) == 44:
        try:
            encryptor.file_decrypt(key_chk, f'./static/encryptedDrive/enc_{fileName}', f'./static/decrypted/dec_{fileName}')
            if os.path.exists(f'./static/decrypted/dec_{fileName}') == True:
                print('Correct Key!')
        except:
            print('Incorrect Key!')
    else:
        print('Incorrect Key!')
    return jsonify({'Result': 'Success'})

if __name__ == '__main__':
    app.run(debug=True, port=8080)

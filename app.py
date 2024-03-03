from flask import Flask, render_template, jsonify, request
from encryptor import Encryptor
from firebase_storage import upload_file_to_storage, download_file_from_storage
from firebase_init import blobs
import os, os.path, requests

app = Flask(__name__)
name_list = []

encryptor = Encryptor()

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
    keyVal = encryptor.key_create()
    encryptor.key_write(keyVal, './mykey.txt')
    loaded_key = encryptor.key_load('./mykey.txt')

    encryptor.file_encrypt(loaded_key, file_path, f'{file.filename}.txt')
    upload_file_to_storage(f'./{file.filename}.txt', f'{file.filename}.txt')


@app.route('/api/data', methods=['GET', 'POST'])
def get_data():
    
    data = {}
    data.update({"name": name_list})
    return data

@app.route('/send', methods=['POST'])
def send_data():
    
    filename = request.data.decode('utf-8')
    fileName = filename.split('.')[0]+'.'+filename.split('.')[1]
    download_file_from_storage(f'{filename}', f'enc_{fileName}')
    
    key_chk = 'LQFyje1-DRdd9x8HPjgx5nw7QDu-TcvNCIdEJojtYxg='

    if len(key_chk) == 44:
        try:
            encryptor.file_decrypt(key_chk, filename, f'dec_{fileName}')
            if os.path.exists(f'dec_{fileName}') == True:
                print('Correct Key!')
        except:
            print('Incorrect Key!')
    else:
        print('Incorrect Key!')
        

if __name__ == '__main__':
    app.run(debug=True, port=8080)

from driveAPI.driveapi import auth
import io
from googleapiclient.http import MediaIoBaseUpload

def upload_file_to_drive(file_path, file_name):
    service = auth()

    file_metadata = {
        'name': file_name
    }

    media = MediaIoBaseUpload(io.FileIO(file_path, 'rb'), mimetype='application/octet-stream', resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print('File ID:', file.get('id'))
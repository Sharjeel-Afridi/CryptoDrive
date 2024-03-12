from driveapi import auth
import io
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseUpload

def upload_file_to_drive(file_path, file_name):
  
  try:
    service = auth()
    
    file_metadata = {
        'name': file_name
    }

    media = MediaIoBaseUpload(io.FileIO(file_path, 'rb'), mimetype='application/octet-stream', resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print('File ID:', file.get('id'))
    
  except HttpError as error:
  # TODO(developer) - Handle errors from drive API.
    print(f"An error occurred: {error}")
    
# create_file()
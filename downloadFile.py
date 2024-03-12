from driveapi import auth
from googleapiclient.http import MediaIoBaseDownload

def download_file_from_drive(file_id, file_path):
    
    service = auth()
    request = service.files().get_media(fileId=file_id)
    
    with open(file_path, 'wb') as f:
        downloader = MediaIoBaseDownload(f, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()

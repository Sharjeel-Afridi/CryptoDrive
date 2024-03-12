from googleapiclient.discovery import build
from driveAPI.driveapi import auth

def search_files_by_name(file_name):
    
    service = auth()
    query = f"name = '{file_name}'"
    response = service.files().list(q=query, fields='files(id)').execute()
    files = response.get('files', [])
    file_ids = [file['id'] for file in files]
    return file_ids[0]
from googleapiclient.discovery import build
from driveapi import auth

def search_files_by_name(file_name):
    # service = build('drive', 'v3', credentials=auth())
    service = auth()
    query = f"name = '{file_name}'"
    response = service.files().list(q=query, fields='files(id)').execute()
    files = response.get('files', [])
    file_ids = [file['id'] for file in files]
    return file_ids[0]

# Example usage
# file_name = 'Admission_card.pdf'
# file_ids = search_files_by_name(file_name)
# print("File IDs:", file_ids[0])

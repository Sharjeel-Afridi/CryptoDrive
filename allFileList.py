from google.oauth2 import service_account
from googleapiclient.discovery import build
from driveapi import auth

# def list_all_items():
#     service = auth()
#     page_token = None
#     all_items = []
#     name_list = []

#     while True:
#         response = service.files().list(
#             pageSize = 100,
#             fields='nextPageToken, files(id, name, mimeType)',
#             pageToken=page_token
#         ).execute()

#         items = response.get('files', [])
#         all_items.extend(items)

#         page_token = response.get('nextPageToken')
#         if not page_token:
#             break
#     for item in all_items:
#         name_list.append(item['name'])
#     return name_list

# print(list_all_items())

def list_files():
    
    service = auth()
    name_list = []
    
    response = service.files().list(
        pageSize=100,
        fields="files(id, name)"
    ).execute()
    files = response.get('files', [])
    
    for file in files:
        name_list.append(file['name'])
        
    return name_list
        
# print(list_files())
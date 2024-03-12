from google.oauth2 import service_account
from googleapiclient.discovery import build
from driveapi import auth

def list_all_items():
    # drive_service = build('drive', 'v3', credentials=auth())
    service = auth()
    page_token = None
    all_items = []
    name_list = []

    while True:
        response = service.files().list(
            pageSize = 100,
            fields='nextPageToken, files(id, name, mimeType)',
            pageToken=page_token
        ).execute()

        items = response.get('files', [])
        all_items.extend(items)

        page_token = response.get('nextPageToken')
        if not page_token:
            break
    for item in all_items:
        name_list.append(item['name'])
    return name_list

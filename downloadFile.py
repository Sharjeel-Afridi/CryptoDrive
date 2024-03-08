from googleapiclient.discovery import build
from driveapi import auth
from googleapiclient.http import MediaIoBaseDownload

def download_file_from_drive(file_id, file_path):
    service = build('drive', 'v3', credentials=auth())
    
    request = service.files().get_media(fileId=file_id)
    
    with open(file_path, 'wb') as f:
        downloader = MediaIoBaseDownload(f, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()

# Example usage
# drive_service = authenticate('path/to/service_account_key.json')
# file_id = '110Ug6kouhunaR1X-X2552j7ek7RBOEWT45DCbq5-UKM'
# download_file(file_id, 'infobyte.png')


# def download_google_doc(file_id, file_path, export_format='pdf'):
    
#     service = build('drive', 'v3', credentials=auth())
    
#     request = service.files().export_media(fileId=file_id, mimeType=f'application/{export_format}')
#     with open(file_path, 'wb') as f:
#         downloader = MediaIoBaseDownload(f, request)
#         done = False
#         while done is False:
#             status, done = downloader.next_chunk()

# # Example usage
# file_id = '110Ug6kouhunaR1X-X2552j7ek7RBOEWT45DCbq5-UKM'
# download_google_doc(file_id, 'infobyte.pdf', export_format='pdf')



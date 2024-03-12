# import os.path

# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build

# SCOPES = ["https://www.googleapis.com/auth/drive"]

# def auth():
#   creds = None

#   if os.path.exists("token.json"):
#     creds = Credentials.from_authorized_user_file("token.json", SCOPES)

#   if not creds or not creds.valid:
#     if creds and creds.expired and creds.refresh_token:
#       creds.refresh(Request())
#     else:
#       flow = InstalledAppFlow.from_client_secrets_file(
#           'client_secret.json', SCOPES
#       )
#       creds = flow.run_local_server(port=8000)
#     # Save the credentials for the next run
#     with open("token.json", "w") as token:
#       token.write(creds.to_json())
            
#     return creds


import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
# SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]
SCOPES = ["https://www.googleapis.com/auth/drive"]

def auth():
  """Shows basic usage of the Drive v3 API.
  Prints the names and ids of the first 10 files the user has access to.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "client_secret.json", SCOPES
      )
      creds = flow.run_local_server(port=2020)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())
            
  # return creds

  try:
    service = build("drive", "v3", credentials=creds)
    
    return service

    # # Call the Drive v3 API
    # file_metadata = {
    #     'name': 'imgOfMe.jpg'
    # }
    # if folder_id:
    #     file_metadata['parents'] = [folder_id]

    # media = MediaIoBaseUpload(io.FileIO('./IMG_5669.JPG', 'rb'), mimetype='application/octet-stream', resumable=True)
    # file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    # print('File ID:', file.get('id'))
  #   results = (
  #       service.files()
  #       .list(pageSize=20, fields="nextPageToken, files(id, name)")
  #       .execute()
  #   )
  #   items = results.get("files", [])

  #   if not items:
  #     print("No files found.")
  #     return
  #   print("Files:")
  #   for item in items:
  #     print(f"{item['name']} ({item['id']})")
  except HttpError as error:
    # TODO(developer) - Handle errors from drive API.
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  auth()
  # create_folder()
  # print(auth())
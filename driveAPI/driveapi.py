import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/drive"]

def auth():

    creds = None

    if os.path.exists("token.json"):
      creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "./client_secret.json", SCOPES
        )
        creds = flow.run_local_server(port=2020)

      with open("token.json", "w") as token:
        token.write(creds.to_json())     

    try:
      service = build("drive", "v3", credentials=creds)
      return service
    
    except HttpError as error:
      print(f"An error occurred: {error}")
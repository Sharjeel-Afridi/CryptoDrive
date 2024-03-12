import firebase_admin
from firebase_admin import credentials, storage

cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

storage_client = storage.bucket('cryptodrive-team96.appspot.com')

blobs = storage_client.list_blobs()

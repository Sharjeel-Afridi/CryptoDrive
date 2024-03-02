from firebase_init import storage_client

def upload_file_to_storage(file_path, destination_blob_name):
    blob = storage_client.blob(destination_blob_name)
    blob.upload_from_filename(file_path)

def download_file_from_storage(source_blob_name, destination_file_path):
    blob = storage_client.blob(source_blob_name)
    blob.download_to_filename(destination_file_path)
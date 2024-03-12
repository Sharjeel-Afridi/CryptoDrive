from driveapi import auth

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
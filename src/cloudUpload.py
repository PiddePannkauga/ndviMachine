from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.http import MediaFileUpload
from google.oauth2 import service_account

class CloudUpload:
    



<<<<<<< HEAD
    def __init__(self,fileNameToCloud):
        self.fileName = fileNameToCloud
=======
    def __init__(self,filePath,fileName):
        self.filePath = filePath
        self.fileName = fileName
>>>>>>> Version 2 Av kamera

 
    def upload(self):
        SCOPE = ["https://www.googleapis.com/auth/drive.file"]
<<<<<<< HEAD
        SERVICE_ACCOUNT_FILE = '/home/pi/Exjobb/ndviMachine/src/secrets/serviceaccount.json'
=======
        SERVICE_ACCOUNT_FILE = '/home/pi/ndviMachine/src/secrets/serviceaccount.json'
>>>>>>> Version 2 Av kamera
        new_permission = {
                'emailAddress': "petter.mansson1@gmail.com",
                'type': "user",
                'role': "writer"
             }
<<<<<<< HEAD

        file_metadata = {"name": self.fileName}
        media = MediaFileUpload(self.fileName, mimetype = 'image/png')
=======
        
        folder_id = '1lCeaVlXoaX9DxuXTl900QynK1Yy8XeL2'

        file_metadata = {'name': self.fileName,
                        'parents': [folder_id]}
        media = MediaFileUpload(self.filePath, mimetype = 'image/png')
>>>>>>> Version 2 Av kamera
        


        credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPE)

        service = build("drive", "v3" , credentials = credentials)

<<<<<<< HEAD


        getFile = service.files().get(fileId='K7gWh_d6Wb7ojlvqp0tl4wt7B')

        file = service.files().create(body=file_metadata,media_body = media, fields = "id").execute()

        service.permissions().create(fileId=file['id'],body = new_permission).execute()
=======
 

        file = service.files().create(body=file_metadata,media_body = media, fields = "parents").execute() 
>>>>>>> Version 2 Av kamera

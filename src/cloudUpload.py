from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.http import MediaFileUpload
from google.oauth2 import service_account

class CloudUpload:
    

    def __init__(self,filePath,fileName):
        self.filePath = filePath
        self.fileName = fileName

 
    def upload(self):
        SCOPE = ["https://www.googleapis.com/auth/drive.file"]

        SERVICE_ACCOUNT_FILE = '/home/pi/ndviMachine/src/secrets/serviceaccount.json'

        
        folder_id = '1lCeaVlXoaX9DxuXTl900QynK1Yy8XeL2'

        file_metadata = {'name': self.fileName,
                        'parents': [folder_id]}
        media = MediaFileUpload(self.filePath, mimetype = 'image/png')


        credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPE)

        service = build("drive", "v3" , credentials = credentials)

        file = service.files().create(body=file_metadata,media_body = media, fields = "parents").execute() 


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

        
        folder_id_Fastie = '1lCeaVlXoaX9DxuXTl900QynK1Yy8XeL2'
        folder_id_NDVI = '1MFCb9E29KAPOwMIgYENohiWHtFzIOdRM'

        file_metadata_Fastie = {'name': self.fileName,
                        'parents': [folder_id_Fastie]}
        media_Fastie = MediaFileUpload(self.filePath+'/output/'+self.fileName, mimetype = 'image/png')
        
        file_metadata_NDVI = {'name': self.fileName,
                        'parents': [folder_id_NDVI]}
        media_NDVI = MediaFileUpload('/home/pi/ndviMachine/src/ndvi/'+self.fileName, mimetype = 'image/png')

        credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPE)

        service = build("drive", "v3" , credentials = credentials)

        file = service.files().create(body=file_metadata_Fastie,media_body = media_Fastie, fields = "parents").execute() 
        
        file = service.files().create(body=file_metadata_NDVI,media_body = media_NDVI, fields = "parents").execute() 


from PIL import Image, ImageFilter
import time

class PreProcess:

    def __init__(self, imagePath):
        self.imagePath = imagePath
        

    def resize(self):

        img = Image.open(self.imagePath)

        imgResize = img.resize((800,600), Image.LANCZOS)
         
        timestamp = time.localtime().tm_sec
        
        imgFileName = "resized{}".format(timestamp)
        imgResize.save(imgFileName, "jpeg")

        
        return imgFileName

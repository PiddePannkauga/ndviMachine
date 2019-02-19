from PIL import Image, ImageFilter
import time

class PreProcess:

    def __init__(self,sourcePath,imagePath):
        self.imagePath = imagePath
        self.sourcePath = sourcePath
    
           


    def resize(self):

        img = Image.open(self.imagePath)

        imgResize = img.resize((800,600), Image.LANCZOS)
         
        self.timestamp = self.timestamp = "{}-{}-{}-{}-{}-{}".format(time.gmtime().tm_year,time.gmtime().tm_mon,time.gmtime().tm_mday,time.gmtime().tm_hour,time.gmtime().tm_min,time.gmtime().tm_sec)


        imgResizePath = "{}/output/resized{}.png".format(self.sourcePath,self.timestamp)
        imgResize.save(imgResizePath, "png")

        return imgResizePath


    
        

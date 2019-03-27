from picamera import PiCamera
import time
from fractions import Fraction 
class TakePicture:
    
    camera = PiCamera()
    redAWB=2.26
    blueAWB=0.74
    customGains = (redAWB, blueAWB)
    camera.awb_mode = "off"
    camera.awb_gains = customGains
#    camera.hflip = True
#    camera.vflip = True   
    camera.resolution = (1920,1080)
    
   # camera.framerate = Fraction(1,6)
   # camera.shutter_speed = 6000000
    #camera.exposure_mode = 'off'

   # camera.iso = 800
    




    def capture(self,path):
        self.path = "{}/input/testAWB.png".format(path)
        time.sleep(3)
        self.camera.capture(self.path, "png")
        self.camera.close()
        
        
        return self.path


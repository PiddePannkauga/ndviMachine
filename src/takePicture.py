from picamera import PiCamera
class TakePicture:
    
    camera = PiCamera()
    redAWB=1.43
    blueAWB=0.86
    customGains = (redAWB, blueAWB)
    camera.awb_mode = "off"
    camera.awb_gains = customGains
    camera.hflip = True
    camera.vflip = True
<<<<<<< HEAD
    
=======
    camera.resolution = (1920,1080)
#:    camera.exposure_mode = 'off'
>>>>>>> Version 2 Av kamera

    def capture(self,path):
        self.path = "{}/input/testAWB.png".format(path)
        self.camera.capture(self.path, "png")
        self.camera.close()
        
        
        return self.path


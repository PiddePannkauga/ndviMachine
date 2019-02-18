from picamera import PiCamera
class TakePicture:
    
    camera = PiCamera()
    redAWB=1.43
    blueAWB=0.86
    customGains = (redAWB, blueAWB)
    camera.awb_mode = "off"
    camera.awb_gains = customGains

    def capture(self):
        self.camera.capture("testAWB.png", "png")
        return "testAWB.png"


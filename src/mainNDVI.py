
from takePicture import TakePicture
from imgPreProcess import PreProcess
from subprocess import Popen
camera = TakePicture()

imgFileName=camera.capture()
preProcess = PreProcess(imgFileName)

imgResizeFileName=preProcess.resize()
process = 'infrapix_single -i {} -o ndvi_{}.png'.format("./"+imgResizeFileName, imgResizeFileName)
Popen(process, shell=True,executable="/bin/bash")





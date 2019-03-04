#!/usr/bin/env python

#PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/sbin:/bin:/home/pi/Exjobb/ndviMachine/src/

from takePicture import TakePicture
from imgPreProcess import PreProcess
from subprocess import Popen
from cloudUpload import CloudUpload
<<<<<<< HEAD
=======
import imgNdviProcess 
>>>>>>> Version 2 Av kamera
import os
import time
import signal

<<<<<<< HEAD
filePath = '/home/pi/Exjobb/ndviMachine/src'
=======
filePath = '/home/pi/ndviMachine/src'
>>>>>>> Version 2 Av kamera


camera = TakePicture()

imgFileName=camera.capture(filePath)
preProcess = PreProcess(filePath,imgFileName)


imgResizeFilePath=preProcess.resize()
<<<<<<< HEAD
process = '/usr/local/bin/infrapix_single -i {} -o {}ndvi_{}.png'.format(imgResizeFilePath,filePath+"/output/", preProcess.timestamp)
popen=Popen(process, shell=True,executable="/bin/bash", preexec_fn=os.setsid)

processedFile = "{}ndvi_{}.png".format(filePath+"/output/",preProcess.timestamp)


while not os.path.exists(processedFile):
    print("Fil processeras")
    time.sleep(10)

os.killpg(os.getpgid(popen.pid), signal.SIGTERM)

cloudUpload = CloudUpload(processedFile)

=======

processedImgFilename = "ndvi_{}.png".format(preProcess.timestamp)
processedImgOutputPath = filePath+"/output/"+processedImgFilename


processedFile=imgNdviProcess.ndvi(imgResizeFilePath,processedImgOutputPath)
#process = '/usr/local/bin/infrapix_single -i {} -o {}ndvi_{}.png'.format(imgResizeFilePath,filePath+"/output/", preProcess.timestamp)
#popen=Popen(process, shell=True,executable="/bin/bash", preexec_fn=os.setsid)



while not os.path.exists(processedImgOutputPath):
    print("Fil processeras")
    time.sleep(5)

#os.killpg(os.getpgid(popen.pid), signal.SIGTERM)

cloudUpload = CloudUpload(processedImgOutputPath,processedImgFilename)
>>>>>>> Version 2 Av kamera
cloudUpload.upload()




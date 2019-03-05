#!/usr/bin/env python

#PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/sbin:/bin:/home/pi/Exjobb/ndviMachine/src/

from takePicture import TakePicture
from imgPreProcess import PreProcess
from cloudUpload import CloudUpload
import imgNdviProcess 
import os
import time
import signal

filePath = '/home/pi/ndviMachine/src'


camera = TakePicture()

imgFileName=camera.capture(filePath)
preProcess = PreProcess(filePath,imgFileName)


imgResizeFilePath=preProcess.resize()


processedImgFilename = "ndvi_{}.png".format(preProcess.timestamp)
processedImgOutputPath = filePath+"/output/"+processedImgFilename


processedFile=imgNdviProcess.ndvi(imgResizeFilePath,processedImgOutputPath)


while not os.path.exists(processedImgOutputPath):
    print("Fil processeras")
    time.sleep(5)

cloudUpload = CloudUpload(processedImgOutputPath,processedImgFilename)
cloudUpload.upload()




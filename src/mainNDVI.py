#!/usr/bin/env python

#PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/sbin:/bin:/home/pi/Exjobb/ndviMachine/src/

from takePicture import TakePicture
from imgPreProcess import PreProcess
from cloudUpload import CloudUpload
import matplotlib
import imgNDVIProcess 
import os
import time
import signal

matplotlib.use('Agg')

filePath = './'

camera = TakePicture()
imgFileName=camera.capture(filePath)

preProcess = PreProcess(filePath,imgFileName)
preProcess.resize()

processedImgFilename = "ndvi_{}.png".format(preProcess.timestamp)

processedFile=imgNDVIProcess.ndvi(preProcess.imgResizePath,processedImgFilename,'./output/'+processedImgFilename)


while not os.path.exists(filePath+'output/'+processedImgFilename):
    print("Fil processeras")
    time.sleep(5)
print(preProcess)
cloudUpload = CloudUpload(filePath,processedImgFilename,preProcess.imgResizePath,preProcess.timestamp)
cloudUpload.upload()




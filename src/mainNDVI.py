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

filePath = '/home/pi/ndviMachine/src'


camera = TakePicture()

imgFileName=camera.capture(filePath)
preProcess = PreProcess(filePath,imgFileName)


imgResizeFilePath=preProcess.resize()


processedImgFilename = "ndvi_{}.png".format(preProcess.timestamp)



processedFile=imgNDVIProcess.ndvi(imgResizeFilePath,processedImgFilename,filePath+'/output/'+processedImgFilename)


while not os.path.exists(filePath+'/output/'+processedImgFilename):
    print("Fil processeras")
    time.sleep(5)

cloudUpload = CloudUpload(filePath,processedImgFilename)
cloudUpload.upload()




#!/usr/bin/env python

#PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/sbin:/bin:/home/pi/Exjobb/ndviMachine/src/

from takePicture import TakePicture
from imgPreProcess import PreProcess
from subprocess import Popen
from cloudUpload import CloudUpload
import os
import time
import signal

filePath = '/home/pi/Exjobb/ndviMachine/src'


camera = TakePicture()

imgFileName=camera.capture(filePath)
preProcess = PreProcess(filePath,imgFileName)


imgResizeFilePath=preProcess.resize()
process = '/usr/local/bin/infrapix_single -i {} -o {}ndvi_{}.png'.format(imgResizeFilePath,filePath+"/output/", preProcess.timestamp)
popen=Popen(process, shell=True,executable="/bin/bash", preexec_fn=os.setsid)

processedFile = "{}ndvi_{}.png".format(filePath+"/output/",preProcess.timestamp)


while not os.path.exists(processedFile):
    print("Fil processeras")
    time.sleep(10)

os.killpg(os.getpgid(popen.pid), signal.SIGTERM)

cloudUpload = CloudUpload(processedFile)

cloudUpload.upload()




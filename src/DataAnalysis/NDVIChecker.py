from PIL import Image
import numpy as numpy
import numpy.ma as ma
from collections import defaultdict

import math
import os
from sys import argv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
numpy.set_printoptions(threshold=numpy.inf)

#Script for segmentation and data extraction of images under Infragram


onlyWaterBoxCropedImagePath = "./cropedImages/onlyWaterBox/"
nutritionBoxCroppedImagePath = "./cropedImages/nutritionBox/"

onlyWaterBoxNDVI_ImagePath = "./NDVI_Images/onlyWaterBox/"
nutritionBoxNDVI_ImagePath = "./NDVI_Images/nutritionBox/"

onlyWaterBoxGraphValues = defaultdict(list)
nutritionBoxGraphValues = defaultdict(list)

dateKeys = []

def imageSegmentation(path,imageToSegment):#Segments each image and stores the new images in seprate folders.
    nutritionBoxCoords = {"x1":140,"x2":610,"y1":120,"y2":270}
    onlyWaterBoxCoords = {"x1":140,"x2":600,"y1":400,"y2":550}

    timestamp = imageToSegment.split("_")
    
    img = Image.open(path+imageToSegment)

    onlyWaterBoxImage = img.crop((onlyWaterBoxCoords["x1"],onlyWaterBoxCoords["y1"],onlyWaterBoxCoords["x2"],onlyWaterBoxCoords["y2"]))
   
    onlyWaterBoxImage.save(onlyWaterBoxCropedImagePath+"croped_{}.png".format(timestamp[1]),"png")

    nutritionBoxImage = img.crop((nutritionBoxCoords["x1"],nutritionBoxCoords["y1"],nutritionBoxCoords["x2"],nutritionBoxCoords["y2"]))
    
    nutritionBoxImage.save(nutritionBoxCroppedImagePath+"croped_{}.png".format(timestamp[1]), "png")

def ndvi(path,image):

    timestamp = image.split("_")

    img = Image.open(image)

    imgR, imgG, imgB, imgA = img.split()

    arrR = numpy.asarray(imgR).astype('float')
    arrB = numpy.asarray(imgB).astype('float')
    
    redBlueDiff = (arrR - arrB)
    redBlueSum = (arrR + arrB)


    arrNDVI = redBlueDiff/redBlueSum

    imageDataExtraction(path,timestamp[1],arrNDVI)

    plt.imsave(path+"ndvi_{}.png".format(timestamp[1]),arrNDVI,vmin=-1.0, vmax=1.0)


def imageDataExtraction(path,timestamp,NDVIValueArr):#Extracts data to be used with matplot to generate graphs
    
    date = timestamp[0:9]

    if date.endswith("-"):
        date=date[:7] + "0"+date[7] 

    mx = ma.masked_less(NDVIValueArr, 0.25)

    NDVICompressed = numpy.ma.compressed(mx)
    
    #Each image from each day are stored in a list inside a dictionary

    if "onlyWaterBox" in path:
        onlyWaterBoxGraphValues[date].append(NDVICompressed)
    else:
        nutritionBoxGraphValues[date].append(NDVICompressed)

    

def graphGenerator():
    """Generate graph to analyze experiment results
    """

    ndviMeanGraphValues,standardDeviation=statistics("mean")
    fig = plt.figure(figsize=(10,100))
    

# Make room for legend at bottom
    fig.subplots_adjust(bottom=0.2)

# The axes for your lists 1-3
    ax1 = fig.add_subplot(211)

    ax1.set_ylim(0,1)
    ax1.set_xlim(0,len(onlyWaterBoxGraphValues))
    ax1.set_ylabel('NDVI')
    ax1.set_xlabel('Days')
    plt.xticks(numpy.arange(0, len(onlyWaterBoxGraphValues), 1))
    plt.yticks(numpy.arange(0, 1.1, 0.1))

    waterLine = ndviMeanGraphValues["onlyWaterBoxMeanGraphValues"]
    nutritionLine = ndviMeanGraphValues["nutritionBoxMeanGraphValues"]

    waterLine = ax1.plot(waterLine,'#000eff',linewidth=1,label='Only Water',marker=".",markersize=5)
    nutritionLine = ax1.plot(nutritionLine,'#ff0005',linewidth=1,label='Nutrition',marker=".",markersize=5)

    plt.grid()
    plt.legend()
    lines = waterLine+nutritionLine
    
    plt.show()
    

def statistics(typeOfStats):

    #To calculate mean take all images from a day. Calculate mean for each Store each value in array, calculate mean for whole day.
    
    if typeOfStats == "mean":

        meanDictionary = defaultdict(list)
        standardDeviationDict = defaultdict(list)
        meanValues = []
        

        for key,values in sorted(onlyWaterBoxGraphValues.items()):
            
            for ndviValues in values:
       
                if ndviValues.size == 0:
                    meanValues.append(0)
                else:
                    meanValues.append(numpy.mean(ndviValues))
            
            if len(meanValues) == 0:
                mean = 0
            else:
                mean=numpy.mean(meanValues)

            meanValues = []
            
            meanDictionary["onlyWaterBoxMeanGraphValues"].append(mean)
            

        for key,values in sorted(nutritionBoxGraphValues.items()):
            
            for ndviValues in values:
                if ndviValues.size == 0:
                    meanValues.append(0)
                else:
                    meanValues.append(numpy.mean(ndviValues))
            if len(meanValues) == 0:
                mean = 0
            else:
                mean=numpy.mean(meanValues)

            meanDictionary["nutritionBoxMeanGraphValues"].append(mean)
            
            meanValues = []
            
        for key,values in meanDictionary.items():

            standardDeviationDict[key].append(numpy.std(values))

        print(standardDeviationDict.items())

        return meanDictionary,standardDeviationDict


def main(folderWithDataSet):
    imagesToSegment = os.listdir(folderWithDataSet)
    for image in imagesToSegment:
        imageSegmentation(folderWithDataSet,image)

    onlyWaterImagesCroped = os.listdir(onlyWaterBoxCropedImagePath)
    for image in onlyWaterImagesCroped:
        ndvi(onlyWaterBoxNDVI_ImagePath,onlyWaterBoxCropedImagePath+image)

    nutritionImagesCroped = os.listdir(nutritionBoxCroppedImagePath)
    for image in nutritionImagesCroped:
        ndvi(nutritionBoxNDVI_ImagePath,nutritionBoxCroppedImagePath+image)
        

    



main(argv[1])
graphGenerator()

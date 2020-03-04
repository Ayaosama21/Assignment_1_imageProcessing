
# -*- coding: utf-8 -*-
"""
Spyder Editor
code by: Aya Osama
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy import ndarray
import cv2
import numpy as np
image = mpimg.imread('imagessaltandpeper.jpg')
def detection(brain_im):
    status = ""
    ## your code here ##
 #   image = mpimg.imread('imagessaltandpeper.jpg')
    median = cv2.medianBlur(image,5)
    ret,thr = cv2.threshold(median,150,255,cv2.THRESH_BINARY_INV)

    plt.subplot(221)
    plt.imshow(thr)

    #plt.subplot(222)
    #plt.hist(thr.ravel(),256,[0,256]);    #plt.hist(thr.ravel(),256)
    histr = cv2.calcHist([thr],[0],None,[256],[0,256]) 
   # plt.plot(histr)
    #plt.show()
    if histr[0] != 0:
        print("Tumor Detected")
    else:
        print("Tumor Not Detected")
    return status
status = detection(image) # you can change image name according to the filtered one
print(status)
## note: output should be for ex:"Tumor Detected" or "Tumor Not Detected"
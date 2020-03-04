# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 23:02:36 2020

@author: Aya Osama
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import cv2
import numpy as np

image = mpimg.imread('imagessaltandpeper.jpg')

median = cv2.medianBlur(image,5)

#plt.subplot(122)
plt.hist(median.ravel(),256,[0,256]);
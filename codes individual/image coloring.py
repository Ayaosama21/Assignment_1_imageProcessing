# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 23:15:18 2020

@author: Aya Osama
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from copy import deepcopy
import cv2
import numpy as np

# Read in the image 
image = mpimg.imread('HP_train.jpg') 
plt.imshow(image)

red = deepcopy(image)
green = deepcopy(image)
blue = deepcopy(image)

red[:,:,2] = 0    #red
green[:,:,1] = 0    #green
blue[:,:,0]    #blue

red[:,:,2] = 0    #red
green[:,:,1]     #green
blue[:,:,0] = 0   #blue

red[:,:,2]    #red
green[:,:,1] = 0    #green
blue[:,:,0] = 0   #blue

plt.subplot(221)
plt.imshow(red)

plt.subplot(222)
plt.imshow(green)

plt.subplot(212)
plt.imshow(blue)
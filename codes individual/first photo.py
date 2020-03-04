import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import cv2
import numpy as np

#%matplotlib inline
#from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'inline')
# Read in the image
image = mpimg.imread('imagessaltandpeper.jpg')

median = cv2.medianBlur(image,5)
#hist = cv2.calcHist([median],[0],None,[256],[0,256])
#plt.subplot(121)
plt.imshow(median)


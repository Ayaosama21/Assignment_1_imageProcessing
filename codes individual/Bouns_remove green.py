# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 00:26:50 2020

@author: Aya Osama
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import cv2
import numpy as np

import scipy.io as sio
from skimage.io import imread,imsave 
#Read in the image
image = mpimg.imread('HP_Green.jpg') 
# Print out the image dimantions ( height , width , and depth ( color ))
#print('Image dimensions:', image.shape) 
# Display the image 
#plt.imshow(image)
#hsv= cv2.cvt.color(frame,cv2.COLOR_BGR2HSV)
# Define our color selection boundaries in R G B values " change those numbers" 
lower_green = np.array([35, 140, 60]) 
upper_green = np.array([220, 230, 240])

# Define the masked area
mask = cv2.inRange(image, lower_green, upper_green)

# Vizualize the mask
plt.imshow(mask, cmap='gray')

# Mask the image to let the car show through
masked_image = np.copy(image)

masked_image[mask != 0] = [22,232,0]
#22,232,0
#lower_green = np.array([35, 140, 60]) #BGR
#upper_green = np.array([220, 230, 240])

# Display it!
plt.imshow(masked_image)

#convert to HSV
hsv = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
# HSV channels
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

# Visualize the individual color channels
f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20,10))
ax1.set_title('H channel')
ax1.imshow(h, cmap='gray')
ax2.set_title('S channel')
ax2.imshow(s, cmap='gray')
ax3.set_title('V channel')
ax3.imshow(v, cmap='gray')


#Settting colour limit
lower_green_hue = np.array([52]) 
upper_green_hue = np.array([66])

# Define the masked area
hue_mask = cv2.inRange(h, lower_green_hue, upper_green_hue)

hue_masked_image = np.copy(h)

# Convert image to monotone image (255 = car, 0 = background)
hue_masked_image[hue_mask != 0] = [0]
hue_masked_image[hue_mask == 0] = [255]


# Mask the image to show real object
masked_image = np.copy(image)
masked_image[hue_masked_image == 0] = [0, 0, 0]



background_image = mpimg.imread('./images/result.jpg')

out_height = masked_image.shape[0]
out_width = masked_image.shape[1]

print("{} x {}".format(out_width, out_height))

# Resize the image
scale_x = float(out_width) / background_image.shape[1]
scale_y = float(out_height) / background_image.shape[0]
scale = scale_x

if scale_x>1.0 or scale_y>1.0:
    scale = scale_x if scale_x>scale_y else scale_y
    
if scale>1.0:
    background_image = cv2.resize(background_image, background_image.shape*scale) 
    
background_image = background_image[0:out_height, 0:out_width]


# Add masked S channel Mask Back
final_image = background_image.copy()
final_image[hue_masked_image != 0] = [0, 0, 0]
final_image = final_image + masked_image

#Write Image
imsave('3.jpg', final_image)

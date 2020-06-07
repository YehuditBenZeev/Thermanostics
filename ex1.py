import numpy as np
#import skimage
import cv2
#from PIL import Image, ImageFilter
from matplotlib import pyplot as plt
#from skimage import data, io, filters

#from pyimagesearch import imutils
from skimage import exposure
import argparse
import imutils

def showPic(image):
    window_name = 'Image'
    cv2.imshow(window_name, image)
    cv2.waitKey(0)

path = "Im1.jpg"
src = cv2.imread(path)

# Window name in which image is displayed
showPic(src)

#convert image to gray scale
image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# Displaying the image
showPic(image)




border = cv2.bilateralFilter(image, 11, 17, 17)
edged = cv2.Canny(border, 30, 200)

# Displaying the image
cv2.imshow(window_name, border)
cv2.waitKey(0)
cv2.imshow(window_name, edged)
cv2.waitKey(0)


#mask to black & white
ret, thresh = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
cv2.imshow('thresh',thresh)
cv2.waitKey(0)

'''th2=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow('thresh',th2)
cv2.waitKey(0)
th3=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow('thresh',th3)
cv2.waitKey(0)
fin = cv2.bitwise_and(image, image, mask = th3)
cv2.imshow('fin', fin)
cv2.waitKey(0)'''

#return gray scale to hand
fin = cv2.bitwise_and(image, image, mask = thresh)
cv2.imshow('fin', fin)
cv2.waitKey(0)

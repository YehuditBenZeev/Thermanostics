import img as img
import numpy as np
import cv2
import os.path
import sys
import argparse


def showPic(image):
    window_name = 'Image'
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    c = cv2.Canny(image, 500, 500)
    print(c[200])
    cv2.imshow(window_name, c)
    cv2.waitKey(0)


path = "Im1.jpg"
src = cv2.imread(path)
showPic(src)
image = src[:,:,1] # green layer
showPic(image)

#Find hotspots by regions
def fin(p1,p2,h,w):
    temp = 0
    for i in range(p1, h):
        for j in range(p2, w):
            x = image[i][j]
            if x > temp:
                temp = image[i][j]
    return temp
#scan all picture
def ScanImage(h,w):
   print(fin(0,0,(int)(h/10),(int)(w/10)))




img = cv2.imread(path)
h = img.shape[0]
w = img.shape[1]
ScanImage(h,w)






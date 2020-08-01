import numpy as np
#import skimage
import cv2
#from PIL import Image, ImageFilter
#from matplotlib import pyplot as plt
#from skimage import data, io, filters

#from pyimagesearch import imutils
#from skimage import exposure
#import argparse
#import imutils
import scipy
from scipy import ndimage


def showPic(image):
    window_name = 'Image'
    cv2.imshow(window_name, image)
    cv2.waitKey(0)

path = "Im1.jpg"
src = cv2.imread(path)

src = cv2.fastNlMeansDenoisingColored(src,None,10,10,7,21)

aaaa = cv2.imread(path)
height, width = aaaa.shape[0:2]
image = aaaa[:,:,1]

showPic(image)
for i in range(0, height):
    for j in range(0, width):
       # if (aaaa[i][j][2] >=80)  and (aaaa[i][j][1]>=80) and (aaaa[i][j][0] <=150)  : # red , green , blue
      #if (aaaa[i][j][2] <= 80) and (aaaa[i][j][1] <= 80) and (aaaa[i][j][0] >= 150):  # red , green , blue
            aaaa[i][j] = 0


kernel = np.ones((3, 3), np.float32) / 9
aaaa = cv2.filter2D(aaaa, -1, kernel)
showPic(aaaa)


# Window name in which image is displayed
showPic(src)
print(src)

#convert image to gray scale
image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# Displaying the image
showPic(image)
print(image)

im = image[250:500,250:500]
showPic(im)


border = cv2.bilateralFilter(image, 11, 17, 17)
edged = cv2.Canny(border, 30, 200)

# Displaying the image
#showPic(border)
#showPic(edged)
'''
bw = 100 #width of border required
mask = np.ones(image.shape[:2], dtype = "uint8")
cv2.rectangle(mask, (bw,bw),(image.shape[1]-bw,image.shape[0]-bw), 0, -1)
output = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow('out', output)
cv2.waitKey(0)'''


#mask to black & white
ret, thresh = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
showPic(thresh)

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
#showPic(fin)

mask = np.zeros(image.shape,np.uint8)
'''
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(image,mask = mask)
print(min_val)
print(max_val)
print(min_loc)
print(max_loc)'''

print(scipy.ndimage.extrema(input, labels=None, index=None))
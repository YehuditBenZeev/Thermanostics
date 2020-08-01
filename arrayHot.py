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


"""
count = 1
first = 0
temp = np.array([0,0]) # holds: row , column
rows, columns=np.size


finger_width = 0

#print(rows, columns)


for j in range(0, rows-1):
    for i in range(0, columns-1):
        if path[j][i]==0 and path[j][i+1]!=0 :
            print("ll")
           #print(path[i][j])
           """
"""
from PIL import Image
image = Image.open(path)
mask=image.convert("L")
th=150 # the value has to be adjusted for an image of interest
mask = mask.point(lambda i: i < th and 255)
cv2.imread(mask.save(path))
"""
img = cv2.imread(path)
h = img.shape[0]
w = img.shape[1]
temp = image[0][0]
for i in range(0, h):
    for j in range(0, w):
      x=image[i][j]
      print(x)






from mailcap import show

import img as img
import numpy as np
import cv2
import os.path
import sys
import argparse
# importing required libraries
import mahotas


def showPic(image):
    window_name = 'Image'
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    c = cv2.Canny(image, 500, 500)
    #print(c[200])
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

def passOnImage(h, w):
    print(h,"h",w,"w")
    arr=[]
    arrI=[]
    arrJ=[]
    flag1 =False
    flag2 = False
    flag3 = False
    flag4 = False
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            if i-1 >0:
                if image[i-1][j]<image[i][j]:
                    flag1=True
            if j-1 >0:
                if image[i][j-1]<image[i][j]:
                    flag2=True

            if i+1 < h:
                if image[i+1][j]<image[i][j]:
                    flag3=True

            if j+1 < w:
                if image[i][j+1]<image[i][j]:
                    flag4=True
            if flag1 & flag2 & flag3 & flag4 :
                if image[i][j]>40:
                    arr.append(image[i][j])
                    arrI.append(i)
                    arrJ.append(j)
                    print(i,"___",j,"___",image[i][j])


                flag1=False
                flag2=False
                flag3=False
                flag4=False
    print(arr,"arr")
    print(arrI,"arrI")
    print(arrJ,"arrJ")
    for i in range(len(arr)):
        if arrI[i]>50:
            cv2.circle(src, ( arrJ[i],arrI[i]), 4, (255, 128, 0), 2)
            print(arrI[i],arrJ[i])
            break

    showPic(image)








img = cv2.imread(path)
h = img.shape[0]
w = img.shape[1]
ScanImage(h,w)
h, w = image.shape
passOnImage(h,w)

# imgd = mahotas.imread('Im1.jpg')
#
# # fltering image
# imgd = imgd[:, :, 0]
#
# print("Image",imgd)
#






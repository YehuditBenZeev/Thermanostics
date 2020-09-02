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
    cv2.imshow(window_name, c)
    cv2.waitKey(0)


path = "Im1.jpg"
src = cv2.imread(path)
showPic(src)
image = src[:,:,1] # green layer
showPic(image)



#Find max hotspots by regions
def findMaxPointInArea(p1,p2,h,w,valu):
    jo=0
    io=0
    #check if point in area
    if p1 < 0 :
        return 0, 0, 0
    if p2<0:
        return 0, 0, 0
    if h >511:
        return 0, 0, 0
    if w>640:
        return 0, 0, 0
    else:
        temp = valu
        for i in range(p1, h):
            for j in range(p2, w):
                x = image[i][j]
                if x > temp:
                    temp = image[i][j]
                    io=i
                    jo=j
        return temp,io,jo

#scan all picture funk get point and define to area
def ScanImage(i,j,k,valu):
   l1=i-k
   l2=j-k
   l3=i+k
   l4=j+k
   valuePoint,io,ji= findMaxPointInArea(l1,l2,(int)(l3),(int)(l4),valu)
   if valuePoint==0 & io==0 & ji==0:
       return 0,0,0
   else:
       return valuePoint,io,ji
def passOnImage(h, w,k,temp):
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
                    t1,t2,t3=ScanImage(i,j,k,temp)# sage1: return max poin in area in size 10 of point
                    arr.append(t1)
                    arrI.append(t2)
                    arrJ.append(t3)
                flag1=False
                flag2=False
                flag3=False
                flag4=False
    #print array that hold max point from stage1
    print(arr, "arr")
    print(arrI, "arrI")
    print(arrJ, "arrJ")
    return arr ,arrJ,arrI

    #showPic(image)
    #point(arrI, arrJ)
# def point(arrI,arrJ):
#     tempI=arrI[0]
#     tempJ=arrJ[0]
#     flag=False
#     for i in range(len(arrI)):
#         print(arrI[i],"++",tempI,"++", arrJ[i],"++",tempJ)
#         if arrI[i]-tempI <15 & arrJ[i]-tempJ < 15:
#             print("good",arrI[i],tempI,arrJ[i],tempJ)
#         else:
#             print(tempI,tempJ,arrI[i],arrJ[i])
#             ti,io,jo= fin(tempI,tempJ,arrI[i],arrJ[i])
#             print(io,jo)
#             #cv2.circle(src, (io,jo), 4, (255, 128, 0), 2)
#             tempJ=arrJ[i]
#             tempI=arrI[i]
#         # if tempI > arrI[i]+15 |tempI < arrI[i]+15 | tempI > arrI[i]-15 |tempI < arrI[i]-15 |tempI==arrI[i] :
#         #     if tempJ > arrJ[i]+20 |tempJ < arrJ[i]+20 | tempJ > arrJ[i]-20 |tempJ < arrJ[i]-20|tempJ==arrJ[i]:
#         #         flag=True
#         #         print(flag)
#         #     else:
#         #          tempJ=arrJ[i]
#         # else:
#         #     tempI=arrI[i]
#         #if flag==False:
#             #fin()
#
#
#     #     if arrI[i] > 50:
#     #         cv2.circle(src, (arrJ[i],arrI[i]), 4, (255, 128, 0), 2)
#     #         print(arrI[i],arrJ[i])
#     #         break
#     showPic(image)
def findPointIncreaseArea(arr ,arrJ,arrI):
    arr1=[]
    arr2=[]
    arr3 = []
    for i in range(len(arrI)):
       w1, w2, w3 = ScanImage(arrI[i], arrJ[i], 10, arr[i])#stage2: increase area and find max point
       if w2 != 0 | w3 != 0:
           if w2 in arr2 and w3 in arr3:#not return again
               continue
           else:
               arr1.append(w1)
               arr2.append(w2)
               arr3.append(w3)
               cv2.circle(src, (w3, w2), 4, (255, 128, 0), 2)
    showPic(image)
    return arr1,arr2,arr3









#img = cv2.imread(path)
#h = img.shape[0]
#w = img.shape[1]
h, w = image.shape
arr ,arrJ,arrI=passOnImage(h,w,10,0)
arr1,arr2,arr3=findPointIncreaseArea(arr,arrJ,arrI)
print(arr1,"arr1")
print(arr2,"arr2")
print(arr3,"arr3")








import numpy as np
import cv2

def showPic(image):
    window_name = 'Image'
    cv2.imshow(window_name, image)
    cv2.waitKey(0)

def border(image):
    window_name = 'Image'
    c = cv2.Canny(image, 500, 500)
    cv2.imshow(window_name, c)
    cv2.waitKey(0)
    return c

path = "Im1.jpg"
src = cv2.imread(path)
showPic(src)
c=border(src)
image = src[:,:,1] # green layer
#showPic(image)

def findBorderPoint(h,w,c):
    list1=[]
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            if c[i][j]>20:
               # print(image[i][j])
               number_tuple = (i, j)
               list1.append(number_tuple)
               cv2.circle(src, (j, i), 4, (255, 128, 0), 2)

    showPic(image)
    print(list1)



h, w = image.shape
findBorderPoint(h,w,c)

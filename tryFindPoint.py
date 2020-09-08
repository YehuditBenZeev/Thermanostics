import numpy as np
import cv2
import cv2 as cv
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

#img = cv.imread('Im1.jpg',0)
ret,thresh = cv.threshold(c,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)
print(contours)

# cnt = contours[0]
# #print(contours[0][0][0][1],"cccccccccccc")
# i=contours[0][0][0][0]
# j=contours[0][0][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)
# showPic(image)
# M = cv.moments(cnt)
# print( M )
# area = cv.contourArea(cnt)
# print(area)
# epsilon = 0.1*cv.arcLength(cnt,True)
# approx = cv.approxPolyDP(cnt,epsilon,True)
# print(approx)
# hull = cv.convexHull(contours[0])
# print(hull)
#hull = cv.convexHull(points[, hull[, clockwise[, returnPoints]]
for i in range(0,80):
    i = contours[i][0][0][0]
    j=contours[i][0][0][1]
    cv2.circle(src, (j, i), 4, (255, 128, 0), 2)
showPic(image)


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
    return list1
def find_point1(list1):
    for i in range(list1):
        print("___ ")
h,w = image.shape
#list1=findBorderPoint(h,w,c)


# i=contours[1][0][0][0]
# j=contours[1][0][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)
# i=contours[2][0][0][0]
# j=contours[2][0][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)
# i=contours[3][0][0][0]
# j=contours[3][0][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)
# i=contours[4][0][0][0]
# j=contours[4][0][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)
# i=contours[5][0][0][0]
# j=contours[5][0][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)
# i=contours[6][0][0][0]
# j=contours[6][0][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)
# i=contours[15][0][0][0]
# j=contours[15][0][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)
# i=contours[20][0][0][0]
# j=contours[20][0][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)
# i=contours[40][0][0][0]
# j=contours[40][0][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)
# i=contours[60][0][0][0]
# j=contours[60][0][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)
# i=contours[70][0][0][0]
# j=contours[70][0][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)
# i=contours[80][0][0][0]
# j=contours[80][0][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)
# i=contours[90][0][0][0]
# j=contours[90][0][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)
# i=contours[100][0][0][0]
# j=contours[100][0][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)
# i=contours[150][0][0][0]
# j=contours[150][0][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)
# i=contours[155][0][0][0]
# j=contours[155][0][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)
# i=contours[170][0][0][0]
# j=contours[170][0][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)
# i=contours[180][0][0][0]
# j=contours[180][0][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)
# i=contours[200][0][0][0]
# j=contours[200][0][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)
# ###
# i=contours[100][2][0][0]
# j=contours[100][2][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)
# i=contours[180][3][0][0]
# j=contours[180][3][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)
# i=contours[500][0][0][0]
# j=contours[500][0][0][1]
# cv2.circle(src, (i,j), 4, (255, 128, 0), 2)


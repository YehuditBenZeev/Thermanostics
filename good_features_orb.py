import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img1 = cv.imread('506 RF.bmp')
gray1 = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
orb = cv.ORB_create()
corners = cv.goodFeaturesToTrack(gray1,1000,0.01,10)
kps1 = [cv.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in corners]
kps1, des1 = orb.compute(img1,kps1)
corners = np.int0(corners)
for i in corners:
    x,y = i.ravel()
    cv.circle(img1,(x,y),3,255,-1)
plt.imshow(img1),plt.show()



img2 = cv.imread('514 RF1.bmp')
gray2 = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
corners = cv.goodFeaturesToTrack(gray2,1000,0.01,10)
kps2 = [cv.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in corners]
kps2, des2 = orb.compute(img2,kps2)
corners = np.int0(corners)
for i in corners:
    x,y = i.ravel()
    cv.circle(img2,(x,y),3,255,-1)
plt.imshow(img2),plt.show()

# create BFMatcher object
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
# Match descriptors.
matches = bf.match(des1,des2)
# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)
# Draw first 10 matches.
#img3 = cv.drawMatches(img1,kps1,img2,kps2,matches[:10], flags=2)
#plt.imshow(img3),plt.show()

imMatches = cv.drawMatches(img1, kps1, img2, kps2, matches, None)
cv.imwrite("matches.jpg", imMatches)




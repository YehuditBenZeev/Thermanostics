import cv2
import numpy as np


def showPic(image):
    window_name = 'Image'
    cv2.imshow(window_name, image)
    cv2.waitKey(0)



path = "Im1.jpg"
src = cv2.imread(path)

image = src[:,:,1] # green layer

showPic(image)

print(image)
print(image.shape)

height, width = image.shape

for i in range(1, height-1):
    for j in range(1, width-1):
        if (image[i][j]<20) and ((image[i+1][j+1]<10) and (image[i-1][j-1]<10) ):
            image[i][j] = 0

#zeroing first & last column
image[:,:1] = 0
image[:,-1:] = 0

#zeroing first & last column
image[:1,:] = 0
image[-1:,:] = 0

print(image)
showPic(image)
print(image[200:201])


edged = cv2.Canny(image, 350, 500)

# Displaying the image
showPic(edged)
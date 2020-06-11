import cv2
import numpy as np


def show_pic(image):
    window_name = 'Image'
    cv2.imshow(window_name, image)
    cv2.waitKey(0)

class Image_Processing :

    def __init__(self, image_path):
        ########## self.image_path = image_path
        self.image = cv2.imread(image_path)


    # convert image to gray scale
    def convert_image_to_gray_scale(self):
        self.image = self.image[:,:,1] # green layer
        show_pic(self.image)
        print(self.image)
        print(self.image.shape)

        height, width = self.image.shape

        for i in range(1, height-1):
            for j in range(1, width-1):
                if (self.image[i][j]<20) and ((self.image[i+1][j+1]<10) and (self.image[i-1][j-1]<10) ):
                    self.image[i][j] = 0

        #zeroing first & last column
        self.image[:,:1] = 0
        self.image[:,-1:] = 0

        #zeroing first & last column
        self.image[:1,:] = 0
        self.image[-1:,:] = 0

        print(self.image)
        show_pic(self.image)
        print(self.image[200:201])

        return self.image

    # detects edge of palm
    def edge_detecting(self):
        edged = cv2.Canny(self.image, 350, 500)
        show_pic(edged)

# will detect hot spots
class palm:

    def __init__(self, processed_image):
        self.image = processed_image
        self.np.array #how to make it dynamic ??????
        show_pic(self.image)


class hot_spot:

    def __init__(self , value , location):
        self.value = value
        self.location = location



####################################################
### class  Image_Processing ###
a = Image_Processing('Im1.jpg')
im = a.convert_image_to_gray_scale()
a.edge_detecting()

#######################################################
### class  Hot_Spot ###
b= palm(im)


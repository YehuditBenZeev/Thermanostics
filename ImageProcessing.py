import cv2
import numpy as np
import argparse


# Displaying an image
def show_pic(image , name):
    window_name = name
    cv2.imshow(window_name, image)
    cv2.waitKey(0)

def edge_detecting(image , noise , intensity ):
   # image = cv2.imread(image_path)
    image_b_w = cv2.Canny(image, noise, intensity) # was 350 , 500 used in Palm
    return image_b_w

class ImageProcessing:
    def __init__(self, image_path):
        #########ma# self.image_path = image_path
        self.image = cv2.imread(image_path)

    def black_border(self):
        self.image = self.image[:,:,1] # green layer
       # mask = self.image
        border = cv2.bilateralFilter(self.image, 11, 17, 17)
        mask = cv2.Canny(border, 350, 500)

        rows, columns = self.image.shape
        show_pic(self.image,"edge" )

        for j in range(1, rows - 1):
           for i in range(1, columns - 1):
                if mask[j][i] != 0:
                    self.image[j][i] = 0
                    mask[j][i] = 0
                else: mask[j][i] = 255

        show_pic(mask,"edge" )
        show_pic(self.image,"edge" )
        mask = cv2.Canny(border, 350, 500)
        show_pic(mask,"edge" )

    # convert image to gray scale
    def convert_image_to_gray_scale(self):
        self.image = self.image[:,:,1] # green layer
       # show_pic(self.image, "image")
       #print(self.image)
       ##### print(self.image.shape)
        self.image = cv2.bilateralFilter(self.image, 11, 17, 17)
        show_pic(self.image, "image")

        ##  print(self.image.shape)

        height, width = self.image.shape

        for i in range(1, height-1):
            for j in range(1, width-1):
                if (self.image[i][j]<20) and ((self.image[i+1][j+1]<10) and (self.image[i-1][j-1]<10)):
                    self.image[i][j] = 0

        show_pic(self.image, "image")

       # show_pic(self.image)

        #zeroing first & last column
        self.image[:,:1] = 0
        self.image[:,-1:] = 0

        #zeroing first & last column
        self.image[:1,:] = 0
        self.image[-1:,:] = 0

       # print(self.image)
        show_pic(edge_detecting(self.image), "***")
        ####print(self.image[269:270])

        return self.image

    # Blackens the background better
    def convert_gray_scale(self):
        print("81")
        self.image = self.image[:,:,1] # green layer
        b_w_image = edge_detecting(self.image , 100, 50)
        show_pic(b_w_image ,"b_w_image")
        height, width = self.image.shape
        top_wrist = 0
        bottom_wrist =0

        for i in range(1, height - 1):
            if b_w_image[i][width -2] != 0 :
                top_wrist = i
                break
        for i in range(1, height - 1):
            if b_w_image[height - i][width - 2] != 0 :
                bottom_wrist = height - i
                break

        print("top_wrist , bottom_wrist"  , top_wrist , bottom_wrist)

        for i in range(1, height - 1):
            for j in range(1, width - 1):
                if b_w_image[i][j] == 0:
                    self.image[i][j] = 0
                else : break

        for i in range(1, height - 1):
            if ( i < top_wrist ) or ( i > bottom_wrist ):
                for j in range(1, width - 1):
                    if b_w_image[height - i][width - j] == 0:
                        self.image[height - i][width - j] = 0
                    else : break

        show_pic(self.image , "done")
'''
        b_w_image = edge_detecting(self.image , 350, 500)
        show_pic(b_w_image ,"b_w_image")

        for i in range(1, height - 1):
            for j in range(1, width - 1):
                if b_w_image[i][j] != 0:
                    self.image[i][j] = 0
                    break

        for i in range(1, height - 1):
            if ( i < top_wrist ) or ( i > bottom_wrist ):
                for j in range(1, width - 1):
                    if b_w_image[height - i][width - j] != 0:
                        self.image[height - i][width - j] = 0
                        break
                        '''




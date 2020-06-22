import cv2
import numpy as np
import argparse


# Displaying an image
def show_pic(image , name):
    window_name = name
    cv2.imshow(window_name, image)
    cv2.waitKey(0)

class Image_Processing :

    def __init__(self, image_path):
        ########## self.image_path = image_path
        self.image = cv2.imread(image_path)


    # convert image to gray scale
    def convert_image_to_gray_scale(self):
        self.image = self.image[:,:,1] # green layer
        show_pic(self.image, "image")
       #print(self.image)
       ##### print(self.image.shape)
        self.image = cv2.bilateralFilter(self.image, 11, 17, 17)
      ##  print(self.image.shape)

        height, width = self.image.shape

        for i in range(1, height-1):
            for j in range(1, width-1):
                if (self.image[i][j]<20) and ((self.image[i+1][j+1]<10) and (self.image[i-1][j-1]<10)):
                    self.image[i][j] = 0


       # show_pic(self.image)

        #zeroing first & last column
        self.image[:,:1] = 0
        self.image[:,-1:] = 0

        #zeroing first & last column
        self.image[:1,:] = 0
        self.image[-1:,:] = 0

       # print(self.image)
        #show_pic(self.image)
        ####print(self.image[269:270])

        return self.image

    # detects edge of palm
    def edge_detecting(self):
        edged = cv2.Canny(self.image, 350, 500)
        show_pic(edged,"edged")

# will detect hot spots
class palm:

    def __init__(self, processed_image):
        self.image = processed_image
      #  self.np.array #how to make it dynamic ??????
        self.finger1 = finger()
        self.finger2 = finger()
        self.finger3 = finger()
        self.finger4 = finger()
        self.finger5 = finger()

        show_pic(self.image,"image")

    def find_max_for_palm(self): ##################

        show_pic(self.image, "image")

        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(self.image)
        print (minVal, maxVal, minLoc, maxLoc)
      #  ss = self.image[maxLoc[0] -50:maxLoc[0]+50,maxLoc[1]-50:maxLoc[1]+50]
       # print("72")
        #show_pic(ss)
        cv2.circle(self.image, maxLoc, 20, (255, 0, 0), 2)
        show_pic(self.image,"max circle")

    #def detect_hot_spot(self):
    def central_of_palm(self):
        height, width = self.image.shape

        for i in range(0, height):
            for j in range(0, width):
                if (self.image[i][j]<20) and ((self.image[i+1][j+1]<10) and (self.image[i-1][j-1]<10)):
                    self.image[i][j] = 0

        print("o")

    def detect_fingers(self):

        #critical_piont = np.array()
        rows, columns = self.image.shape
        count = 0
        first = 0
        temp = np.array([0,0])
        print(rows, columns)

        show_pic(self.image, "image")

        for j in range(0, rows-1):
            for i in range(0, columns-1):
                if self.image[j][i]==0 and self.image[j+1][i+1]!=0 :
                    self.image[j][i]=255
                    if first == 0:
                        first = 1
                        self.finger1.top_1[0] = j
                        self.finger1.top_1[0] = i
                        while i<55:
                            i -= 1
                            j += 1
                    if j > temp[0] and i > temp[1]:
                        temp[0] = j
                        temp[1] = i
                   # cv2.circle(self.image, (i,j), 1, (255, 0, 0), 1)
                if self.image[rows-1-j][columns-1-i] == 0 and self.image[rows-2-j - 1][columns-2-i] != 0:
                    self.image[rows-1-j][columns-1-i] = 255
                    #cv2.circle(self.image, (columns-1-i, rows-1-j), 1, (255, 0, 0), 1)

        show_pic(self.image, "image")
        #print(self.image[263-7:263+7,104-7:104+7])

                    #if temp[0]>
                       # temp = [i,j]

                #critical_piont[count] =[i,j]
              #  count +=1
        '''for j in range(rows-1, 1, -1):
            for i in range(columns-1, 1,-1):
                if self.image[j][i] == 0 and self.image[j - 1][i - 1] != 0:
                    cv2.circle(self.image, (i, j), 2, (255, 0, 0), 1)'''

        show_pic(self.image, "image")


        return

class finger:
    def __init__(self):
        self.top_1 = np.array([0,0])
        self.top_2 =  np.array([0,0])
        self.bottom_1 =  np.array([0,0])
        self.bottom_2 =  np.array([0,0])

class hot_spot:

    def __init__(self , value , location):
        self.max_value = value
        self.location = location




####################################################
### class  Image_Processing ###
a = Image_Processing('Im1.jpg')
im = a.convert_image_to_gray_scale()
#a.edge_detecting()

#######################################################
### class  Hot_Spot ###

b= palm(im)
#b.find_max_for_palm()
b.detect_fingers()
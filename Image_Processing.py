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
       # show_pic(self.image, "image")
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
        #show_pic(edged,"edged")

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

      # show_pic(self.image,"image")

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


    def draw_on_point(self):
        cv2.circle(self.image, (self.finger1.top_1[1], self.finger1.top_1[0]), 4, (255, 0, 0), 2)
        cv2.circle(self.image, (self.finger1.top_2[1], self.finger1.top_2[0]), 4, (255, 0, 0), 2)
        cv2.circle(self.image, (self.finger1.bottom_2[1], self.finger1.bottom_2[0]), 4, (255, 0, 0), 2)
        show_pic(self.image, "finger1")

        cv2.circle(self.image, (self.finger2.top_1[1], self.finger2.top_1[0]), 4, (255, 0, 0), 2)
        cv2.circle(self.image, (self.finger2.top_2[1], self.finger2.top_2[0]), 4, (255, 0, 0), 2)
        cv2.circle(self.image, (self.finger2.bottom_2[1], self.finger2.bottom_2[0]), 4, (255, 0, 0), 2)
        show_pic(self.image, "finger2")

        cv2.circle(self.image, (self.finger3.top_1[1], self.finger3.top_1[0]), 4, (255, 0, 0), 2)
        cv2.circle(self.image, (self.finger3.top_2[1], self.finger3.top_2[0]), 4, (255, 0, 0), 2)
        cv2.circle(self.image, (self.finger3.bottom_2[1], self.finger3.bottom_2[0]), 4, (255, 0, 0), 2)
        show_pic(self.image, "finger3")

        cv2.circle(self.image, (self.finger4.top_1[1], self.finger4.top_1[0]), 4, (255, 0, 0), 2)
        cv2.circle(self.image, (self.finger4.top_2[1], self.finger4.top_2[0]), 4, (255, 0, 0), 2)
        cv2.circle(self.image, (self.finger4.bottom_2[1], self.finger4.bottom_2[0]), 4, (255, 0, 0), 2)
        show_pic(self.image, "finger4")

        cv2.circle(self.image, (self.finger5.top_1[1], self.finger5.top_1[0]), 4, (255, 0, 0), 2)
        cv2.circle(self.image, (self.finger5.top_2[1], self.finger5.top_2[0]), 4, (255, 0, 0), 2)
        cv2.circle(self.image, (self.finger5.bottom_2[1], self.finger5.bottom_2[0]), 4, (255, 0, 0), 2)


    #detects
    def detect_tow_points(self, j , i , current_finger):
        print("i , j , current_finger" , i ,j , current_finger.top_1[0] , current_finger.top_1[1])

        rows, columns = self.image.shape
        find = 0
        temp = np.array([current_finger.top_1[0],current_finger.top_1[1]]) # holds: row , column / [y,x] / [j,i] / [k,l]
        print(temp)
        for k in range(j, rows - 1):
            if find == 2:  # found both the points
                find = 0
                break
            if find == 0:  # looking for first terning point
                for l in range(0, i):
                    if self.image[k][l] == 0 and self.image[k][l + 1] != 0:

                        if k > temp[0] and l < temp[1] :  # if lower row and a lower column
                            temp[0] = k
                            temp[1] = l
                        if k > temp[0] and l >temp[1] :  # if lower row and a higher column - pasted the terning point
                            current_finger.top_2[0] = temp[0]
                            current_finger.top_2[1] = temp[1]
                            find = 1
                            break
            elif find == 1 :#and k > current_finger.top_2[0] + 100:  # looking for bottom second point
                temp[0] = k
                temp[1] = l
                for l in range(self.finger1.top_2[1], columns - 1):
                    if self.image[k][l] == 0 and self.image[k][l + 1] != 0:
                        if  temp[1] > l:  # if lower row and a lower column
                            temp[0] = k
                            temp[1] = l
                        if temp[1] < l:  # if lower row and a higher column - pasted the terning point
                            current_finger.bottom_2[0] = temp[0]
                            current_finger.bottom_2[1] = temp[1]
                            find = 2
                            break
        print("139" , current_finger.top_1[0] , current_finger.top_1[1] ,current_finger.top_2[0], current_finger.top_2[1], current_finger.bottom_2[0], current_finger.bottom_2[1])

    def detect_fingers(self):

        #critical_piont = np.array()
        rows, columns = self.image.shape
        count = 1
        first = 0
        temp = np.array([0,0]) # holds: row , column
        print(rows, columns)

        show_pic(self.image, "image")

        for j in range(0, rows-1):
            for i in range(0, columns-1):
                if self.image[j][i]==0 and self.image[j][i+1]!=0 :
                    #self.image[j][i]=255
                    if count == 1: # detect first finger
                        count = 2

                        self.finger1.top_1[0] = j
                        self.finger1.top_1[1] = i
                        print ("i , j",i ,j ,self.finger1.top_1[1], self.finger1.top_1[0])

                        self.detect_tow_points(j, i, self.finger1)

                        print("178", self.finger1.bottom_2 , self.image[self.finger1.bottom_2[0]][self.finger1.bottom_2[1]+1])

                        '''for k in range(j, rows-1):
                            if find == 2 : # found the point
                                find = 0
                                break
                           # if find == 0:
                            if find == 0:  # looking for first terning point
                                for l in range(0 , i):
                                    if self.image[k][l]==0 and self.image[k+1][l+1]!=0:
                                        if  temp[0] > k and temp[1] < l : # if lower row and a lower column
                                            temp[0] = k
                                            temp[1] = l
                                        if  temp[0] > k and temp[1] > l : # if lower row and a higher column - pasted the terning point
                                            self.finger1.top_2[0] = j
                                            self.finger1.top_2[1] = i
                                            find = 1
                            if find == 1: # looking for bottom second point
                                temp[0] = k
                                temp[1] = l
                                for l in range(self.finger1.top_2[1], columns-1):
                                    if self.image[k][l]==0 and self.image[k+1][l+1]!=0:
                                        if  temp[0] > k and temp[1] > l : # if lower row and a lower column
                                            temp[0] = k
                                            temp[1] = l
                                        if  temp[0] > k and temp[1] < l : # if lower row and a higher column - pasted the terning point
                                            self.finger1.top_2[0] = j
                                            self.finger1.top_2[1] = i
                                            find = 2
                                            break


                                    cv2.circle(self.image, (l, k), 2, (255, 0, 0), 1)'''
                                    #show_pic(self.image, "image")
        if count != 0:
            print(self.finger1.top_2[1])
            for j in range(0, rows - 1):
                if count > 5:
                    break
                for i in range(0,self.finger1.top_2[1] ):
                    if self.image[j][i] == 0 and self.image[j][i + 1] != 0:
                        print ("i , j",i ,j )
                        if count == 2:  # detect second finger
                            print(count)
                            count = 3
                            self.finger2.top_1[0] = j
                            self.finger2.top_1[1] = i
                            self.detect_tow_points( j, i, self.finger2)
                        elif count == 3:  # detect third finger
                            print(count)
                            count = 4
                            self.finger3.top_1[0] = j
                            self.finger3.top_1[1] = i
                            self.detect_tow_points( j, i, self.finger3)
                        elif count == 4:  # detect fourth finger
                            print(count)
                            count = 5
                            self.finger4.top_1[0] = j
                            self.finger4.top_1[1] = i
                            self.detect_tow_points( j, i, self.finger4)
                        elif count == 5:  # detect fifth finger
                            print(count)
                            count = 6
                            self.finger5.top_1[0] = j
                            self.finger5.top_1[1] = i
                            self.detect_tow_points(j, i, self.finger5)
                        else:
                            print(count)
                            break

        '''for j in range(rows-1, 1, -1):
            for i in range(columns-1, 1,-1):
                if self.image[j][i] == 0 and self.image[j - 1][i - 1] != 0:
                    cv2.circle(self.image, (i, j), 2, (255, 0, 0), 1)'''
        self.draw_on_point()
        show_pic(self.image, "image")

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
a.edge_detecting()

#######################################################
### class  Hot_Spot ###

b= palm(im)
#b.find_max_for_palm()
b.detect_fingers()
import cv2
import numpy as np
import argparse
import Finger as f
import Image_Processing as ip

# will detect hot spots
class Palm:

    def __init__(self, processed_image, path):
        self.image = processed_image
        self.black_white_image = ip.edge_detecting(path)
        self.finger_width = 0
      #  self.np.array #how to make it dynamic ??????
        self.finger1 = f.Finger()
        self.finger2 = f.Finger()
        self.finger3 = f.Finger()
        self.finger4 = f.Finger()
        self.finger5 = f.Finger()

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
        print("127 ", self.finger1.bottom_2[1], self.finger1.bottom_2[0])

        ip.show_pic(self.image, "finger1")

        cv2.circle(self.image, (self.finger2.top_1[1], self.finger2.top_1[0]), 4, (255, 0, 0), 2)
        cv2.circle(self.image, (self.finger2.top_2[1], self.finger2.top_2[0]), 4, (255, 0, 0), 2)
        cv2.circle(self.image, (self.finger2.bottom_2[1], self.finger2.bottom_2[0]), 4, (255, 0, 0), 2)
        ip.show_pic(self.image, "finger2")

        cv2.circle(self.image, (self.finger3.top_1[1], self.finger3.top_1[0]), 4, (255, 0, 0), 2)
        cv2.circle(self.image, (self.finger3.top_2[1], self.finger3.top_2[0]), 4, (255, 0, 0), 2)
        cv2.circle(self.image, (self.finger3.bottom_2[1], self.finger3.bottom_2[0]), 4, (255, 0, 0), 2)
        ip.show_pic(self.image, "finger3")

        cv2.circle(self.image, (self.finger4.top_1[1], self.finger4.top_1[0]), 4, (255, 0, 0), 2)
        cv2.circle(self.image, (self.finger4.top_2[1], self.finger4.top_2[0]), 4, (255, 0, 0), 2)
        cv2.circle(self.image, (self.finger4.bottom_2[1], self.finger4.bottom_2[0]), 4, (255, 0, 0), 2)
        ip.show_pic(self.image, "finger4")

        cv2.circle(self.image, (self.finger5.top_1[1], self.finger5.top_1[0]), 4, (255, 0, 0), 2)
        cv2.circle(self.image, (self.finger5.top_2[1], self.finger5.top_2[0]), 4, (255, 0, 0), 2)
        cv2.circle(self.image, (self.finger5.bottom_2[1], self.finger5.bottom_2[0]), 4, (255, 0, 0), 2)

    def inclination_between_two_points(self, temp , k ,l):
        y = temp[0] - k
        x = temp[1] - l
        if y == 0 or x == 0:
            return 0
        inclination= y/x
        return inclination

    def detect_tow_points(self, j , i , current_finger):
        print("i , j , current_finger" , i ,j , current_finger.top_1[0] , current_finger.top_1[1])

        rows, columns = self.image.shape
        found = 0
        temp = np.array([current_finger.top_1[0],current_finger.top_1[1]]) # holds: row , column / [y,x] / [j,i] / [k,l]
        for k in range(j, rows - 1):
            if found == 2:  # found both the points
                found = 0
                break
            if found == 0:  # looking for first terning point
                for l in range(0, i):
                    if self.image[k][l] == 0 and self.image[k][l + 1] != 0:

                        if k > temp[0] and l < temp[1] :  # if lower row and a lower column
                            temp[0] = k
                            temp[1] = l
                        if k > temp[0] and l >temp[1] :  # if lower row and a higher column - pasted the terning point
                            current_finger.top_2[0] = temp[0]
                            current_finger.top_2[1] = temp[1]
                            found = 1

            elif found == 1 and k > current_finger.top_2[0] + 102:  # looking for bottom second point

                for l in range(self.finger1.top_2[1], columns - 1):
                    if self.black_white_image[k][l] == 0 and self.black_white_image[k][l + 1] != 0:
                        # print("149 , k , l ,", k , l ,self.black_white_image[k][l] ,self.black_white_image[k][l + 1])
                        #if  temp[1] > l:  # if lower row and a lower column

                        if self.inclination_between_two_points(temp , k , l) < 0:  # if lower row and a higher column - pasted the terning point
                            print("186 , k , l ,", k, l, self.black_white_image[k][l], self.black_white_image[k][l + 1])
                            current_finger.bottom_2[0] = k
                            current_finger.bottom_2[1] = l
                            print("191 , k , l ,", k, l, temp[0], temp[1])
                            found = 2
                            break
                        else :
                            print("197" , k,l)
                            temp[0] = k
                            temp[1] = l
                            continue

        print("202" , current_finger.top_1[0] , current_finger.top_1[1] ,current_finger.top_2[0], current_finger.top_2[1], current_finger.bottom_2[0], current_finger.bottom_2[1])

    def detect_bottom2_point(self , i , j , current_finger):
        rows, columns = self.image.shape
        found = 0
        temp = np.array([current_finger.top_1[0],current_finger.top_1[1]]) # holds: row , column / [y,x] / [j,i] / [k,l]

        for k in range(j, rows - 1):
            if found == 1 :
                break
            for l in range(i, columns - 1):
                if self.black_white_image[k][l] == 0 and self.black_white_image[k][l + 1] != 0:
                    inclination = self.inclination_between_two_points(temp, k, l)

                    if inclination < -0.7:  # if lower row and a higher column - pasted the terning point
                        print(" ********* " , )
                        current_finger.bottom_2[0] = k
                        current_finger.bottom_2[1] = l
                        found = 1
                        break
                    else:
                        temp[0] = k
                        temp[1] = l
                        continue

    def detect_bottom2_finger5(self):
        print("146")


    def detect_second_finger(self , i , j ):
        rows, columns = self.image.shape
        found = 0
        for l in range(i, columns - 1):
            if found == 1 :
                break
            for k in range(0 , j):
                if self.black_white_image[k][l] == 0 and self.black_white_image[k][l + 1] != 0:
                    self.finger2.top_1[0] = k
                    self.finger2.top_1[1] = l
                    found = 1
                    break
        #self.finger2.bottom_2[0] = self.finger2.top_1[0] + int(self.finger_width/2)
       # self.finger2.bottom_2[1] = self.finger2.top_1[1]
        self.detect_bottom2_point(self.finger2.top_1[1] , self.finger2.top_1[0] + int(self.finger_width/2) , self.finger2)

    def detect_fourth_finger(self , i , j):
        rows, columns = self.image.shape
        found = 0
        for l in range(i, columns - 1):
            if found == 1 :
                break
            for k in range(j , rows -1):
                if self.black_white_image[k][l] == 0 and self.black_white_image[k][l + 1] != 0:
                    self.finger4.top_1[0] = k
                    self.finger4.top_1[1] = l
                    found = 1
                    break
        self.finger4.top_2[0] = self.finger4.top_1[0]
        self.finger4.top_2[1] = self.finger4.top_1[1]
     #   self.detect_bottom2_point(self.finger4.top_1[1] , self.finger4.top_1[0] + int(self.finger_width /2), self.finger4)

    def detect_fifth_finger(self , i , j):
        rows, columns = self.image.shape
        found = 0
        for l in range(i, columns - 1):
            if found == 1:
                break
            for k in range(j, rows - 1):
                if self.black_white_image[k][l] == 0 and self.black_white_image[k][l + 1] != 0:
                    self.finger5.top_1[0] = k
                    self.finger5.top_1[1] = l
                    found = 1
                    break


        self.detect_bottom2_finger5()

    # finds the distance between two points
    def distance(self, point1 , point2):
        x = point1[1] - point2[1]
        y = point1[0] - point2[0]

        distance = (x**2 + y**2)**0.5
        return  distance

    def detect_fingers(self):
        #critical_piont = np.array()
        rows, columns = self.image.shape
        count = 1
        first = 0
        temp = np.array([0,0]) # holds: row , column
        ip.show_pic(self.black_white_image, "image")

        for j in range(0, rows-1):
            for i in range(0, columns-1):
                if self.black_white_image[j][i]==0 and self.black_white_image[j][i+1]!=0 :
                    #self.image[j][i]=255
                    if count == 1: # detected first finger
                        count = 2

                        self.finger1.top_1[0] = j
                        self.finger1.top_1[1] = i

                        self.detect_tow_points(j, i, self.finger1)

                        self.finger_width = int(self.distance(self.finger1.top_1 , self.finger1.top_2))
                        print("self.finger_width = ", self.finger_width)
                        print("178", self.finger1.bottom_2 , self.black_white_image[self.finger1.bottom_2[0]][self.finger1.bottom_2[1]+1])

        for i in range(0, columns - 1):
            if count == 3:
                break
            for j in range(0, rows-1):
                if self.black_white_image[j][i] == 0 and self.black_white_image[j][i + 1] != 0:
                    if count == 2:  # detect third finger
                        count = 3

                        self.finger3.top_1[0] = j
                        self.finger3.top_1[1] = i
                        print("j = " ,j , " finger = ", self.finger3.top_1[0] )
                       # self.detect_bottom2_point(self.finger3.top_1[1], self.finger3.top_1[0] + int(self.finger_width/2) ,self.finger2)

                        self.detect_second_finger(int(i - self.finger_width) , int(j - self.finger_width))
                        self.detect_fourth_finger(int(i + self.finger_width) , int(j + self.finger_width))
                        self.detect_fifth_finger(int(self.finger4.top_2[1] + self.finger_width) , int(self.finger4.top_2[0] + self.finger_width)  )
                        break

        self.finger3.bottom_1[0] = self.finger2.bottom_2[0]
        self.finger3.bottom_1[1] = self.finger2.bottom_2[1]
        self.finger4.bottom_1[0] = self.finger3.bottom_2[0]
        self.finger4.bottom_1[1] = self.finger3.bottom_2[1]
        self.finger5.bottom_1[0] = self.finger4.bottom_2[0]
        self.finger5.bottom_1[1] = self.finger4.bottom_2[1]

        self.draw_on_point()
        ip.show_pic(self.image, "image")

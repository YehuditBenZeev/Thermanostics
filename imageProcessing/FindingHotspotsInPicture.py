import numpy as np
import cv2
import csv
from Thermanostics.imageProcessing import ConvertGrayScale as Ip

class FindingHotspotsInPicture:
    def __init__(self, processed_image):
        self.image = processed_image
        self.number_tuple = (0, 0)
        self.pointList = []
        self.h, self.w = self.image.shape
        self.img = np.array(self.image)

    def find_max_point_in_area(self, p1, p2, p3, p4, value):
        jo = 0
        io = 0
        # check if point in area
        if p1 < 0:
            return 0, 0, 0
        if p2 < 0:
            return 0, 0, 0
        if p3 > 511:
            return 0, 0, 0
        if p4 > 640:
            return 0, 0, 0
        else:
            temp = value
            for i in range(p1, p3):
                for j in range(p2, p4):
                    x = self.image[i][j]
                    if x > temp:
                        temp = self.image[i][j]
                        io = i
                        jo = j
            return temp, io, jo
    # #scan all picture funk get point and define to area
    def scan_image(self, i, j, k, value):
        l1 = i - k
        l2 = j - k
        l3 = i + k
        l4 = j + k
        valuePoint, io, ji = self.find_max_point_in_area(l1, l2, int(l3), int(l4), value)

        if(valuePoint == 0) & (io == 0) & (ji == 0):
            return 0, 0, 0
        else:
            return valuePoint, io, ji
    def pass_on_image(self, size):
        flag1 = False
        flag2 = False
        flag3 = False
        flag4 = False
        for i in range(1, self.h - 1):
            for j in range(1, self.w - 1):
                if i-1 > 0:
                    if self.image[i-1][j] < self.image[i][j]:
                        flag1 = True
                if j-1 > 0:
                    if self.image[i][j-1] < self.image[i][j]:
                        flag2 = True

                if i+1 < self.h:
                    if self.image[i+1][j] < self.image[i][j]:
                        flag3 = True
                if j+1 < self.w:
                    if self.image[i][j+1] < self.image[i][j]:
                        flag4 = True
                if flag1 & flag2 & flag3 & flag4:
                    if self.image[i][j] > 170:
                        t1, t2, t3 = self.scan_image(i, j, size, 0)  # sage1: return max poin in area in size 10 of point
                        self.number_tuple = (t3, t2)
                        self.pointList.append(self.number_tuple)
                    flag1 = False
                    flag2 = False
                    flag3 = False
                    flag4 = False
        self.pointList = list(dict.fromkeys(self.pointList))
        for i in self.pointList:
            cv2.circle(self.img, i, 4, (0, 0,250), 2)
        Ip.show_pic(self.img, "p")
# ____________________________________________________________________________________________
    def write_in_file(self):
        # field names
        fields = ['X', 'Y']
        # data rows of csv file
        rows = []
        for point in self.pointList:
             row = [point[0], point[1]]
             rows.append(row)
        filename = "algoritm_point.csv"

        # writing to csv file
        with open(filename, 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)

            # writing the fields
            csvwriter.writerow(fields)

            # writing the data rows
            csvwriter.writerows(rows)
        return filename
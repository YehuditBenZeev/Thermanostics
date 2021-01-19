import math

import cv2
import numpy as np
import pandas as pd
import csv


def show_pic(image, name):
    window_name = name
    cv2.imshow(window_name, image)
    cv2.waitKey(0)


def distance_to_line(point, p1, p2):
    x_diff = p2[0] - p1[0]
    y_diff = p2[1] - p1[1]
    num = abs(y_diff * point[0] - x_diff * point[1] + p2[0] * p1[1] - p2[1] * p1[0])
    den = math.sqrt(y_diff ** 2 + x_diff ** 2)
    return num / den


def midpoint(p1, p2):
    return int((p1[0] + p2[0]) / 2), int((p1[1] + p2[1]) / 2)


class ObjectTest:
    def __init__(self, image, point1, point2, point3, point4, point5, point6, point7, point8, point9):
        self.image = cv2.imread(image)
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4
        self.point5 = point5
        self.point6 = point6
        self.point7 = point7
        self.point8 = point8
        self.point9 = point9
        self.mid_root = midpoint(self.point1, self.point2)

    def trapeze(self):
        pts = np.array(
            [self.point1, self.point2, self.point3, self.point4, self.point5, self.point6, self.point7, self.point8,
             self.point9], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(self.image, [pts], True, (255, 0, 0))
        show_pic(self.image, "p")

    def div_coordinates(self):
        # Draw a diagonal blue line with thickness of 5 px
        cv2.arrowedLine(self.image, self.point1, self.point2, (41, 185, 64), 2)
        cv2.arrowedLine(self.image, self.mid_root, self.point7, (41, 185, 64), 2)
        show_pic(self.image, "p")

    # Finding the position of a point for the new coordinates
    def find_new_location(self, point):
        cv2.circle(self.image, point, 4, (255, 56, 0), 2)
        distance_x = round(distance_to_line(point, self.point7, self.mid_root), 2)
        distance_y = round(distance_to_line(point, self.point1, self.point2), 2)
        show_pic(self.image, "p")
        return distance_x, distance_y


if __name__ == "__main__":
    with open("plam.csv", 'r') as f:
        for row in csv.DictReader(f):
            a = ObjectTest(row['numberPlam'], (int(row['X1']), int(row['Y1'])), (int(row['X2']), int(row['Y2'])),
                           (int(row['X3']), int(row['Y3'])),
                           (int(row['X4']), int(row['Y4'])), (int(row['X5']), int(row['Y5'])),
                           (int(row['X6']), int(row['Y6'])),
                           (int(row['X7']), int(row['Y7'])), (int(row['X8']), int(row['Y8'])),
                           (int(row['X9']), int(row['Y9'])))
            a.trapeze()
            a.div_coordinates()
            # Go through all the points of the palm in area 0
            print(a.find_new_location((301, 200)))
            print(a.find_new_location((319, 129)))

    # open the point table from imageJ
    # reader=csv.DictReader(open("Results.csv"))
    # print(row0)

    # Sent to a function that returns our endpoints

#  a = ObjectTest("514 RF.bmp",(214,230),(464,214),(454,144),(471,275))
#  """For the palm we will draw a trapezoid"""
#  a.trapeze((227,134),(261,308),(471,275),(454,144))
#  """For the palm we will draw a axial system"""
#  a.div_coordinates((214,230),(471,275),(464,214),(454,144))
# #a.find_new_location((301, 200))
#  """For each hotspot we will check its relative distance from the system of axes"""
#  with open("Results.csv",'r') as f:
#      for row in csv.DictReader(f):
#          if row['Area']=='0':
#              distance_x, distance_y = a.find_new_location((459, 186)) #try
#              row["localX"] = distance_x
#              row['localY']=distance_y
#              print(row)
#              #
#              # distance_x=0
#              # row['localX']=distance_x

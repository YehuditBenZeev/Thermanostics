import math

import cv2
import numpy as np
import pandas as pd



def show_pic(image, name):
    window_name = name
    cv2.imshow(window_name, image)
    cv2.waitKey(0)

def convert_exel_csv(exelFile):
    read_file = pd.read_excel(exelFile)
    read_file.to_csv("Point.csv", index=None,header=True)
    df = pd.DataFrame(pd.read_csv("Point.csv"))
    print(df)


def distance_to_line(point, p1, p2):
    x_diff = p2[0] - p1[0]
    y_diff = p2[1] - p1[1]
    num = abs(y_diff * point[0] - x_diff * point[1] + p2[0] * p1[1] - p2[1] * p1[0])
    den = math.sqrt(y_diff ** 2 + x_diff ** 2)
    return num / den

class ObjectTest:
    def __init__(self,image,point1,point2,point3,point4):
        self.image = cv2.imread(image)
        self.mid_finger_point_x=point1
        self.mid_root_point_x=point2
        self.R_root_point_y=point3
        self.L_root_point_y = point4


    def trapeze(self,point_1,point_2,point_3,point_4):
        pts = np.array([point_1,point_2,point_3,point_4], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(self.image, [pts], True, (255, 0, 0))
        show_pic(self.image, "p")
    def div_coordinates(self,finger_point,root_point1,root_point2,root_point3):
        # Draw a diagonal blue line with thickness of 5 px
        cv2.arrowedLine(self.image,root_point2,finger_point, (41, 185, 64), 2)
        cv2.arrowedLine(self.image,root_point1, root_point3, (41, 185, 64), 2)
        show_pic(self.image, "p")

    def straight_slope(self):
        return self.mid_finger_point_x[1]-self.mid_root_point_x[1]/self.mid_finger_point_x[0]-self.mid_root_point_x[0]


    #Finding the position of a point for the new coordinates
    def find_new_location(self,point):
        cv2.circle(self.image,point,4, (255, 56, 0), 2)
        distance_x=round(distance_to_line(point,self.mid_finger_point_x,self.mid_root_point_x), 2)
        distance_y=round(distance_to_line(point,self.L_root_point_y,self.R_root_point_y), 2)
        show_pic(self.image, "p")
        return distance_x ,distance_y








if __name__ == "__main__":
    a = ObjectTest("514 RF.bmp",(214,230),(464,214),(454,144),(471,275))
    a.trapeze((227,134),(261,308),(471,275),(454,144))
    a.div_coordinates((214,230),(471,275),(464,214),(454,144))
    a.find_new_location((301,200))


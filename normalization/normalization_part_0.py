import math
import cv2
import numpy as np
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

    def div_coordinates(self):
        # Draw a diagonal blue line with thickness of 5 px
        cv2.arrowedLine(self.image, self.point1, self.point2, (41, 185, 64), 2)
        cv2.arrowedLine(self.image, self.mid_root, self.point7, (41, 185, 64), 2)

    # Finding the position of a point for the new coordinates
    def find_new_location(self, point):
        cv2.circle(self.image, point, 4, (255, 56, 0), 2)
        distance_x = round(distance_to_line(point, self.point7, self.mid_root), 2)
        distance_y = round(distance_to_line(point, self.point1, self.point2), 2)
        return distance_x, distance_y


if __name__ == "__main__":
    with open("palm.csv", 'r') as f:
        for row in csv.DictReader(f):
            a = ObjectTest(row['numberPalm'], (int(row['X1']), int(row['Y1'])), (int(row['X2']), int(row['Y2'])),
                           (int(row['X3']), int(row['Y3'])),
                           (int(row['X4']), int(row['Y4'])), (int(row['X5']), int(row['Y5'])),
                           (int(row['X6']), int(row['Y6'])),
                           (int(row['X7']), int(row['Y7'])), (int(row['X8']), int(row['Y8'])),
                           (int(row['X9']), int(row['Y9'])))
            a.trapeze()
            a.div_coordinates()

            # iterate on all hat spots and call find_new_location read points from file (no file right now - yous mock data)

            # Go through all the points of the palm in area 0
            print(a.find_new_location((301, 200)))
            print(a.find_new_location((319, 129)))

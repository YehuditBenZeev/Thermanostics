import cv2
from image_processing import convert_gray_scale as Ip, palm as P
import numpy as np


class DivisionPalmArea:

    def __init__(self, processed_image, path):
        self.palmIn = P.Palm(processed_image, path)
        self.palmIn.detect_fingers()
        self.TopLeFt = 0
        self.TopRight = 0
        self.bottomLeft = 0
        self.bottomRight = 0
        self.img = np.array(self.palmIn.image)

    def find_area_0(self):
        self.TopLeFt = self.palmIn.finger1.bottom_2
        self.TopRight = self.palmIn.finger5.bottom_2
        self.bottomLeft = self.palmIn.palm_base_top
        self.bottomRight = self.palmIn.palm_base_bottom
        pts = np.array([self.TopLeFt, self.TopRight, self.bottomRight, self.bottomLeft], np.int32)  # add point according to tramonstics request
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(self.img, [pts], True, (255, 0, 0))

    def find_finger_1(self):
        self.TopLeFt = self.palmIn.finger1.top_1
        self.TopRight = self.palmIn.finger1.top_2
        self.bottomLeft = self.palmIn.finger1.bottom_1
        self.bottomRight = self.palmIn.finger1.bottom_2
        pts = np.array([self.TopLeFt, self.TopRight, self.bottomRight, self.bottomLeft], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(self.img, [pts], True, (255, 0, 0))

    def find_finger_2(self):
        self.TopLeFt = self.palmIn.finger2.top_1
        self.TopRight = self.palmIn.finger2.top_2
        self.bottomLeft = self.palmIn.finger2.bottom_1
        self.bottomRight = self.palmIn.finger2.bottom_2
        pts = np.array([self.TopLeFt, self.TopRight, self.bottomLeft, self.bottomRight], np.int32)
        pts = pts.reshape((-1, 1, 2))

    def find_finger_3(self):
        self.TopLeFt = self.palmIn.finger3.top_1
        self.TopRight = self.palmIn.finger3.top_2
        self.bottomLeft = self.palmIn.finger3.bottom_1
        self.bottomRight = self.palmIn.finger4.bottom_1

        pts = np.array([self.TopLeFt,self.TopRight, self.bottomRight, self.bottomLeft], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(self.img, [pts], True, (255, 0, 0))

    def find_finger_4(self):
        self.TopLeFt = self.palmIn.finger4.top_1
        self.TopRight = self.palmIn.finger4.top_2
        self.bottomLeft = self.palmIn.finger4.bottom_1
        self.bottomRight = self.palmIn.finger4.bottom_2
        pts = np.array([self.TopLeFt,self.TopRight, self.bottomRight, self.bottomLeft], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(self.img, [pts], True, (255, 0, 0))

    def find_finger_5(self):
        self.TopLeFt = self.palmIn.finger5.top_1
        self.TopRight = self.palmIn.finger5.top_2
        self.bottomLeft = self.palmIn.finger5.bottom_1
        self.bottomRight = self.palmIn.finger5.bottom_2
        pts = np.array([self.TopLeFt,self.TopRight, self.bottomRight, self.bottomLeft], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(self.img, [pts], True, (255, 0, 0))

        # show results
        # Ip.show_pic(self.img, "find_finger")


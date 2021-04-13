import cv2
from image_processing import convert_gray_scale as Ip, palm as P
import numpy as np
from shapely.geometry.polygon import Polygon


class DivisionPalmArea:

    def __init__(self, processed_image, path):
        self.palmIn = P.Palm(processed_image, path)
        self.palmIn.detect_fingers()
        self.polygon_array = []
        self.img = np.array(self.palmIn.image)
        self.find_areas()

    def find_areas(self):
        self.find_area_0(self)
        self.find_area_1(self)
        self.find_area_2(self)
        self.find_area_3(self)
        self.find_area_4(self)
        self.find_area_5(self)

    def find_area_0(self):
        TopLeFt = self.palmIn.finger1.bottom_2
        TopRight = self.palmIn.finger5.bottom_2
        bottomLeft = self.palmIn.palm_base_top
        bottomRight = self.palmIn.palm_base_bottom
        polygon = Polygon([TopLeFt, TopRight, bottomLeft, bottomRight])
        self.polygon_array.insert(0, polygon)

        # pts = np.array([self.TopLeFt, self.TopRight, self.bottomRight, self.bottomLeft], np.int32)  # add point according to tramonstics request
        # pts = pts.reshape((-1, 1, 2))
        # cv2.polylines(self.img, [pts], True, (255, 0, 0))

    def find_area_1(self):
        TopLeFt = self.palmIn.finger1.top_1
        TopRight = self.palmIn.finger1.top_2
        bottomLeft = self.palmIn.finger1.bottom_1
        bottomRight = self.palmIn.finger1.bottom_2
        polygon = Polygon([TopLeFt, TopRight, bottomLeft, bottomRight])
        self.polygon_array.insert(1, polygon)

        # pts = np.array([TopLeFt, TopRight, bottomRight, bottomLeft], np.int32)
        # pts = pts.reshape((-1, 1, 2))
        # cv2.polylines(self.img, [pts], True, (255, 0, 0))

    def find_area_2(self):
        TopLeFt = self.palmIn.finger2.top_1
        TopRight = self.palmIn.finger2.top_2
        bottomLeft = self.palmIn.finger2.bottom_1
        bottomRight = self.palmIn.finger2.bottom_2
        polygon = Polygon([TopLeFt, TopRight, bottomLeft, bottomRight])
        self.polygon_array.insert(2, polygon)

        # pts = np.array([TopLeFt, TopRight, bottomLeft, bottomRight], np.int32)
        # pts = pts.reshape((-1, 1, 2))
        # cv2.polylines(self.img, [pts], True, (255, 0, 0))

    def find_area_3(self):
        TopLeFt = self.palmIn.finger3.top_1
        TopRight = self.palmIn.finger3.top_2
        bottomLeft = self.palmIn.finger3.bottom_1
        bottomRight = self.palmIn.finger4.bottom_1
        polygon = Polygon([TopLeFt, TopRight, bottomLeft, bottomRight])
        self.polygon_array.insert(3, polygon)

        # pts = np.array([TopLeFt, TopRight, bottomRight, bottomLeft], np.int32)
        # pts = pts.reshape((-1, 1, 2))
        # cv2.polylines(self.img, [pts], True, (255, 0, 0))

    def find_area_4(self):
        TopLeFt = self.palmIn.finger4.top_1
        TopRight = self.palmIn.finger4.top_2
        bottomLeft = self.palmIn.finger4.bottom_1
        bottomRight = self.palmIn.finger4.bottom_2
        polygon = Polygon([TopLeFt, TopRight, bottomLeft, bottomRight])
        self.polygon_array.insert(4, polygon)

        # pts = np.array([TopLeFt, TopRight, bottomRight, bottomLeft], np.int32)
        # pts = pts.reshape((-1, 1, 2))
        # cv2.polylines(self.img, [pts], True, (255, 0, 0))

    def find_area_5(self):
        TopLeFt = self.palmIn.finger5.top_1
        TopRight = self.palmIn.finger5.top_2
        bottomLeft = self.palmIn.finger5.bottom_1
        bottomRight = self.palmIn.finger5.bottom_2
        polygon = Polygon([TopLeFt, TopRight, bottomLeft, bottomRight])
        self.polygon_array.insert(5, polygon)

        # pts = np.array([TopLeFt, TopRight, bottomRight, bottomLeft], np.int32)
        # pts = pts.reshape((-1, 1, 2))
        # cv2.polylines(self.img, [pts], True, (255, 0, 0))
        # show results
        # Ip.show_pic(self.img, "find_finger")


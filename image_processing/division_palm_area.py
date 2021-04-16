import cv2
from image_processing import convert_gray_scale as Ip, palm as P
import numpy as np
from shapely.geometry.polygon import Polygon


class DivisionPalmArea:

    def __init__(self, image, areas_points_list):
        # self.palmIn = P.Palm(processed_image, path)
        # self.palmIn.detect_fingers()
        self.polygon_array = []
        self.img = np.array(image)
        self.find_areas(areas_points_list)

    def find_areas(self, areas_points_list):
        self.find_area_0(areas_points_list[0])
        self.find_area_1(areas_points_list[1])
        self.find_area_2(areas_points_list[2])
        self.find_area_3(areas_points_list[3])
        self.find_area_4(areas_points_list[4])
        self.find_area_5(areas_points_list[5])

    def find_area_0(self, area_points_list):
        polygon = Polygon([area_points_list[0], area_points_list[1], area_points_list[2], area_points_list[3],
                           area_points_list[4], area_points_list[5], area_points_list[6], area_points_list[7],
                           area_points_list[8]])
        self.polygon_array.insert(0, polygon)

        # pts = np.array([self.TopLeFt, self.TopRight, self.bottomRight, self.bottomLeft], np.int32)  # add point according to tramonstics request
        # pts = pts.reshape((-1, 1, 2))
        # cv2.polylines(self.img, [pts], True, (255, 0, 0))

    def find_area_1(self, area_points_list):
        polygon = Polygon([area_points_list[0], area_points_list[1], area_points_list[2], area_points_list[3]])
        self.polygon_array.insert(1, polygon)

        # pts = np.array([TopLeFt, TopRight, bottomRight, bottomLeft], np.int32)
        # pts = pts.reshape((-1, 1, 2))
        # cv2.polylines(self.img, [pts], True, (255, 0, 0))

    def find_area_2(self, area_points_list):
        polygon = Polygon([area_points_list[0], area_points_list[1], area_points_list[2], area_points_list[3]])
        self.polygon_array.insert(2, polygon)

        # pts = np.array([TopLeFt, TopRight, bottomLeft, bottomRight], np.int32)
        # pts = pts.reshape((-1, 1, 2))
        # cv2.polylines(self.img, [pts], True, (255, 0, 0))

    def find_area_3(self, area_points_list):
        polygon = Polygon([area_points_list[0], area_points_list[1], area_points_list[2], area_points_list[3]])
        self.polygon_array.insert(3, polygon)

        # pts = np.array([TopLeFt, TopRight, bottomRight, bottomLeft], np.int32)
        # pts = pts.reshape((-1, 1, 2))
        # cv2.polylines(self.img, [pts], True, (255, 0, 0))

    def find_area_4(self, area_points_list):
        polygon = Polygon([area_points_list[0], area_points_list[1], area_points_list[2], area_points_list[3]])
        self.polygon_array.insert(4, polygon)

        # pts = np.array([TopLeFt, TopRight, bottomRight, bottomLeft], np.int32)
        # pts = pts.reshape((-1, 1, 2))
        # cv2.polylines(self.img, [pts], True, (255, 0, 0))

    def find_area_5(self, area_points_list):
        polygon = Polygon([area_points_list[0], area_points_list[1], area_points_list[2], area_points_list[3]])
        self.polygon_array.insert(5, polygon)

        # pts = np.array([TopLeFt, TopRight, bottomRight, bottomLeft], np.int32)
        # pts = pts.reshape((-1, 1, 2))
        # cv2.polylines(self.img, [pts], True, (255, 0, 0))
        # show results
        # Ip.show_pic(self.img, "find_finger")


import cv2 as cv
import numpy as np
from image_processing import division_palm_area as Div, finding_hotspots as Find
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from image_processing import convert_gray_scale as Ip


class SortHotPointInArea:

    def __init__(self, processed_image, division_obj, hotspots_ob):
        self.image = processed_image
        self.divPalm = division_obj
        self.findPoint = hotspots_ob
        self.array_area_0 = []
        self.array_area_1 = []
        self.array_area_2 = []
        self.array_area_3 = []
        self.array_area_4 = []
        self.array_area_5 = []
        self.listContours = []
        self.find_listContours()
        self.sort_hotspots()

    def find_listContours(self):
        ret, thresh = cv.threshold(self.image, 127, 255, 0)
        contours, hierarchy = cv.findContours(thresh, 1, 2)
        for x in contours:
            for p in x:
                for m in p:
                    self.listContours.append((m[0], m[1]))

    def sort_hotspots(self):
        self.area_0()
        self.area_1()
        self.area_2()
        self.area_3()
        self.area_4()
        self.area_5()

    def area_0(self):
        for p in self.findPoint.pointList:
            polygon = self.divPalm.polygon_array[0] #change to palm point
            point = Point(p)
            if polygon.contains(point):
                if p not in self.listContours:
                    self.array_area_0.append(p)
                    self.findPoint.pointList.remove(p)

    def area_1(self):
        for p in self.findPoint.pointList:
            polygon = self.divPalm.polygon_array[1]
            point = Point(p)
            if polygon.contains(point):
                if p not in self.listContours:
                    self.array_area_1.append(p)
                    self.findPoint.pointList.remove(p)

    def area_2(self):
        for p in self.findPoint.pointList:
            polygon = self.divPalm.polygon_array[2]
            point = Point(p)
            if polygon.contains(point):
                if p not in self.listContours:
                    self.array_area_2.append(p)
                    self.findPoint.pointList.remove(p)

    def area_3(self):
        for p in self.findPoint.pointList:
            polygon = self.divPalm.polygon_array[3]
            point = Point(p)
            if polygon.contains(point):
                if p not in self.listContours:
                    self.array_area_3.append(p)
                    self.findPoint.pointList.remove(p)

    def area_4(self):
        for p in self.findPoint.pointList:
            polygon = self.divPalm.polygon_array[4]
            point = Point(p)
            if polygon.contains(point):
                if p not in self.listContours:
                    self.array_area_4.append(p)
                    self.findPoint.pointList.remove(p)

    def area_5(self):
        for p in self.findPoint.pointList:
            polygon = self.divPalm.polygon_array[5]
            point = Point(p)
            if polygon.contains(point):
                if p not in self.listContours:
                    self.array_area_5.append(p)
                    self.findPoint.pointList.remove(p)

        # shows results
        # Ip.show_pic(self.divPalm.img, "div area")

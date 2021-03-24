import cv2 as cv
from Thermanostics.imageProcessing import  DivisionPalmArea as Div ,FindingHotspotsInPicture as Find
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from Thermanostics.imageProcessing import ConvertGrayScale as Ip


class SortHotPointInArea:

    def __init__(self, processed_image, path, size):
        self.image = processed_image
        self.divPalm = Div.DivisionPalmArea(processed_image, path)
        self.findPoint = Find.FindingHotspotsInPicture(processed_image,path)
        self.findPoint.pass_on_image(size)
        self.array_area_0 = []
        self.array_area_1 = []
        self.array_area_2 = []
        self.array_area_3 = []
        self.array_area_4 = []
        self.array_area_5 = []
        self.listContours = []
        ret, thresh = cv.threshold(self.image, 127, 255, 0)
        contours, hierarchy = cv.findContours(thresh, 1, 2)
        for x in contours:
            for p in x:
                for m in p:
                    self.listContours.append((m[0], m[1]))

    def area_0(self):
        self.divPalm.find_area_0()
        for p in self.findPoint.pointList:
            polygon = Polygon([self.divPalm.TopLeFt, self.divPalm.TopRight, self.divPalm.bottomLeft, self.divPalm.bottomRight]) #change to palm point
            point = Point(p)
            if polygon.contains(point):
                if p not in self.listContours:
                    self.array_area_0.append(p)
                    self.findPoint.pointList.remove(p)
    def area_1(self):
        self.divPalm.find_finger_1()
        for p in self.findPoint.pointList:
            polygon = Polygon([self.divPalm.TopLeFt, self.divPalm.TopRight, self.divPalm.bottomRight,self.divPalm.bottomLeft])
            point = Point(p)
            if polygon.contains(point):
                if p not in self.listContours:
                    self.array_area_1.append(p)
                    self.findPoint.pointList.remove(p)
    def arae_2(self):
        self.divPalm.find_finger_2()
        for p in self.findPoint.pointList:
            polygon = Polygon([self.divPalm.TopLeFt, self.divPalm.TopLeFt, self.divPalm.bottomRight, self.divPalm.bottomLeft])
            point = Point(p)
            if polygon.contains(point):
                if p not in self.listContours:
                    self.array_area_1.append(p)
                    self.findPoint.pointList.remove(p)
                    # print(polygon.contains(point), "area1___________")
    def arae_3(self):
        self.divPalm.find_finger_3()
        for p in self.findPoint.pointList:
            polygon = Polygon([self.divPalm.TopLeFt, self.divPalm.TopRight, self.divPalm.bottomRight, self.divPalm.bottomLeft])
            point = Point(p)
            if polygon.contains(point):
                if p not in self.listContours:
                    self.array_area_1.append(p)
                    self.findPoint.pointList.remove(p)
    def arae_4(self):
        self.divPalm.find_finger_4()
        for p in self.findPoint.pointList:
            polygon = Polygon([self.divPalm.TopLeFt, self.divPalm.TopRight, self.divPalm.bottomRight, self.divPalm.bottomLeft])
            point = Point(p)
            if polygon.contains(point):
                if p not in self.listContours:
                    self.array_area_1.append(p)
                    self.findPoint.pointList.remove(p)
    def arae_5(self):
        self.divPalm.find_finger_5()
        for p in self.findPoint.pointList:
            polygon = Polygon([self.divPalm.TopLeFt, self.divPalm.TopRight, self.divPalm.bottomLeft, self.divPalm.bottomRight])
            point = Point(p)
            if polygon.contains(point):
                if p not in self.listContours:
                    self.array_area_1.append(p)
                    self.findPoint.pointList.remove(p)

        Ip.show_pic(self.divPalm.img, "div area")

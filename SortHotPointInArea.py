import cv2
import DivisionPalmArea as Div
import ImageProcessing as Ip
import numpy as np
import FindingHotspotsInPicture as Find
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


class SortHotPointInArea:

    def __init__(self, processed_image, path,size):
        self.divPalm = Div.DivisionPalmArea(processed_image, path)
        self.findPoint=Find.FindingHotspotsInPicture(processed_image, path)
        self.findPoint.passOnImage(size)
        self.ArrayArea0=[]
        self.ArrayArea1=[]
        self.ArrayArea2=[]
        self.ArrayArea3=[]
        self.ArrayArea4=[]
        self.ArrayArea5=[]

    def Area0(self):
        print("area 0")
    def Area1(self):
        self.divPalm.FindFinger1()
        print("area1")
        for p in self.findPoint.pointList:
              polygon = Polygon([self.divPalm.rectTopLeFt, self.divPalm.rectTopRight, self.divPalm.bottomRight, (435,109)])
              point = Point(p)
              if polygon.contains(point):
                  self.ArrayArea1.append(p)
                  cv2.circle(self.divPalm.img, p, 4, (255, 128, 0), 2)
                  self.findPoint.pointList.remove(p)
                  #print(polygon.contains(point), "area1___________")
        Ip.show_pic(self.divPalm.img,"p")
    def Arae2(self):
        self.divPalm.FindFinger2()
        print("area2")
        for p in self.findPoint.pointList:
            polygon = Polygon([[self.divPalm.rectTopLeFt[0],self.divPalm.rectTopLeFt[1]+20],[self.divPalm.rectTopLeFt[0],self.divPalm.rectTopLeFt[1]-20],[self.divPalm.bottomRight[0],210],[self.divPalm.bottomRight[0],self.divPalm.bottomRight[1]]])
            point = Point(p)
            if polygon.contains(point):
                self.ArrayArea1.append(p)
                cv2.circle(self.divPalm.img, p, 4, (255, 128, 0), 2)
                self.findPoint.pointList.remove(p)
                # print(polygon.contains(point), "area1___________")
        Ip.show_pic(self.divPalm.img, "p")
    def Arae3(self):
        self.divPalm.FindFinger3()
        print("area3")
        for p in self.findPoint.pointList:
            polygon = Polygon([[self.divPalm.rectTopLeFt[0],310],[self.divPalm.rectTopLeFt[0],360], self.divPalm.bottomRight,self.divPalm.bottomLeft])
            point = Point(p)
            if polygon.contains(point):
                self.ArrayArea1.append(p)
                cv2.circle(self.divPalm.img, p, 4, (255, 128, 0), 2)
                self.findPoint.pointList.remove(p)
                # print(polygon.contains(point), "area1___________")
        Ip.show_pic(self.divPalm.img, "p")

    def Arae4(self):
        self.divPalm.FindFinger4()
        print("area4")
        for p in self.findPoint.pointList:
            polygon = Polygon([[self.divPalm.rectTopLeFt[0],370],[self.divPalm.rectTopLeFt[0],430], self.divPalm.bottomRight, self.divPalm.bottomLeft])
            point = Point(p)
            if polygon.contains(point):
                self.ArrayArea1.append(p)
                cv2.circle(self.divPalm.img, p, 4, (255, 128, 0), 2)
                self.findPoint.pointList.remove(p)
                # print(polygon.contains(point), "area1___________")
        Ip.show_pic(self.divPalm.img, "p")

    def Arae5(self):
        self.divPalm.FindFinger5()
        print("area5")
        for p in self.findPoint.pointList:
            polygon = Polygon([[self.divPalm.rectTopLeFt[0],430], [self.divPalm.rectTopLeFt[0],480],[self.divPalm.bottomLeft[0],450], self.divPalm.bottomLeft])
            point = Point(p)
            if polygon.contains(point):
                self.ArrayArea1.append(p)
                cv2.circle(self.divPalm.img, p, 4, (255, 128, 0), 2)
                self.findPoint.pointList.remove(p)
                # print(polygon.contains(point), "area1___________")
        Ip.show_pic(self.divPalm.img, "p")

import cv2
import DivisionPalmArea as Div
import ImageProcessing as Ip
import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

class SortHotPointInArea:

    def __init__(self, processed_image, path):
        self.divPalm = Div.DivisionPalmArea(processed_image, path)
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
        point = Point(367,99)
        polygon = Polygon([self.divPalm.rectTopLeFt, self.divPalm.rectTopRight, self.divPalm.bottomRight, (435,109)])
        if polygon.contains(point):
            self.ArrayArea1.append(point)
        print(polygon.contains(point), "area1___________")
    def Arae2(self):
        self.divPalm.FindFinger2()
        print("area2")
        point = Point(227,241)
        polygon = Polygon([[self.divPalm.rectTopLeFt[0],self.divPalm.rectTopLeFt[1]+20],[self.divPalm.rectTopLeFt[0],self.divPalm.rectTopLeFt[1]-20],[self.divPalm.bottomRight[0],210],[self.divPalm.bottomRight[0],self.divPalm.bottomRight[1]]])
        if polygon.contains(point):
            self.ArrayArea2.append(point)
        print(polygon.contains(point), "area2_________")
    def Arae3(self):
        self.divPalm.FindFinger3()
        print("area3")
        point = Point(136,324)
        polygon = Polygon([[self.divPalm.rectTopLeFt[0],310],[self.divPalm.rectTopLeFt[0],360], self.divPalm.bottomRight,self.divPalm.bottomLeft])
        if polygon.contains(point):
            self.ArrayArea3.append(point)
        print(polygon.contains(point), "area3_________")

    def Arae4(self):
        self.divPalm.FindFinger4()
        print("area4")
        point = Point(186, 373)
        polygon = Polygon([[self.divPalm.rectTopLeFt[0],370],[self.divPalm.rectTopLeFt[0],430], self.divPalm.bottomRight, self.divPalm.bottomLeft])
        if polygon.contains(point):
            self.ArrayArea4.append(point)
        print(polygon.contains(point), "area4_________")

    def Arae5(self):
        self.divPalm.FindFinger5()
        print("area5")
        point = Point(263,435)
        polygon = Polygon([[self.divPalm.rectTopLeFt[0],430], [self.divPalm.rectTopLeFt[0],480],[self.divPalm.bottomLeft[0],450], self.divPalm.bottomLeft])
        if polygon.contains(point):
            self.ArrayArea5.append(point)
        print(polygon.contains(point), "area5_________")

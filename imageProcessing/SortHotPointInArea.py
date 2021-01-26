import cv2
from imageProcessing import DivisionPalmArea as Div, FindingHotspotsInPicture as Find
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from imageProcessing import ConvertGrayScale as Ip


class SortHotPointInArea:

    def __init__(self, processed_image, path,size):
        self.image=processed_image
        self.divPalm = Div.DivisionPalmArea(processed_image, path)
        self.findPoint=Find.FindingHotspotsInPicture(processed_image, path)
        self.findPoint.passOnImage(size)
        self.ArrayArea0=[]
        self.ArrayArea1=[]
        self.ArrayArea2=[]
        self.ArrayArea3=[]
        self.ArrayArea4 = []
        self.ArrayArea5 = []
        self.ListContours=[]
        ret, thresh = cv2.threshold(self.image, 127, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, 1, 2)
        for x in contours:
            for p in x:
                for m in p:
                    self.ListContours.append((m[0],m[1]))

    def Area0(self):
        self.divPalm.FindArea0()
        print("area 0")

    def Area1(self):
        self.divPalm.FindFinger1()
        print("area1")
        for p in self.findPoint.pointList:
              polygon = Polygon([self.divPalm.TopLeFt, self.divPalm.TopRight, self.divPalm.bottomRight, (435,109)])
              point = Point(p)
              if polygon.contains(point):
                  if p not in self.ListContours:
                      self.ArrayArea1.append(p)

                      self.findPoint.pointList.remove(p)
                      #print(polygon.contains(point), "area1___________")
        Ip.show_pic(self.divPalm.img,"p")

    def Arae2(self):
        self.divPalm.FindFinger2()
        print("area2")
        for p in self.findPoint.pointList:
            polygon = Polygon([self.divPalm.TopLeFt,self.divPalm.TopLeFt,self.divPalm.bottomRight,self.divPalm.bottomLeft])
            point = Point(p)
            if polygon.contains(point):
                if p not in self.ListContours:
                    self.ArrayArea1.append(p)
                    self.findPoint.pointList.remove(p)
                    # print(polygon.contains(point), "area1___________")
        Ip.show_pic(self.divPalm.img, "p")

    def Arae3(self):
        self.divPalm.FindFinger3()
        print("area3")
        for p in self.findPoint.pointList:
            polygon = Polygon([self.divPalm.TopLeFt,self.divPalm.TopRight,self.divPalm.bottomRight,self.divPalm.bottomLeft])
            point = Point(p)
            if polygon.contains(point):
                if p not in self.ListContours:
                    self.ArrayArea1.append(p)
                    self.findPoint.pointList.remove(p)
                    # print(polygon.contains(point), "area1___________")
        Ip.show_pic(self.divPalm.img, "p")

    def Arae4(self):
        self.divPalm.FindFinger4()
        print("area4")
        for p in self.findPoint.pointList:
            polygon = Polygon([self.divPalm.TopLeFt,self.divPalm.TopRight, self.divPalm.bottomRight, self.divPalm.bottomLeft])
            point = Point(p)
            if polygon.contains(point):
                if p not in self.ListContours:
                    self.ArrayArea1.append(p)
                    self.findPoint.pointList.remove(p)
                    # print(polygon.contains(point), "area1___________")
        Ip.show_pic(self.divPalm.img, "p")

    def Arae5(self):
        self.divPalm.FindFinger5()
        print("area5")
        for p in self.findPoint.pointList:
            polygon = Polygon([self.divPalm.TopLeFt,self.divPalm.TopRight,self.divPalm.bottomLeft, self.divPalm.bottomRight])
            point = Point(p)
            if polygon.contains(point):
                if p not in self.ListContours:
                    self.ArrayArea1.append(p)
                    self.findPoint.pointList.remove(p)
                    # print(polygon.contains(point), "area1___________")
        Ip.show_pic(self.divPalm.img, "p")

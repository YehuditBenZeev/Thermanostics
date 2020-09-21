import Palm as P
import cv2
import ImageProcessing as Ip
import numpy as np


class DivisionPalmArea:

    def __init__(self, processed_image, path):
        self.palmIn=P.Palm(processed_image, path)
        self.palmIn.detect_fingers()
        self.rectTopLeFt=0
        self.rectTopRight=0
        self.bottomLeft=0
        self.bottomRight=0
        self.img=np.array(self.palmIn.image)


    def FindFinger1(self):
        self.rectTopLeFt = self.palmIn.finger1.top_1
        self.rectTopRight=self.palmIn.finger1.top_2
        self.bottomLeft=self.palmIn.finger1.bottom_1
        self.bottomRight=self.palmIn.finger1.bottom_2
        i=self.rectTopLeFt[0]
        j=self.rectTopLeFt[1]
        cv2.circle(self.img, (i, j), 4, (255, 128, 0), 2)
        i = self.rectTopRight[0]
        j = self.rectTopRight[1]
        cv2.circle(self.img, (i, j), 4, (255, 128, 0), 2)
        i = self.bottomRight[0]
        j = self.bottomRight[1]
        cv2.circle(self.img, (i, j), 4, (255, 128, 0), 2)

        pts = np.array([self.rectTopLeFt,self.rectTopRight,self.bottomRight,[371, 70]], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(self.img, [pts], True, (255, 0, 0))
        Ip.show_pic(self.img,"p")
        print(self.rectTopLeFt,self.rectTopRight,self.bottomRight,self.bottomLeft,"++++++++++++++++++++")
        print(int(self.rectTopLeFt[0]+self.bottomRight[0])/2)
        cv2.circle(self.img, (i, j), 4, (255, 128, 0), 2)


    def FindFinger2(self):
        self.rectTopLeFt = self.palmIn.finger2.top_1
        self.rectTopRight = self.palmIn.finger2.top_2
        self.bottomLeft = self.palmIn.finger2.bottom_1
        self.bottomRight = self.palmIn.finger2.bottom_2
        i = self.rectTopLeFt[0]
        j = self.rectTopLeFt[1]
        cv2.circle(self.img, (i, j), 4, (255, 128, 0), 2)
        i = self.bottomRight[0]
        j = self.bottomRight[1]
        cv2.circle(self.img, (i, j), 4, (255, 128, 0), 2)
        pts = np.array([[self.rectTopLeFt[0],self.rectTopLeFt[1]+20],[self.rectTopLeFt[0],self.rectTopLeFt[1]-20],[self.bottomRight[0],210],[self.bottomRight[0],self.bottomRight[1]]], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(self.img, [pts], True, (255, 0, 0))
        Ip.show_pic(self.img, "p")
        print(self.rectTopLeFt, self.rectTopRight, self.bottomRight, self.bottomLeft, "++++++++++++++++++++")
    def FindFinger3(self):
        self.rectTopLeFt = self.palmIn.finger3.top_1
        self.rectTopRight = self.palmIn.finger3.top_2
        self.bottomLeft = self.palmIn.finger3.bottom_1
        self.bottomRight = self.palmIn.finger4.bottom_1
        i = self.palmIn.finger4.bottom_1[0]
        j = self.palmIn.finger4.bottom_1[1]
        cv2.circle(self.img, (i, j), 4, (255, 128, 0), 2)

        pts = np.array([[self.rectTopLeFt[0],310],[self.rectTopLeFt[0],360], self.bottomRight,self.bottomLeft], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(self.img, [pts], True, (255, 0, 0))
        Ip.show_pic(self.img, "p")
        print(self.rectTopLeFt, self.rectTopRight, self.bottomRight, self.bottomLeft, "++++++++++++++++++++")

    def FindFinger4(self):
        self.rectTopLeFt = self.palmIn.finger4.top_1
        self.rectTopRight = self.palmIn.finger4.top_2
        self.bottomLeft = self.palmIn.finger4.bottom_1
        self.bottomRight = self.palmIn.finger4.bottom_2
        pts = np.array([[self.rectTopLeFt[0],370],[self.rectTopLeFt[0],430], self.bottomRight, self.bottomLeft], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(self.img, [pts], True, (255, 0, 0))
        Ip.show_pic(self.img, "p")
        print(self.rectTopLeFt, self.rectTopRight, self.bottomRight, self.bottomLeft, "++++++++++++++++++++")

    def FindFinger5(self):
        self.rectTopLeFt = self.palmIn.finger5.top_1
        self.rectTopRight = self.palmIn.finger5.top_2
        self.bottomLeft = self.palmIn.finger5.bottom_1
        self.bottomRight = self.palmIn.finger5.bottom_2
        i = self.palmIn.finger4.bottom_2[0]
        j = self.palmIn.finger4.bottom_2[1]
        cv2.circle(self.img, (i, j), 4, (255, 128, 0), 2)
        pts = np.array([[self.rectTopLeFt[0],430], [self.rectTopLeFt[0],480],[self.bottomLeft[0],450], self.bottomLeft], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(self.img, [pts], True, (255, 0, 0))
        Ip.show_pic(self.img, "p")
        print(self.rectTopLeFt, self.rectTopRight, self.bottomRight, self.bottomLeft, "++++++++++++++++++++")


import cv2
import numpy as np


def show_pic(image, name):
    window_name = name
    cv2.imshow(window_name, image)
    cv2.waitKey(0)

class FindingHotsPoint:
    def __init__(self,processed_image):
        self.image =cv2.imread(processed_image, cv2.IMREAD_GRAYSCALE) # image color gray 2D
        print(self.image[283,224],self.image[352,175],self.image[362,298])
        cv2.circle(self.image, (283,224), 5, (255, 0, 127), 2)
        cv2.circle(self.image, (352,175), 7, (255, 0, 127), 2)
        show_pic(self.image, "3")
        self.number_tuple = (0, 0)
        self.pointList = []
        self.h, self.w = self.image.shape
        print(self.image.shape)
        self.img = np.array(self.image)
        show_pic(self.image, "black")

    def findMaxPointInArea(self, p1, p2, p3, p4, valu):
        jo = 0
        io = 0
        # check if point in area
        if p1 < 0:
            return 0, 0, 0
        if p2 < 0:
            return 0, 0, 0
        if p3 > 373:
            return 0, 0, 0
        if p4 > 523:
            return 0, 0, 0
        else:
            temp = valu
            for i in range(p1, p3):
                for j in range(p2, p4):
                    x = self.image[i][j]
                    if x > temp:
                        temp = self.image[i][j]
                        io = i
                        jo = j
            return temp, io, jo

    # #scan all picture funk get point and define to area
    def ScanImage(self, i, j, k, valu):
        l1 = i - k
        l2 = j - k
        l3 = i + k
        l4 = j + k
        valuePoint, io, ji = self.findMaxPointInArea(l1, l2, (int)(l3), (int)(l4), valu)
        if valuePoint == 0 & io == 0 & ji == 0:
            return 0, 0, 0
        else:
            return valuePoint, io, ji

    def passOnImage(self, size):
        flag1 = False
        flag2 = False
        flag3 = False
        flag4 = False
        for i in range(1, self.h - 1):
            for j in range(1, self.w - 1):
                if i - 1 > 0:
                    if self.image[i - 1][j] < self.image[i][j]:
                        flag1 = True
                if j - 1 > 0:
                    if self.image[i][j - 1] < self.image[i][j]:
                        flag2 = True

                if i + 1 < self.h:
                    if self.image[i + 1][j] < self.image[i][j]:
                        flag3 = True
                if j + 1 < self.w:
                    if self.image[i][j + 1] < self.image[i][j]:
                        flag4 = True
                if flag1 & flag2 & flag3 & flag4:
                    #print(self.image[i][j])
                    if self.image[i][j] >173:
                        cv2.circle(self.image, (i,j), 3, (255, 0, 127), 2)
                        show_pic(self.image, "3")

                        t1, t2, t3 = self.ScanImage(i, j, size,
                                                    0)  # sage1: return max poin in area in size 10 of point
                        self.number_tuple = (t3, t2)
                        self.pointList.append(self.number_tuple)
                    flag1 = False
                    flag2 = False
                    flag3 = False
                    flag4 = False


        # print array that hold max point from stage1
        print(self.pointList, "pointList")
        self.pointList = list(dict.fromkeys(self.pointList))
        print(self.pointList)
        for i in self.pointList:
            cv2.circle(self.image, i, 4, (255, 128, 0), 2)
        show_pic(self.image, "p")

if __name__ == "__main__":
    a=FindingHotsPoint("514 RF1.bmp")
    print(a.passOnImage(10))
import numpy as np
import cv2
from image_processing import convert_gray_scale as Ip


class FindingHotspots:

    def __init__(self, processed_image, size):
        self.image = processed_image
        self.pointList = []
        self.pass_on_image(size)

    def find_min_point_in_area(self, p1, p2, p3, p4):
        jo = 0
        io = 0
        h, w = self.image.shape

        # check if point in area
        if p1 < 0 or p2 < 0 or p3 > h or p4 > w:
            return -1, -1, -1
        temp = 255
        for i in range(p1, p3): #run on small matrix
            for j in range(p2, p4):
                x = self.image[i][j]
                if x < temp:
                    temp = x
                    io = i
                    jo = j
        return temp, io, jo  # return max value

    # scan all picture funk get point and define to area
    def scan_image(self, i, j, k):
        l1 = i - k  # defines a 2*k+1 matrix
        l2 = j - k
        l3 = i + k
        l4 = j + k

        return self.find_min_point_in_area(l1, l2, l3, l4)

    def pass_on_image(self, size):
        h, w = self.image.shape
        img = np.array(self.image)

        flag1 = False
        flag2 = False
        flag3 = False
        flag4 = False
        for i in range(1, h - 1):  # pass on image
            for j in range(1, w - 1):
                    if self.image[i-1][j] > self.image[i][j]:
                        flag1 = True
                    if self.image[i][j-1] > self.image[i][j]:
                        flag2 = True
                    if self.image[i+1][j] > self.image[i][j]:
                        flag3 = True
                    if self.image[i][j+1] > self.image[i][j]:
                        flag4 = True
                    if flag1 & flag2 & flag3 & flag4:#point is eXstrim point and higher then the threshold
                        if self.image[i][j] < 127:
                            valuePoint, x, y = self.scan_image(i, j, size)  # sage1: return max poin in area in size 10 of point
                            if not((valuePoint == -1) & (x == -1) & (y == -1)) :
                                number_tuple = (y, x)
                                self.pointList.append(number_tuple)
                        flag1 = False
                        flag2 = False
                        flag3 = False
                        flag4 = False

        self.pointList = list(dict.fromkeys(self.pointList))
        for i in self.pointList:
            cv2.circle(img, i, 4, (0, 0, 250), 2)
        Ip.show_pic(img, "p")


if __name__ == '__main__':
    im = cv2.imread("../images/514 RF.bmp")
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    hotspot = FindingHotspots(gray, 20)
    print("done")

import cv2
import  numpy as np
from imageProcessing import CovertGrayScale as Ip

class ObjectTest:
    def __init__(self,image):
        self.image=image

    def trapeze(self,point_1,point_2,point_3,point_4):
        pts = np.array([point_1,point_2,point_3,point_4], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(self.image, [pts], True, (255, 0, 0))
        Ip.show_pic(self.img, "p")






if __name__ == "__main__":
    a = ObjectTest("505 RF Sick.bmp")


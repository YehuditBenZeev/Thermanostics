import numpy as np
import argparse
import imutils
import cv2
from imageProcessing import CovertGrayScale as Ip


class Rotation:

    def __init__(self, processed_image, path):
        self.image = processed_image
        self.path=path

        # construct the argument parse and parse the arguments
        # loop over the rotation angles
        for angle in np.arange(0, 360, 15):
            rotated = imutils.rotate(self.image, angle)
            cv2.imshow("Rotated (Problematic)", rotated)
            cv2.waitKey(0)
        # loop over the rotation angles again, this time ensure the
        # entire pill is still within the ROI after rotation
        # for angle in np.arange(0, 360, 15):
        #     rotated = imutils.rotate_bound(self.image, angle)
        #     cv2.imshow("Rotated (Correct)", rotated)
        #     cv2.waitKey(0)
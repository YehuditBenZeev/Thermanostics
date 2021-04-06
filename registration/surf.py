import cv2
import numpy as np

MAX_MATCHES = 500
GOOD_MATCH_PERCENT = 0.15


def get_homography(im1, im2):
    """Given two images, returns the matches"""
    surf = cv2.xfeatures2d.SURF_create()



def get_homography_good_features(im1, im2):
    pass


if __name__ == '__main__':
    refFilename = "../images/514 RF.bmp"
    Filename = "../images/509 RF.bmp"
    get_homography(refFilename,Filename)

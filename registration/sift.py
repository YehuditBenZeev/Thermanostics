import cv2 as cv
import numpy as np
from registration.harris import harris_corner_detection

MAX_MATCHES = 500
GOOD_MATCH_PERCENT = 0.15
MIN_MATCH_COUNT = 4


def get_matching_points(im1, im2, matcher):
    # Initiate SIFT detector
    sift = cv.SIFT_create()
    kps1, des1 = sift.detectAndCompute(im1, None)
    kps2, des2 = sift.detectAndCompute(im2, None)

    udes1 = np.uint8(des1)
    udes2 = np.uint8(des2)

    matches = matcher(udes1, udes2)

    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = kps1[match.queryIdx].pt
        points2[i, :] = kps2[match.trainIdx].pt

    return points1, points2
<<<<<<< HEAD
def get_matching_points_good_features(im1, im2):

=======


def get_matching_points_good_features(im1, im2, matcher):
>>>>>>> 153e949dd5cf134c68fc8691d904de10eef8e7a3
    sift = cv.SIFT_create()

    gray1 = cv.cvtColor(im1, cv.COLOR_BGR2GRAY)
    gray2 = cv.cvtColor(im2, cv.COLOR_BGR2GRAY)

    points1 = cv.goodFeaturesToTrack(gray1, 1000, 0.01, 10)

    kps1 = [cv.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in points1]
    kps1, des1 = sift.compute(gray1, kps1)
    udes1 = np.uint8(des1)

    points2 = cv.goodFeaturesToTrack(gray2, 1000, 0.01, 10)
    kps2 = [cv.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in points2]
    kps2, des2 = sift.compute(im2, kps2)  # ??????????????????????gray2
    udes2 = np.uint8(des2)

    matches = matcher(udes1, udes2)

    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = kps1[match.queryIdx].pt
        points2[i, :] = kps2[match.trainIdx].pt

    return points1, points2


def get_matching_points_harris(im1, im2, matcher):

    gray1 = cv.cvtColor(im1, cv.COLOR_BGR2GRAY)
    gray2 = cv.cvtColor(im2, cv.COLOR_BGR2GRAY)

    points1 = harris_corner_detection(im1)
    points2 = harris_corner_detection(im2)
    sift = cv.SIFT_create()

    kps1 = [cv.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in points1]
    kps1, des1 = sift.compute(gray1, kps1)
    udes1 = np.uint8(des1)

    kps2 = [cv.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in points2]
    kps2, des2 = sift.compute(gray2, kps2)
    udes2 = np.uint8(des2)

    matches = matcher(udes1, udes2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key=lambda x: x.distance)
    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        print(len(matches))
        points1[i, :] = kps1[match.queryIdx].pt
        points2[i, :] = kps2[match.trainIdx].pt

    return points1, points2


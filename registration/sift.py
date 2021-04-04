import cv2 as cv
import numpy as np
from matplotlib import pylab as plt
from Thermanostics.registration import matcher
from Thermanostics.registration.image_stitching import harris_corner_detection

MAX_MATCHES = 500
GOOD_MATCH_PERCENT = 0.15
MIN_MATCH_COUNT = 4


def get_matching_points(im1, im2):
    im3 = im1
    im4 = im2

    # Initiate SIFT detector
    sift = cv.SIFT_create()
    keypoints1, descriptors1 = sift.detectAndCompute(im1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(im2, None)
    cv.drawKeypoints(im1, keypoints1, im3, color=(255, 0, 0))
    plt.imshow(im3)
    cv.drawKeypoints(im2, keypoints1, im4, color=(255, 0, 0))
    plt.imshow(im4)
    # feature matching
    bf = cv.BFMatcher(cv.NORM_L1, crossCheck=True)

    matches = bf.match(descriptors1, descriptors2)
    matches = sorted(matches, key=lambda x: x.distance)

    img3 = cv.drawMatches(im1, keypoints1, im2, keypoints2, matches[:50], im2, flags=2)
    plt.imshow(img3), plt.show()
    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = keypoints1[match.queryIdx].pt
        points2[i, :] = keypoints2[match.trainIdx].pt

    return points1, points2
def get_matching_points_good_features(im1, im2):
    
    sift = cv.SIFT_create()
    gray1 = cv.cvtColor(im1, cv.COLOR_BGR2GRAY)
    gray2 = cv.cvtColor(im2, cv.COLOR_BGR2GRAY)

    points1 = cv.goodFeaturesToTrack(gray1, 1000, 0.01, 10)

    kps1 = [cv.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in points1]  # [2, 3,], [4, 5], [3, 4] -> [[2, 4, 3], [3, 5, 4]]
    kps1, des1 = sift.compute(gray1, kps1)
    udes1= np.uint8(des1)

    points2 = cv.goodFeaturesToTrack(gray2, 1000, 0.01, 10)
    kps2 = [cv.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in points2]
    kps2, des2 = sift.compute(im2, kps2)
    udes2 = np.uint8(des2)

    matches =matcher.matcher_DescriptorMatcher(udes1,udes2)

    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = kps1[match.queryIdx].pt
        points2[i, :] = kps2[match.trainIdx].pt

    return points1, points2

def get_matching_points_harris(link1, link2):
    im1 = cv.imread(link1, cv.IMREAD_COLOR)
    im2 = cv.imread(link2, cv.IMREAD_COLOR)
    gray1 = cv.cvtColor(im1, cv.COLOR_BGR2GRAY)
    gray2 = cv.cvtColor(im2, cv.COLOR_BGR2GRAY)

    points1 = harris_corner_detection(link1)
    points2 = harris_corner_detection(link2)
    sift = cv.SIFT_create()
    print(points1)
    print(points2)
    coun=0
    str=[]
    for p in points1[0]:
        coun+=1
        str.append(cv.KeyPoint(x=p[0],y=p[1],_size=20))

    kps1 = [cv.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in points1]
    kps1, des1 = sift.compute(gray1, str)
    udes1 = np.uint8(des1)

    kps2 = [cv.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in points2]
    kps2, des2 = sift.compute(gray2, kps2)
    udes2 = np.uint8(des2)

    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

    # Match descriptors.

    matches = bf.match(udes1, udes2)
    # Sort them in the order of their distance.
    matches = sorted(matches, key=lambda x: x.distance)
    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        print(len(matches))
        points1[i, :] = kps1[match.queryIdx].pt
        points2[i, :] = kps2[match.trainIdx].pt
    return points1,points2


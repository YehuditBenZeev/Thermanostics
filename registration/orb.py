from __future__ import print_function
import cv2 as cv
import numpy as np
from registration.image_stitching import harris_corner_detection
from matplotlib import pylab as plt
from registration import matcher


MAX_MATCHES = 500
GOOD_MATCH_PERCENT = 0.15


def get_matching_points(im1, im2, matcher):
    # Convert images to grayscale
    im1Gray = cv.cvtColor(im1, cv.COLOR_BGR2GRAY)
    im2Gray = cv.cvtColor(im2, cv.COLOR_BGR2GRAY)

    # Detect ORB features and compute descriptors.
    orb = cv.ORB_create(MAX_MATCHES)
    keypoints1, descriptors1 = orb.detectAndCompute(im1Gray, None)
    keypoints2, descriptors2 = orb.detectAndCompute(im2Gray, None)
    print(descriptors1)
    print(descriptors1[0])
    print(descriptors1[0][0])
    print(type(descriptors1))
    print(type(descriptors1[0]))
    print(type(descriptors1[0][0]))

    matches = matcher(descriptors1, descriptors2)

    # Remove not so good matches
    numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
    matches = matches[:numGoodMatches]

    # Draw top matches
    imMatches = cv.drawMatches(im1, keypoints1, im2, keypoints2, matches, None)
    cv.imwrite("matches.jpg", imMatches)

    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = keypoints1[match.queryIdx].pt
        points2[i, :] = keypoints2[match.trainIdx].pt

    return points1, points2


def get_matching_points_good_features(im1, im2, matcher):
    gray1 = cv.cvtColor(im1, cv.COLOR_BGR2GRAY)
    orb = cv.ORB_create()
    points1 = cv.goodFeaturesToTrack(gray1, 1000, 0.01, 10)
    kps1 = [cv.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in points1] # [2, 3,], [4, 5], [3, 4] -> [[2, 4, 3], [3, 5, 4]]
    kps1, des1 = orb.compute(im1, kps1)

    gray2 = cv.cvtColor(im2, cv.COLOR_BGR2GRAY)
    points2 = cv.goodFeaturesToTrack(gray2, 1000, 0.01, 10)
    kps2 = [cv.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in points2]
    kps2, des2 = orb.compute(im2, kps2)

    # # Match features.
    # matcher = cv.DescriptorMatcher_create(cv.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
    # matches = matcher.match(des1, des2, None)
    # matches.sort(key=lambda x: x.distance, reverse=False)


    # # create BFMatcher object
    # bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
    # # Match descriptors.
    # matches = bf.match(des1, des2)
    # # Sort them in the order of their distance.
    # matches = sorted(matches, key=lambda x: x.distance)
    matches = matcher(des1, des2)

    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = kps1[match.queryIdx].pt
        points2[i, :] = kps2[match.trainIdx].pt

    return points1, points2


def get_matching_points_harris(link1, link2, matcher):
    im1 = cv.imread(link1, cv.IMREAD_COLOR)
    im2 = cv.imread(link2, cv.IMREAD_COLOR)

    points1 = harris_corner_detection(link1)
    points2 = harris_corner_detection(link2)

    orb = cv.ORB_create()
    temp = []
    counter = 0
    for f in points2[0]:
        counter += 1
        temp.append(cv.KeyPoint(x=f[0], y=f[1], _size=0.5))
    kps1 = [cv.KeyPoint(x=f[0], y=f[1], _size=0.5) for f in points1[0]]
    kps1, des1 = orb.compute(im1, kps1)

    kps2 = [cv.KeyPoint(x=f[0], y=f[1], _size=0.5) for f in points2[0]]
    kps2, des2 = orb.compute(im2, kps2)
    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

    matches = matcher(des1, des2)
    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = kps1[match.queryIdx].pt
        points2[i, :] = kps2[match.trainIdx].pt

    # Draw first 10 matches.
    # img3 = cv.drawMatches(im1, kps1, im2, kps2, matches, None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    # plt.imshow(img3), plt.show()

    return points1, points2


if __name__ == "__main__":
    print(cv.__version__)
    ref_image_link = "../images/514 RF.bmp"
    image_link = "../images/509 RF.bmp"
    im_reference = cv.imread(ref_image_link, cv.IMREAD_COLOR)
    # print(im_reference.shape)
    im = cv.imread(image_link, cv.IMREAD_COLOR)
    matcher =  matcher.matcher_DescriptorMatcher
    im1Reg, h = get_matching_points(im_reference, im, matcher)
    # im1Reg, h = get_matching_points(ref_image_link, image_link)

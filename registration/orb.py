from __future__ import print_function
import cv2
import numpy as np
from registration.image_stitching import harris_corner_detection


MAX_MATCHES = 500
GOOD_MATCH_PERCENT = 0.15


def align_images(im1, im2):
    # Convert images to grayscale
    im1Gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    im2Gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

    # Detect ORB features and compute descriptors.
    orb = cv2.ORB_create(MAX_MATCHES)
    keypoints1, descriptors1 = orb.detectAndCompute(im1Gray, None)
    keypoints2, descriptors2 = orb.detectAndCompute(im2Gray, None)
    #
    # print("type ", type(keypoints1))
    # print("kp ", keypoints1[0])

    # keypoints1 = harris_corner_detection("../images/514 RF.bmp")
    # keypoints2 = harris_corner_detection("../images/509 RF.bmp")

    # Match features.
    matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
    matches = matcher.match(descriptors1, descriptors2, None)

    # Sort matches by score
    matches.sort(key=lambda x: x.distance, reverse=False)

    # Remove not so good matches
    numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
    matches = matches[:numGoodMatches]

    # Draw top matches
    imMatches = cv2.drawMatches(im1, keypoints1, im2, keypoints2, matches, None)
    cv2.imwrite("matches.jpg", imMatches)

    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = keypoints1[match.queryIdx].pt
        points2[i, :] = keypoints2[match.trainIdx].pt

    print("points1, ", (points1[0][0]))
    print("points2, ", (points2[0][0]))
    # Find homography
    h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

    # Use homography
    height, width, channels = im2.shape
    im1Reg = cv2.warpPerspective(im1, h, (width, height))

    return im1Reg, h

# print(cv2.__version__)


def align_images_good_features(im1, im2):
    gray1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    orb = cv2.ORB_create()
    corners = cv2.goodFeaturesToTrack(gray1, 1000, 0.01, 10)
    kps1 = [cv2.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in corners]
    kps1, des1 = orb.compute(im1, kps1)

    gray2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray2, 1000, 0.01, 10)
    kps2 = [cv2.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in corners]
    kps2, des2 = orb.compute(im2, kps2)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    # Match descriptors.
    matches = bf.match(des1, des2)
    # Sort them in the order of their distance.
    matches = sorted(matches, key=lambda x: x.distance)

    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = kps1[match.queryIdx].pt
        points2[i, :] = kps2[match.trainIdx].pt

    h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

    # Use homography
    height, width, channels = im2.shape
    im1Reg = cv2.warpPerspective(im1, h, (width, height))

    return im1Reg, h


def align_images_harris(link1, link2):
    im1 = cv2.imread(link1, cv2.IMREAD_COLOR)
    im2 = cv2.imread(link2, cv2.IMREAD_COLOR)

    points1 = harris_corner_detection(link1)
    points2 = harris_corner_detection(link2)
    print("points1, ", type(points1))
    print("points2, ", type(points2[0]))
    # Find homography
    h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

    # Use homography
    height, width, channels = im2.shape
    im1Reg = cv2.warpPerspective(im1, h, (width, height))

    return im1Reg, h
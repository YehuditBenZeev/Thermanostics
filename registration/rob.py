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
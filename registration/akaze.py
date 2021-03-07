import cv2
import numpy as np

MAX_MATCHES = 1000
GOOD_MATCH_PERCENT = 0.2


def get_homography(im1, im2):
    im1Gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    im2Gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

    akaze = cv2.AKAZE_create()

    keypoints1, descriptors1 = akaze.detectAndCompute(im1Gray, None)
    keypoints2, descriptors2 = akaze.detectAndCompute(im2Gray, None)

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
    points1 = np.zeros((len(matches), 2), dtype=np.float64)
    points2 = np.zeros((len(matches), 2), dtype=np.float64)

    for i, match in enumerate(matches):
        points1[i, :] = keypoints1[match.queryIdx].pt
        points2[i, :] = keypoints2[match.trainIdx].pt

    # Find homography
    homography, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

    # Use homography
    height, width, channels = im2.shape
    im1Reg = cv2.warpPerspective(im1, homography, (width, height))

    return im1Reg, homography


def get_homography_good_features(im1, im2):
    akaze = cv2.AKAZE_create()

    gray1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray1, 1000, 0.01, 10)
    kps1 = [cv2.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in corners]
    kps1, des1 = akaze.compute(im1, kps1)

    gray2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray2, 1000, 0.01, 10)
    kps2 = [cv2.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in corners]
    kps2, des2 = akaze.compute(im2, kps2)

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

from __future__ import print_function

import cv2
import numpy as np
from matplotlib import pylab as plt


MAX_MATCHES = 1000
GOOD_MATCH_PERCENT = 0.01


def alignImages(im1, im2):
    # Convert images to grayscale
    plt.figure()
    a = plt.subplot(2, 2, 1)

    im1Gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    im2Gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

    plt.title("im1Gray")
    plt.imshow(im1Gray, cmap=plt.get_cmap('gray'))
    plt.subplot(2, 2, 2, sharex=a, sharey=a)
    plt.title("im2Gray")
    plt.imshow(im2Gray, cmap=plt.get_cmap('gray'))

    # Detect ORB features and compute descriptors.
    # orb = cv2.ORB_create(MAX_MATCHES)
    akaze = cv2.AKAZE_create()
    # kp, descriptor = akaze.detectAndCompute(gray, None)
    # SURF
    # sift = cv2.SIFT_create()
    # surf = cv2.SURF(400)
    keypoints1, descriptors1 = akaze.detectAndCompute(im1Gray, None)
    keypoints2, descriptors2 = akaze.detectAndCompute(im2Gray, None)
    print(len(descriptors2), len(descriptors1))
    # Match features.
    matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
    matches = matcher.match(descriptors1, descriptors2, None)
    print(matches)

    bf = cv2.BFMatcher()
    # matches = bf.knnMatch(descriptors1, descriptors2, k=2)

    # # Sort matches by score
    matches.sort(key=lambda x: x.distance, reverse=False)

    # Remove not so good matches
    numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
    matches = matches[:numGoodMatches]

    # good_matches = []
    # for m, n in matches:
    # if m.distance < GOOD_MATCH_PERCENT * n.distance:
    # good_matches.append([m])

    print(len(matches))
    # Draw top matches
    imMatches = cv2.drawMatches(im1, keypoints1, im2, keypoints2, matches, None)
    cv2.imwrite("matches.jpg", imMatches)
    # plt.subplot(2, 2, 3, sharex=a, sharey=a)
    plt.figure()
    plt.title("imMatches")
    plt.imshow(imMatches, cmap=plt.get_cmap('gray'))
    plt.show(block=True)

    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = keypoints1[match.queryIdx].pt
        points2[i, :] = keypoints2[match.trainIdx].pt

    # Find homography
    h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

    # Use homography
    height, width, channels = im2.shape
    im1Reg = cv2.warpPerspective(im1, h, (width, height))

    return im1Reg, h


if __name__ == '__main__':
    # Read reference image
    refFilename = "0.jpg"
    print("Reading reference image : ", refFilename)
    imReference = cv2.imread(refFilename, cv2.IMREAD_COLOR)

    # Read image to be aligned
    imFilename = "0_2.jpg"
    print("Reading image to align : ", imFilename)
    im = cv2.imread(imFilename, cv2.IMREAD_COLOR)

    print("Aligning images ...")
    # Registered image will be resotred in imReg.
    # The estimated homography will be stored in h.
    imReg, h = alignImages(im, imReference)

    # Write aligned image to disk.
    outFilename = "aligned.jpg"
    print("Saving aligned image : ", outFilename)
    cv2.imwrite(outFilename, imReg)

    # Print estimated homography
    print("Estimated homography : \n", h)
    
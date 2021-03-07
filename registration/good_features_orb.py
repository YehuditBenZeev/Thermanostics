import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def get_homography(img1, img2):
    # img1 = cv.imread('506 RF.bmp')
    gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    orb = cv.ORB_create()
    corners = cv.goodFeaturesToTrack(gray1, 1000, 0.01, 10)
    kps1 = [cv.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in corners]
    kps1, des1 = orb.compute(img1,kps1)
    # corners = np.int0(corners)
    # for i in corners:
    #     x,y = i.ravel()
    #     cv.circle(img1,(x,y),3,255,-1)
    # plt.imshow(img1),plt.show()

    # img2 = cv.imread('514 RF1.bmp')
    gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    corners = cv.goodFeaturesToTrack(gray2, 1000, 0.01, 10)
    kps2 = [cv.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in corners]
    kps2, des2 = orb.compute(img2,kps2)
    # corners = np.int0(corners)
    # for i in corners:
    #     x,y = i.ravel()
    #     cv.circle(img2,(x,y),3,255,-1)
    # plt.imshow(img2),plt.show()

    # create BFMatcher object
    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
    # Match descriptors.
    matches = bf.match(des1, des2)
    # Sort them in the order of their distance.
    matches = sorted(matches, key=lambda x: x.distance)
    # # Remove not so good matches
    # numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
    # matches = matches[:numGoodMatches]

    imMatches = cv.drawMatches(img1, kps1, img2, kps2, matches, None)
    # cv.imwrite("matches.jpg", imMatches)

    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = kps1[match.queryIdx].pt
        points2[i, :] = kps2[match.trainIdx].pt

    # print("points1, ", (points1[0]))
    # print("points2, ", (points2[0]))

    h, mask = cv.findHomography(points1, points2, cv.RANSAC)

    # Use homography
    height, width, channels = img2.shape
    im1Reg = cv.warpPerspective(img1, h, (width, height))

    return im1Reg, h


if __name__ == "__main__":
    ref_image_link = "../images/514 RF.bmp"
    image_link = "../images/509 RF.bmp"
    im_reference = cv.imread(ref_image_link, cv.IMREAD_COLOR)
    im = cv.imread(image_link, cv.IMREAD_COLOR)
    im1Reg, h = get_homography(im_reference, im)
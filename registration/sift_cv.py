import cv2 as cv
import numpy as np
from matplotlib import pylab as plt

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


if __name__ == "__main__":
    ref_image_link = "../images/514 RF.bmp"
    image_link = "../images/509 RF.bmp"
    im_reference = cv.imread(ref_image_link, cv.IMREAD_COLOR)
    im = cv.imread(image_link, cv.IMREAD_COLOR)
    h = get_matching_points(im_reference, im)

print(cv.__version__)

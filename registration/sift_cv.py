import cv2 as cv
import numpy as np
from matplotlib import pylab as plt

MAX_MATCHES = 500
GOOD_MATCH_PERCENT = 0.15
MIN_MATCH_COUNT = 4


def get_homography(im1, im2):
    # Initiate SIFT detector
    sift = cv.SIFT_create()

    keypoints1, descriptors1 = sift.detectAndCompute(im1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(im2, None)

    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(descriptors1, descriptors2, k=2)

    good = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)

    if len(good) > MIN_MATCH_COUNT:
        src_pts = np.float32([keypoints1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)
        matchesMask = mask.ravel().tolist()
        h, w, d = im1.shape
        pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
        dst = cv.perspectiveTransform(pts, M)
        img2 = cv.polylines(im2, [np.int32(dst)], True, 255, 3, cv.LINE_AA)
    else:
        print("Not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT))
        matchesMask = None

    draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
                       singlePointColor=None,
                       matchesMask=matchesMask,  # draw only inliers
                       flags=2)
    img3 = cv.drawMatches(im1, keypoints1, im2, keypoints2, good, None, **draw_params)
    plt.imshow(img3, 'gray'), plt.show()

    # Find homography
    h, mask = cv.findHomography(pts, dst, cv.RANSAC)

    # Use homography
    height, width, channels = im2.shape
    im1Reg = cv.warpPerspective(im1, h, (width, height))

    return im1Reg, h


if __name__ == "__main__":
    print(cv.__version__)
    ref_image_link = "../images/514 RF.bmp"
    image_link = "../images/509 RF.bmp"
    im_reference = cv.imread(ref_image_link, cv.IMREAD_COLOR)
    print(im_reference.shape)
    im = cv.imread(image_link, cv.IMREAD_COLOR)
    # im1Reg, h = get_homography(im_reference, im)

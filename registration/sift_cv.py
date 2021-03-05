import cv2
import numpy as np
from matplotlib import pylab as plt

MAX_MATCHES = 500
GOOD_MATCH_PERCENT = 0.15
MIN_MATCH_COUNT = 4


def align_images(im1, im2):
    # # Convert images to grayscale
    # im1Gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    # im2Gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

    # Detect ORB features and compute descriptors.
    sift = cv2.SIFT_create()

    keypoints1, descriptors1 = sift.detectAndCompute(im1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(im2, None)

    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(descriptors1, descriptors2, k=2)

    good = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)

    if len(good) > MIN_MATCH_COUNT:
        src_pts = np.float32([keypoints1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        matchesMask = mask.ravel().tolist()
        h, w, d = im1.shape
        pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
        dst = cv2.perspectiveTransform(pts, M)
        img2 = cv2.polylines(im2, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
    else:
        print("Not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT))
        matchesMask = None

    draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
                       singlePointColor=None,
                       matchesMask=matchesMask,  # draw only inliers
                       flags=2)
    img3 = cv2.drawMatches(im1, keypoints1, im2, keypoints2, good, None, **draw_params)
    plt.imshow(img3, 'gray'), plt.show()

    # Find homography
    h, mask = cv2.findHomography(pts, dst, cv2.RANSAC)

    # Use homography
    height, width, channels = im2.shape
    im1Reg = cv2.warpPerspective(im1, h, (width, height))

    return im1Reg, h

# # reading image in grayscale
# img = cv2.imread("../images/514 RF.bmp", cv2.IMREAD_GRAYSCALE)
#
# # intializing web cam
# cap = cv2.VideoCapture(0)
# # creating the SIFT algorithm
# sift = cv2.xfeatures2d.SIFT_create()
#
# # find the keypoints and descriptors with SIFT
# kp_image, desc_image = sift.detectAndCompute(img, None)
#
# # intializing the dictionary
# index_params = dict(algorithm=0, trees=5)
# search_params = dict()
#
# # by using Flann Matcher
# flann = cv2.FlannBasedMatcher(index_params, search_params)
#
# # reading the frame
# # _, frame = cap.read()
# frame = cv2.imread("../images/515 RF.bmp")
#
# # converting the frame into grayscale
# grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
# # find the keypoints and descriptors with SIFT
# kp_grayframe, desc_grayframe = sift.detectAndCompute(grayframe, None)
#
# # finding nearest match with KNN algorithm
# matches = flann.knnMatch(desc_image, desc_grayframe, k=2)
#
# # initialize list to keep track of only good points
# good_points = []
#
# for m, n in matches:
#     # append the points according
#     # to distance of descriptors
#     if (m.distance < 0.6 * n.distance):
#         good_points.append(m)
#
#
# # maintaining list of index of descriptors
# # in query descriptors
# query_pts = np.float32([kp_image[m.queryIdx] .pt for m in good_points]).reshape(-1, 1, 2)
#
# # maintaining list of index of descriptors
# # in train descriptors
# train_pts = np.float32([kp_grayframe[m.trainIdx].pt for m in good_points]).reshape(-1, 1, 2)
#
# print(query_pts)
# print(train_pts)
#
# # finding perspective transformation
# # between two planes
# matrix, mask = cv2.findHomography(query_pts, train_pts, cv2.RANSAC, 5.0)
#
# # ravel function returns
# # contiguous flattened array
# matches_mask = mask.ravel().tolist()
# # initializing height and width of the image
# h, w = img.shape
#
# # saving all points in pts
# pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]) .reshape(-1, 1, 2)
#
# # applying perspective algorithm
# dst = cv2.perspectiveTransform(pts, matrix)
# # using drawing function for the frame
# homography = cv2.polylines(frame, [np.int32(dst)], True, (255, 0, 0), 3)
#
# # showing the final output
# # with homography
# cv2.imshow("Homography", homography)
# cv2.waitKey(0)

# import cv2
# import matplotlib.pyplot as plt

# print(cv2.__version__)

# reading image
# img1 = cv2.imread("../images/514 RF.bmp")
# gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

#keypoints
# sift = cv2.xfeatures2d.SIFT_create()
# keypoints_1, descriptors_1 = sift.detectAndCompute(img1,None)

# img_1 = cv2.drawKeypoints(gray1,keypoints_1,img1)
# plt.imshow(img_1)
# cv2.waitKey(0)

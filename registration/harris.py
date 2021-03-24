import numpy as np
import cv2 as cv
from imutils import paths
import argparse
import imutils


def harris_corner_detection(img):
    # file_name = '../images/514 RF.bmp'
    # img = cv.imread(image_link)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv.cornerHarris(gray, 9, 3, 0.06)

    #result is dilated for marking the corners, not important
    dst = cv.dilate(dst, None)

    # Threshold for an optimal value, it may vary depending on the image.
    img[dst > 0.01 * dst.max()] = [0, 0, 255]


    h, w, c = img.shape
    points = []
    for i in range(h - 1):
        for j in range(w - 1):
            if img[i][j][0] == [0] and img[i][j][1] == [0] and img[i][j][2] == [255]:
                points.append([i, j])
    final = [points, ]
    return final


# def image_stitching():
#
#     # construct the argument parser and parse the arguments
#     # ap = argparse.ArgumentParser()
#     # ap.add_argument("-i", "--images", type=str, required=True,
#     #                 help="path to input directory of images to stitch")
#     # ap.add_argument("-o", "--output", type=str, required=True,
#     #                 help="path to the output image")
#     # args = vars(ap.parse_args())
#     # grab the paths to the input images and initialize our images list
#     print("[INFO] loading images...")
#     imagePaths = sorted(["../images/514 RF.bmp", "../images/509 RF.bmp"])
#     images = []
#     # loop over the image paths, load each one, and add them to our
#     # images to stitch list
#     for imagePath in imagePaths:
#         image = cv.imread(imagePath)
#         images.append(image)
#     # initialize OpenCV's image stitcher object and then perform the image
#     # stitching
#     print("[INFO] stitching images...")
#     # stitcher = cv.Stitcher_create()
#     stitcher = cv.createStitcher(True) if imutils.is_cv3() else cv.Stitcher_create(True)
#     (status, stitched) = stitcher.stitch(images)
#     # if the status is '0', then OpenCV successfully performed image
#     # stitching
#     if status == 0:
#         # write the output stitched image to disk
#         cv.imwrite("stitched.png", stitched)
#         # display the output stitched image to our screen
#         cv.imshow("Stitched", stitched)
#         cv.waitKey(0)
#     # otherwise the stitching failed, likely due to not enough keypoints)
#     # being detected
#     else:
#         print("[INFO] image stitching failed ({})".format(status))
#
#
# # points = harris_corner_detection()
# if __name__ == '__main__':
#     image_stitching()

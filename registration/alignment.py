from __future__ import print_function
import cv2 as cv
import numpy as np
from matplotlib import pylab as plt
import os
import glob
from registration import akaze
from registration import orb
from registration import sift_cv
from registration import good_features_orb
from registration import surf_cv

MAX_MATCHES = 1000
GOOD_MATCH_PERCENT = 0.2


def try_():
    source = np.array([[0, 0], [100, 0], [100, 100], [0, 100]])
    dest = np.array([[0, 0], [-1000, 0], [-1000, -1000], [0, -1000]])
    points = np.float32([[[50, 50]]])
    homography, _ = cv.findHomography(source, dest)
    # print(source.shape)
    # print(homography.shape)
    # print(homography)
    # print(type(homography))
    # print(type(homography[0, 0]))
    transformed = cv.perspectiveTransform(points, homography)
    # print(transformed)
    # => [[[-500. -500.]]]
    homography_inverse = np.linalg.inv(homography)
    detransformed = cv.perspectiveTransform(transformed, homography_inverse)
    # print(detransformed)
    # => [[[50. 50.]]]


def find_points(points, homography):
    try:
        # print(points.shape)
        # print(homography.shape)
        # homography_inverse = np.linalg.inv(homography)
        transformed = cv.perspectiveTransform(points, homography)
        # print(transformed)
    except Exception as e:
        print(e)

        print("fail")
    return transformed


def get_points(ref_image_link, image_link, ref_image_points):

    # print("Reading reference image : ", ref_image_link)
    im_reference = cv.imread(ref_image_link, cv.IMREAD_COLOR)

    # print("Reading image to align : ", image_link)
    im = cv.imread(image_link, cv.IMREAD_COLOR)

    # print("Aligning images ...")
    # Registered image will be resotred in imReg.
    # The estimated homography will be stored in h.

    points1, points2 = orb.get_matching_points(im_reference, im)
    # imReg, homography = orb.get_homography_harris(ref_image_link, image_link)

    # Find homography
    homography, mask = cv.findHomography(points1, points2, cv.RANSAC)

    transformed_points = find_points(ref_image_points, homography)
    # # Write aligned image to disk.
    # outFilename = "aligned.jpg"
    # print("Saving aligned image : ", outFilename)
    # cv.imwrite(outFilename, imReg)

    # Print estimated homography
    # print("Estimated homography : \n", homography)
    print(transformed_points)
    return transformed_points


def sow_points_on_image(fig_num, image, image_path, points):
    # print(points)
    plt.figure(fig_num).clf()
    plt.title(image_path)
    plt.imshow(image)
    labels = set()
    plt.plot(points[0, :, 0], points[0, :, 1], 'ro', color='r', markersize=4)


def run_test():
    image_list = glob.glob(os.path.join("../514 images", '*.bmp'))
    for i, image_path in enumerate(image_list):
        image = plt.imread(image_path)
        transformed = get_points(i, image_path)
        sow_points_on_image(i, image, image_path, transformed)
    plt.show(block=True)

    # image_path = '../514 images/514 RF flip.bmp'
    # image = plt.imread(image_path)
    # transformed = main(0, image_path)
    # sow_points_on_image(0, image, image_path, transformed)
    # plt.show(block=True)


if __name__ == '__main__':
    # Read reference image
    refFilename = "../images/514 RF.bmp"
    Filename = "../images/509 RF.bmp"
    # print("Reading reference image : ", refFilename)
    im1 = cv.imread(Filename, cv.IMREAD_COLOR)
    im2= np.array(im1)


    # Read image to be aligned
    #main("../514 images/514 RF.bmp")
    # try_()
    # po = np.float64([[[215.,  36.], [44., 153.], [19., 225.], [55., 270.], [105., 303.]]])
    # print("1: \n", po[0])
    # print("2: \n", po[0, :, 0])
    # print("3: \n", po[0, :, 1])
    # run_test()
    x=get_points(refFilename, Filename, np.float64([[[470, 276], [452, 146], [386, 90], [320, 114], [280, 134], [230, 130], [216, 230], [262, 310], [342, 316]]]))
    print("______________________")
    print(x)
    for i in x[0]:
        print(i,"i")
        cv.circle(im2,(int(i[1]),int(i[0])), 2, (255,0,0), 1)
    cv.imshow("im",im2)
    cv.waitKey(0)
    #plt.imshow(im2)

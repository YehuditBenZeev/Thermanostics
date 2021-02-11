from __future__ import print_function
import cv2
import numpy as np
from matplotlib import pylab as plt
import os
import glob
import akaze

MAX_MATCHES = 1000
GOOD_MATCH_PERCENT = 0.2


def try_():
    source = np.array([[0, 0], [100, 0], [100, 100], [0, 100]])
    dest = np.array([[0, 0], [-1000, 0], [-1000, -1000], [0, -1000]])
    points = np.float32([[[50, 50]]])
    homography, _ = cv2.findHomography(source, dest)
    print(source.shape)
    print(homography.shape)
    print(homography)
    print(type(homography))
    print(type(homography[0, 0]))
    transformed = cv2.perspectiveTransform(points, homography)
    print(transformed)
    # => [[[-500. -500.]]]
    homography_inverse = np.linalg.inv(homography)
    detransformed = cv2.perspectiveTransform(transformed, homography_inverse)
    print(detransformed)
    # => [[[50. 50.]]]


def find_points(points, homography):
    try:
        print(points.shape)
        print(homography.shape)
        # homography_inverse = np.linalg.inv(homography)
        transformed = cv2.perspectiveTransform(points, homography)
        print(transformed)
    except Exception as e:
        print(e)

        print("fail")
    return transformed


def get_points(pic_number, image_link):
    ref_image_link = ''
    if 'RF' in image_link:
        ref_image_link = "../images/514 RF.bmp"
    elif 'RB' in image_link:
        ref_image_link = "../images/514 RB.bmp"
    if 'LF' in image_link:
        ref_image_link = "../images/514 LF.bmp"
    if 'LB' in image_link:
        ref_image_link = "../images/514 LB.bmp"

    print("Reading reference image : ", ref_image_link)
    imReference = cv2.imread(ref_image_link, cv2.IMREAD_COLOR)
    print("Reading image to align : ", image_link)
    im = cv2.imread(image_link, cv2.IMREAD_COLOR)

    print("Aligning images ...")
    # Registered image will be resotred in imReg.
    # The estimated homography will be stored in h.
    imReg, homography = akaze.align_images(imReference, im)

    points = np.float64([[[215, 36], [44, 153], [19, 225], [55, 270], [105, 303]]])
    transformed = find_points(points, homography)
    # Write aligned image to disk.
    outFilename = "aligned.jpg"
    print("Saving aligned image : ", outFilename)
    cv2.imwrite(outFilename, imReg)

    # Print estimated homography
    print("Estimated homography : \n", homography)
    return transformed


def sow_points_on_image(fig_num, image, image_path, points):
    print(points)
    plt.figure(fig_num).clf()
    plt.title(image_path)
    plt.imshow(image)
    labels = set()
    plt.plot(points[0, :, 0], points[0, :, 1], 'ro', color='r', markersize=4)


def run_test():
    image_list = glob.glob(os.path.join("../514 images", '*.bmp'))
    for i, image_path in enumerate(image_list):
        image = plt.imread(image_path)
        transformed = main(i, image_path)
        sow_points_on_image(i, image, image_path, transformed)
    plt.show(block=True)

    # image_path = '../514 images/514 RF flip.bmp'
    # image = plt.imread(image_path)
    # transformed = main(0, image_path)
    # sow_points_on_image(0, image, image_path, transformed)
    # plt.show(block=True)


if __name__ == '__main__':
    # Read reference image
    # refFilename = "../images/514 RF.bmp"
    # print("Reading reference image : ", refFilename)
    # imReference = cv2.imread(refFilename, cv2.IMREAD_COLOR)

    # Read image to be aligned
    #main("../514 images/514 RF.bmp")
    # try_()
    # po = np.float64([[[215.,  36.], [44., 153.], [19., 225.], [55., 270.], [105., 303.]]])
    # print("1: \n", po[0])
    # print("2: \n", po[0, :, 0])
    # print("3: \n", po[0, :, 1])
    run_test()

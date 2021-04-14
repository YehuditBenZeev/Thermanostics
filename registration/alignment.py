from __future__ import print_function
import cv2 as cv
import numpy as np
from matplotlib import pylab as plt
import os
import glob
from customized_exceptions.customized_exceptions import PointLengthError, HomographyError

MAX_MATCHES = 1000
GOOD_MATCH_PERCENT = 0.2


def try_():
    source = np.array([[0, 0], [100, 0], [100, 100], [0, 100]])
    dest = np.array([[0, 0], [-1000, 0], [-1000, -1000], [0, -1000]])
    points = np.float32([[[50, 50]]])
    homography, _ = cv.findHomography(source, dest)

    transformed = cv.perspectiveTransform(points, homography)

    homography_inverse = np.linalg.inv(homography)
    detransformed = cv.perspectiveTransform(transformed, homography_inverse)


def find_points(points, homography):
    try:
        transformed = cv.perspectiveTransform(points, homography)
    except Exception as e:
        raise HomographyError()

    return transformed


def get_points(ref_image_link, image_link, ref_image_points, matching_points, matcher):
    im_reference = cv.imread(ref_image_link, cv.IMREAD_COLOR)

    im = cv.imread(image_link, cv.IMREAD_COLOR)

    points1, points2 = matching_points(im_reference, im, matcher)

    if len(points1) < 4 or len(points2) < 4:
        raise PointLengthError("not enough points to find homography")

    # Find homography
    homography, mask = cv.findHomography(points1, points2, cv.RANSAC)

    if homography is None:
        raise HomographyError()

    transformed_points = find_points(ref_image_points, homography)

    return transformed_points


def show_points_on_image(fig_num, image, image_path, points):
    plt.figure(fig_num).clf()
    plt.title(image_path)
    plt.imshow(image)
    plt.plot(points[0, :, 0], points[0, :, 1], 'ro', color='r', markersize=4)


def run_test():
    image_list = glob.glob(os.path.join("../514 images", '*.bmp'))
    for i, image_path in enumerate(image_list):
        image = plt.imread(image_path)
        transformed = get_points(i, image_path)
        show_points_on_image(i, image, image_path, transformed)
    plt.show(block=True)

    # image_path = '../514 images/514 RF flip.bmp'
    # image = plt.imread(image_path)
    # transformed = main(0, image_path)
    # show_points_on_image(0, image, image_path, transformed)
    # plt.show(block=True)


if __name__ == '__main__':
    run_test()

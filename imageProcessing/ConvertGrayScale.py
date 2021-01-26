import cv2
import imutils
import numpy as np
import argparse
from PIL import Image, ImageOps
from matplotlib import pylab as plt
from skimage.feature import peak_local_max

# Displaying an image
from scipy import ndimage
import scipy.ndimage.filters as filters


def show_pic(image, name):
    window_name = name
    cv2.imshow(window_name, image)
    cv2.waitKey(0)


def edge_detecting(image, noise, intensity):
    # image = cv2.imread(image_path)
    image_b_w = cv2.Canny(image, noise, intensity)  # was 350 , 500 used in Palm
    return image_b_w


def detect_top_bottom_wrist_points(b_w_image):
    height, width = b_w_image.shape

    top_wrist = 0
    bottom_wrist = 0

    for i in range(10, height - 1):
        if b_w_image[i][width - 2] != 0:
            top_wrist = i
            break
    for i in range(10, height - 1):
        if b_w_image[height - i][width - 2] != 0:
            bottom_wrist = height - i
            break

    print("top_wrist , bottom_wrist", top_wrist, bottom_wrist)

    return top_wrist, bottom_wrist


def black_background(image):
    mask = edge_detecting(image, 300, 10)

    mask[1:5, :] = 0
    mask[-2:, :] = 0
    mask[:, 1:5] = 0

    rows, columns, a = image.shape
    print(rows, " ",  columns, " ", a)
    for j in range(1, rows - 1):
        for i in range(1, columns - 1):
            if mask[j][i] != 0:
                image[j][i] = 0

                # mask[j][i] = 0
    show_pic(mask, "mask")
    show_pic(image, "mask")


def hp_filter(img, kernel=np.array([[-1]*3, [-1, 8, -1], [-1]*3])/9):
    hpf_arr = ndimage.convolve(img, kernel)
    return hpf_arr


def lp_filter(img, kernel=np.array([[1] * 3, [1] * 3, [1] * 3])/9):
    lpf_arr = ndimage.convolve(img, kernel)
    return lpf_arr


def local_max(data, size):
    return filters.maximum_filter(data, size=size)


def max_points(img):
    points = peak_local_max(img)
    point_x = []
    point_y = []
    for i, j in points:
        point_x.append(j)
        point_y.append(i)

    return point_x, point_y


def local_min(data, size):
    return filters.minimum_filter(data, size=size)


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


def edge(path):
    img = plt.imread(path)
    gray = rgb2gray(img)
    print(gray.shape)

    plt.figure()

    a = plt.subplot(2, 3, 1)
    plt.title("gray")
    plt.imshow(gray, cmap=plt.get_cmap('gray'))

    hp_filtered_img = hp_filter(gray)
    max_img = local_max(hp_filtered_img, 15)
    plt.subplot(2, 3, 2, sharex=a, sharey=a)
    plt.title("hp_filtered_img")
    plt.imshow(hp_filtered_img, cmap=plt.get_cmap('gray'))

    hp_threshold_image = hp_filtered_img
    mean_value = hp_threshold_image.mean()
    hp_threshold_image[hp_threshold_image <= mean_value] = 0
    hp_threshold_image[hp_threshold_image > mean_value] = 255
    plt.subplot(2, 3, 3, sharex=a, sharey=a)
    plt.title("threshold_image hp")
    plt.imshow(hp_threshold_image, cmap=plt.get_cmap('gray'))

    lp_filtered_image = lp_filter(gray)
    plt.subplot(2, 3, 4, sharex=a, sharey=a)
    plt.title("lp_filtered_image")
    plt.imshow(lp_filtered_image, cmap=plt.get_cmap('gray'))

    hp_filtered_img_2 = hp_filter(gray)
    plt.subplot(2, 3, 5, sharex=a, sharey=a)
    plt.title("hp_filtered_img_2")
    plt.imshow(hp_filtered_img_2, cmap=plt.get_cmap('gray'))

    hp_threshold_image_2 = hp_filtered_img
    mean_value = hp_threshold_image_2.mean()
    print(mean_value)
    hp_threshold_image_2[hp_filtered_img <= 150] = 0
    hp_threshold_image_2[hp_filtered_img > 150] = 255

    lp_threshold = lp_filter(hp_filtered_img_2,  np.array([[1] * 9, [1] * 9, [1] * 9, [1] * 9, [1] * 9, [1] * 9, [1] * 9, [1] * 9, [1] * 9])/81)

    points_x, points_y = max_points(hp_threshold_image_2)
    h, w = hp_threshold_image_2.shape

    print(len(points_x))
    edge_image = np.ones((h, w), dtype=int)*250
    for i in range(len(points_x)):
        edge_image[points_y[i]][points_x[i]] = 0

    print(type(hp_threshold_image))
    image_b_w = cv2.Canny(np.uint8(lp_filtered_image), 50, 150)
    plt.subplot(2, 3, 6, sharex=a, sharey=a)
    plt.title("image_b_w")
    plt.imshow(image_b_w, cmap=plt.get_cmap('gray'))

    plt.show(block=True)
    # h, w, c = img.shape
    # new_image = np.ones((h, w), dtype=int) * 250
    #
    # for i in range(len(light_dots_x)):
    #     new_image[light_dots_y[i]][light_dots_x[i]] = 0
    #
    # # plt.show(block=True)
    # a = plt.subplot(1, 3, 1)
    # plt.imshow(light_img)
    # # plt.subplot(1, 3, 2, sharex=a, sharey=a)
    # # plt.imshow(new_image)
    #
    # filtered_light_img = hpf_2(new_image)
    # max_light_image = local_max(filtered_light_img, 25)
    # print(type(filtered_light_img))
    # plt.subplot(1, 3, 2, sharex=a, sharey=a)
    # plt.imshow(max_light_image)
    #
    # mean_im = max_light_image.mean()
    # print(mean_im)
    # # min_convolve = lpf(max_light_image)
    # # min_light_image_1 = local_max(min_convolve, 20)
    # threshold_image = max_light_image
    # threshold_image[threshold_image <= 180] = 0
    # threshold_image[threshold_image > 180] = 255
    # plt.subplot(1, 3, 3, sharex=a, sharey=a)
    # plt.imshow(threshold_image)
    # plt.show(block=True)
    # get_center_points(threshold_image)
    # # max = max_light_image/255
    # # print(max.max())
    # # im = Image.fromarray(np.uint8(cm.gist_earth(max_light_image) * 255))
    # # plt.subplot(1, 3, 3, sharex=a, sharey=a)
    # # plt.imshow(filtered_light_img)
    # # plt.show(block=True)
    # # board = max_light_image.filter(ImageFilter.FIND_EDGES)


class ImageProcessing:

    def __init__(self, image_path):
        # self.image_path = image_path
        self.image = cv2.imread(image_path)
        self.name = image_path

    def black_border(self):
        # self.image = self.image[:, :, 1]  # green layer
        # mask = self.image

        border = cv2.bilateralFilter(self.image, 11, 17, 17)
        mask = cv2.Canny(border, 350, 500)

        rows, columns = self.image.shape
        # show_pic(self.image, "edge")

        for j in range(1, rows - 1):
            for i in range(1, columns - 1):
                if mask[j][i] != 0:
                    self.image[j][i] = 0
                    mask[j][i] = 0
                else:
                    mask[j][i] = 255

        # show_pic(mask, "edge")
        # show_pic(self.image, "edge")
        mask = cv2.Canny(border, 350, 500)
        # show_pic(mask, "edge")

    def flip_image(self):
        h, w, c = self.image.shape
        # calculate the center of the image
        center = (w / 2, h / 2)



        angle = 180

        scale = 1.0

        # Perform the counter clockwise rotation holding at the center
        # 90 degrees
        M = cv2.getRotationMatrix2D(center, angle, scale)
        rotated = cv2.warpAffine(self.image, M, (w, h))
        show_pic(rotated, "rotated")

    # convert image to gray scale
    def convert_image_to_gray_scale(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        show_pic(gray, "gray")

        if ("LF." in self.name) or ("RB." in self.name):
            self.flip_image()


        b_w_image = edge_detecting(gray, 100, 200)
        show_pic(b_w_image, "edge")

        print(self.image.shape)

        height, width = gray.shape

        for i in range(1, height - 1):
            for j in range(1, width - 1):
                if not(b_w_image[i][j] == 0):
                    break
                gray[i][j] = 0

        top_wrist, bottom_wrist = detect_top_bottom_wrist_points(b_w_image)
        for j in range(1, width - 1):
            if (j < top_wrist) or (j > bottom_wrist):
                for i in range(1, height - 1):
                    if b_w_image[height - i][width - j] != 0:
                        self.image[height - i][width - j] = 0
                        break

        show_pic(gray, "image")

        # show_pic(self.image)

        # zeroing first & last column
        self.image[:, :1] = 0
        self.image[:, -1:] = 0

        # zeroing first & last column
        self.image[:1, :] = 0
        self.image[-1:, :] = 0

        # print(self.image)
        # show_pic(edge_detecting(self.image, 350, 500), "***")
        # print(self.image[269:270])

        # return self.image

    # Blackens the background better
    def convert_gray_scale(self):
        print("81")
        self.image = self.image[:, :, 1]  # green layer
        b_w_image = edge_detecting(self.image, 100, 50)
        # show_pic(b_w_image, "b_w_image")
        height, width = self.image.shape
        top_wrist, bottom_wrist = detect_top_bottom_wrist_points(b_w_image)

        '''for i in range(1, height - 1):
            if b_w_image[i][width - 2] != 0:
                top_wrist = i
                break
        for i in range(1, height - 1):
            if b_w_image[height - i][width - 2] != 0:
                bottom_wrist = height - i
                break

        print("top_wrist , bottom_wrist", top_wrist, bottom_wrist)'''

        for i in range(1, height - 1):
            for j in range(1, width - 1):
                if b_w_image[i][j] == 0:
                    self.image[i][j] = 0
                else:
                    break

        for i in range(1, height - 1):
            if (i < top_wrist) or (i > bottom_wrist):
                for j in range(1, width - 1):
                    if b_w_image[height - i][width - j] == 0:
                        self.image[height - i][width - j] = 0
                    else:
                        break

        show_pic(self.image, "done")
        b_w_image = edge_detecting(self.image, 100, 50)

        return self.image

    ''' b_w_image = edge_detecting(self.image , 350, 500)
        show_pic(b_w_image ,"b_w_image")

        for i in range(1, height - 1):
            for j in range(1, width - 1):
                if b_w_image[i][j] != 0:
                    self.image[i][j] = 0
                    break

        for i in range(1, height - 1):
            if ( i < top_wrist ) or ( i > bottom_wrist ):
                for j in range(1, width - 1):
                    if b_w_image[height - i][width - j] != 0:
                        self.image[height - i][width - j] = 0
                        break
                        '''


def detect_most_left_border_point(b_w_image):
    rows, columns = b_w_image.shape
    show_pic(b_w_image, "detect_most_left_border_point")

    for i in range(0, columns - 1):
        for j in range(0, rows - 1):
            if (b_w_image[j][i] == 0) and (b_w_image[j][i + 1] != 0):
                p = np.array(b_w_image)
                cv2.circle(p, (i, j), 4, (255, 0, 0), 2)
                show_pic(p, "point")
                return i, j


def rotate_image(rotate_img):
    black_white_image = edge_detecting(rotate_img, 300, 10)
    show_pic(black_white_image, "black_white_image")
    top_wrist, bottom_wrist = detect_top_bottom_wrist_points(black_white_image)

    # show_pic(rotate_img, "rotate_img")
    # show_pic(black_white_image, "black_white_image")

    rows, columns = rotate_img.shape

    print("rows, columns", rows, columns)

    mid_wrist = int((bottom_wrist - top_wrist) / 2) + top_wrist

    left_point_x, left_point_y = detect_most_left_border_point(black_white_image)
    print("mid_wrist , left_point_x: ", mid_wrist, left_point_x)

    '''for angle in np.arange(0, 360, 10):
        aaa = imutils.rotate(rotate_img, angle)
    rotate_img = aaa
    show_pic(aaa, "aaa")
    show_pic(rotate_img, "rotate_img")
    for angle in np.arange(0, 360, 10):
        aaa = imutils.rotate(rotate_img, angle)
    rotate_img = aaa
    show_pic(aaa, "aaa")
    show_pic(rotate_img, "rotate_img")'''

    '''while abs(mid_wrist - left_point_x) > 6:
        print("mid_wrist , left_point_x: ", mid_wrist, left_point_x)
        left_point_x, left_point_y = detect_most_left_border_point(black_white_image)
        for angle in np.arange(0, 360, 4):
            rotate_img = imutils.rotate(rotate_img, angle)
        show_pic(rotate_img, "rotate")

    show_pic(aaa, "done to rotate")'''


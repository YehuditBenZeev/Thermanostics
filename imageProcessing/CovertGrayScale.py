import cv2
import imutils
import numpy as np
import argparse
from PIL import Image


# Displaying an image
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

    for i in range(1, height - 1):
        if b_w_image[i][width - 2] != 0:
            top_wrist = i
            break
    for i in range(1, height - 1):
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


class ImageProcessing:

    def __init__(self, image_path):
        # self.image_path = image_path
        self.image = cv2.imread(image_path)

    def black_border(self):
        self.image = self.image[:, :, 1]  # green layer
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

    # convert image to gray scale
    def convert_image_to_gray_scale(self):
        self.image = self.image[:, :, 1]  # green layer
        # show_pic(self.image, "image")
        # print(self.image)
        # print(self.image.shape)
        self.image = cv2.bilateralFilter(self.image, 11, 17, 17)
        # show_pic(self.image, "image")

        # print(self.image.shape)

        height, width = self.image.shape

        for i in range(1, height - 1):
            for j in range(1, width - 1):
                if (self.image[i][j] < 20) and ((self.image[i+1][j+1] < 10) and (self.image[i-1][j-1] < 10)):
                    self.image[i][j] = 0

        # show_pic(self.image, "image")

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

        return self.image

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
        for angle in np.arange(0, 360, 6):
            aaa = imutils.rotate(rotate_img, angle)
        rotate_img = aaa
        show_pic(rotate_img, "rotate")

    show_pic(aaa, "done to rotate")'''


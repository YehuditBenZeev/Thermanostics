import numpy as np
import imutils
import cv2


def rotate_image(out_file_name, rotate_img, angle):
    print('in')
    # for angle in np.arange(0, 360, 10):
    rotate_img = imutils.rotate(rotate_img, angle)
    print('during')
    show_pic(rotate_img, "rotate_img")
    print('after')
    out_file_name += ' rotate ' + str(angle) + '.bmp'
    cv2.imwrite(out_file_name, rotate_img)


def show_pic(image, name):
    window_name = name
    cv2.imshow(window_name, image)
    cv2.waitKey(0)


if __name__ == '__main__':
    image_link = "../images/514 RF.bmp"
    out_file = '../514 images/514 RF'
    image = cv2.imread(image_link, cv2.IMREAD_COLOR)
    show_pic(image, 'before')
    rotate_image(out_file, image, 25)

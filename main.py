
from imageProcessing import ConvertGrayScale,  Palm as Pn, SortHotPointInArea as Sort

import cv2
import numpy as np

####################################################
# ------------ class  Image_Processing ------------------#
# link = "516 LF.bmp"
link = "images/a 041220 after LB.bmp"
ConvertGrayScale.edge(link)
# image = cv2.imread(link)
# print(image.shape)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# CovertGrayScale.show_pic(gray, "gray")
# iii = CovertGrayScale.edge_detecting(gray, 300, 10)
# CovertGrayScale.show_pic(gray, "gray")

# image = CovertGrayScale.black_background(image)
# CovertGrayScale.show_pic(gray, "gray")

# image = CovertGrayScale.rotate_image(gray)
# # CovertGrayScale.show_pic(image, "main")
# a = CovertGrayScale.ImageProcessing(link)
# # a = Image_Processing(link)
# # a.black_border()
# image = a.convert_image_to_gray_scale()
# # image = a.convert_gray_scale()
# # ######################################################
# # CovertGrayScale.rotate_image(gray)

# ## class  Hot_Spot ###
# aa = np.array(image)
# cv2.circle(aa, (50, 350), 4, (255, 0, 0), 2)
# ImageProcessing.show_pic(aa, "**************")
#
# b = Pn.Palm(image, link)
# # b.find_max_for_palm()
# # b.try_detect()
# b.detect_fingers()
# b.draw_on_point()
# b.detect_palm_points()

# s = Sort.SortHotPointInArea(image, link, 20)
# s.Area0()
# s.Area1()
# s.Arae2()
# s.Arae3()
# s.Arae4()
# s.Arae5()

# im = cv2.imread(link)
#
# # smooth the image with alternative closing and opening
# # with an enlarging kernel
# morph = im.copy()
#
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
# morph = cv2.morphologyEx(morph, cv2.MORPH_CLOSE, kernel)
# morph = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel)
#
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
#
# # take morphological gradient
# gradient_image = cv2.morphologyEx(morph, cv2.MORPH_GRADIENT, kernel)
#
# # split the gradient image into channels
# image_channels = np.split(np.asarray(gradient_image), 3, axis=2)
#
# channel_height, channel_width, _ = image_channels[0].shape
#
# # apply Otsu threshold to each channel
# for i in range(0, 3):
#     _, image_channels[i] = cv2.threshold(~image_channels[i], 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
#     image_channels[i] = np.reshape(image_channels[i], newshape=(channel_height, channel_width, 1))
#
# # merge the channels
# image_channels = np.concatenate((image_channels[0], image_channels[1], image_channels[2]), axis=2)
#
# # save the denoised image
# CovertGrayScale.show_pic(image_channels, "pic")

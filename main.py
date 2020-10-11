from imageProcessing import CovertGrayScale, Palm as Pn

####################################################
# ------------ class  Image_Processing ------------------#
link = 'Im1.jpg'
a = CovertGrayScale.ImageProcessing(link)
# a = Image_Processing(link)
# a.black_border()
# image = a.convert_image_to_gray_scale()
image = a.convert_gray_scale()
#######################################################
# --------------- class  Hot_Spot ------------- #
# aa = np.array(image)
# cv2.circle(aa, (50, 350), 4, (255, 0, 0), 2)
# ImageProcessing.show_pic(aa, "**************")

b = Pn.Palm(image, link)
# b.find_max_for_palm()
# b.try_detect()
b.detect_fingers()
#b.detect_palm_points()

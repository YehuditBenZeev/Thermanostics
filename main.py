from imageProcessing import CovertGrayScale, Palm as Pn ,SortHotPointInArea as Sort

####################################################
# ------------ class  Image_Processing ------------------#
link = 'Im1.jpg'
# image = cv2.imread(link)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# CovertGrayScale.show_pic(gray, "gray")
# iii = CovertGrayScale.edge_detecting(gray, 300, 10)
# CovertGrayScale.show_pic(gray, "gray")

# image = CovertGrayScale.black_background(image)
# CovertGrayScale.show_pic(gray, "gray")

# image = CovertGrayScale.rotate_image(gray)
# CovertGrayScale.show_pic(image, "main")
a = CovertGrayScale.ImageProcessing(link)
# a = Image_Processing(link)
# a.black_border()
image = a.convert_image_to_gray_scale()
# image = a.convert_gray_scale()
# ######################################################
# CovertGrayScale.rotate_image(gray)

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

s = Sort.SortHotPointInArea(image, link, 20)
# s.Area0()
s.Area1()
s.Arae2()
s.Arae3()
s.Arae4()
s.Arae5()

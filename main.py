from imageProcessing import CovertGrayScale, Palm as Pn ,Rotation as R,DivisionPalmArea as d

####################################################
# ------------ class  Image_Processing ------------------#
link = 'Im1.jpg'
a = CovertGrayScale.ImageProcessing(link)
# a = Image_Processing(link)
# a.black_border()
# image = a.convert_image_to_gray_scale()
image = a.convert_gray_scale()
#######################################################
### class  Hot_Spot ###
#aa = np.array(image)
#cv2.circle(aa, (50, 350), 4, (255, 0, 0), 2)
#ImageProcessing.show_pic(aa, "**************")
#do=d.DivisionPalmArea(image,link)
ro=R.Rotation(image,link)
# do.FindFinger1()
# do.FindFinger2()
# do.FindFinger3()
# do.FindFinger4()
# do.FindFinger5()
# do.FindArea0()
# s=sort.SortHotPointInArea(image,link,20)
# #s.Area0()
# s.Area1()
# s.Arae2()
# s.Arae3()
# s.Arae4()
# s.Arae5()

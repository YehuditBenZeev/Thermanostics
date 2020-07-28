import Palm as p
import Image_Processing
####################################################
### class  Image_Processing ###
link = 'Im1.jpg'
a = Image_Processing.Image_Processing(link)
#a = Image_Processing(link)
#a.black_border()
im = a.convert_image_to_gray_scale()

#######################################################
### class  Hot_Spot ###

b= p.Palm(im , link)
#b.find_max_for_palm()
b.detect_fingers()
import Palm as p
import ImageProcessing
####################################################
### class  Image_Processing ###
link = 'Im1.jpg'
a = ImageProcessing.ImageProcessing(link)
#a = Image_Processing(link)
#a.black_border()
#image = a.convert_image_to_gray_scale()
image = a.convert_gray_scale()
#######################################################
### class  Hot_Spot ###

b= p.Palm(image , link)
#b.find_max_for_palm()
#b.try_detect()
b.detect_fingers()
b.try_detect()
#print(b.binary_search(638))
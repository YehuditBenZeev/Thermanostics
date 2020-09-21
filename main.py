import Palm as P
import ImageProcessing
import DivisionPalmArea as D
import SortHotPointInArea as S
import FindingHotspotsInPicture as F


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
#aa = np.array(image)
#cv2.circle(aa, (50, 350), 4, (255, 0, 0), 2)
#ImageProcessing.show_pic(aa, "**************")

b = P.Palm(image, link)
#b.find_max_for_palm()
#b.try_detect()
#b.detect_fingers()
#b.try_detect()
#print(b.binary_search(638))
# div = D.DivisionPalmArea(image, link)
# div.FindFinger1()
# div.FindFinger2()
# div.FindFinger3()
# div.FindFinger4()
# div.FindFinger5()
# f=F.FindingHotspotsInPicture(image,link)
# f.passOnImage(15)

sort=S.SortHotPointInArea(image,link,15)
sort.Area1()
sort.Arae2()
sort.Arae3()
sort.Arae4()
sort.Arae5()

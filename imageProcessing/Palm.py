import cv2
from imageProcessing import ConvertGrayScale as Ip, Finger as Fn


def inclination_between_two_points(temp, k, l):
    y = temp[0] - k
    x = temp[1] - l
    if y == 0 or x == 0:
        return 0
    inclination = y / x
    return inclination


# finds the distance between two points
def distance(point1, point2):
    x = point1[1] - point2[1]
    y = point1[0] - point2[0]

    point_distance = (x**2 + y**2)**0.5
    return point_distance


def get_bw_image(path):
    bw_image = cv2.imread(path)
    bw_image = bw_image[:, :, 1]  # green layer
    return Ip.edge_detecting(bw_image, 100, 500)


# will detect hot spots
class Palm:

    def __init__(self, processed_image, path):
        self.image = processed_image
        self.black_white_image = get_bw_image(path)
        self.finger_width = 0
        self.border_points = self.find_border_point()
        self.finger1 = Fn.Finger()
        self.finger2 = Fn.Finger()
        self.finger3 = Fn.Finger()
        self.finger4 = Fn.Finger()
        self.finger5 = Fn.Finger()
        self.palm_base_top = np.array([0, 0])
        self.palm_base_bottom = np.array([0, 0])

    def find_border_point(self):
        # border_point = []
        # h, w = self.image.shape
        c = Ip.edge_detecting(self.image, 500, 500)
        # aa = np.array(self.image)

        ret, thresh = cv2.threshold(c, 127, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, 1, 2)
        # print (contours)
        aa = np.array(self.image)

        for x in contours:
            for p in x:
                for m in p:
                    i = m[0]
                    j = m[1]
                    cv2.circle(aa, (i, j), 4, (255, 128, 0), 2)
        #Ip.show_pic(aa, "border")
        '''  for i in range(1, h - 1):
            for j in range(1, w - 1):
                if c[i][j] != 0:
                    # print(image[i][j])
                    number_tuple = (i, j)
                    border_point.append(number_tuple)
                    aa = np.array(self.image)
                    cv2.circle(aa, (j, i), 4, (255, 0, 0), 2)
                    ip.show_pic(aa, "border")'''

        #  border_point.sort()
        return aa

    # binary search in border_points
    def binary_search(self, val):
        start = 1
        end = len(self.border_points)
        middle = int((end - start)/2)
        print("81 - ", start, ",", middle, ",", end)
        while start <= end:
            # print("start, middle, end = " ,start,",", middle ,"," ,end)
            if self.border_points[middle][0] == val:
                return middle
            elif self.border_points[middle][0] > val:
                # print("54 , ",self.border_points[middle])
                end = middle
                middle = int((middle - start) / 2)
            else:  # self.border_points[middle] < val
                start = middle
                # print("end  , start = " , end , ", ", start)
                middle = int((end - middle) / 2)
        return -1

    def find_max_for_palm(self):  # -------------------------

        #Ip.show_pic(self.image, "image")

        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(self.image)
        print("101 - ", minVal, maxVal, minLoc, maxLoc)
        #  ss = self.image[maxLoc[0] -50:maxLoc[0]+50,maxLoc[1]-50:maxLoc[1]+50]
        # print("72")
        # show_pic(ss)
        cv2.circle(self.image, maxLoc, 20, (255, 0, 0), 2)
        #Ip.show_pic(self.image, "max circle")

    def central_of_palm(self):
        height, width = self.image.shape

        for i in range(0, height):
            for j in range(0, width):
                if (self.image[i][j] < 20) and ((self.image[i+1][j+1] < 10) and (self.image[i-1][j-1] < 10)):
                    self.image[i][j] = 0

    def draw_on_point(self):
        print("palm_base_top : top = ", self.palm_base_top[0], ",", self.palm_base_top[1])
        print("palm_base_bottom : top = ", self.palm_base_bottom[0], ",", self.palm_base_bottom[1])

        p = np.array(self.image)
        cv2.circle(p, (self.palm_base_top[0], self.palm_base_top[1]), 4, (255, 0, 0), 2)
        cv2.circle(p, (self.palm_base_bottom[0], self.palm_base_bottom[1]), 4, (255, 0, 0), 2)

        print("finger 1: top_1 = ", self.finger1.top_1[0], ",", self.finger1.top_1[1], "top_2 = ", self.finger1.top_2[0]
              , ",", self.finger1.top_2[1], "bottom_2 = ", self.finger1.bottom_2[0], ",", self.finger1.bottom_2[1])

        cv2.circle(p, (self.finger1.top_1[0], self.finger1.top_1[1]), 4, (255, 0, 0), 2)
        cv2.circle(p, (self.finger1.top_2[0], self.finger1.top_2[1]), 4, (255, 0, 0), 2)
        cv2.circle(p, (self.finger1.bottom_2[0], self.finger1.bottom_2[1]), 4, (255, 0, 0), 2)
        print("127 ", self.finger1.bottom_2[1], self.finger1.bottom_2[0])
        #Ip.show_pic(p, "finger1")

        cv2.circle(p, (self.finger2.top_1[0], self.finger2.top_1[1]), 4, (255, 0, 0), 2)
        cv2.circle(p, (self.finger2.top_2[0], self.finger2.top_2[1]), 4, (255, 0, 0), 2)
        cv2.circle(p, (self.finger2.bottom_2[0], self.finger2.bottom_2[1]), 4, (255, 0, 0), 2)
        print("finger 2: top_1 = ", self.finger2.top_1[0], ",", self.finger2.top_1[1], "top_2 = ", self.finger2.top_2[0]
              , ",", self.finger2.top_2[1], "bottom_2 = ", self.finger2.bottom_2[0], ",", self.finger2.bottom_2[1])
        #Ip.show_pic(p, "finger2")

        cv2.circle(p, (self.finger3.top_1[0], self.finger3.top_1[1]), 4, (255, 0, 0), 2)
        cv2.circle(p, (self.finger3.top_2[0], self.finger3.top_2[1]), 4, (255, 0, 0), 2)
        cv2.circle(p, (self.finger3.bottom_2[0], self.finger3.bottom_2[1]), 4, (255, 0, 0), 2)
        print("finger 3: top_1 = ", self.finger3.top_1[0], ",", self.finger3.top_1[1], "top_2 = ", self.finger3.top_2[0]
              , ",", self.finger3.top_2[1], "bottom_2 = ", self.finger3.bottom_2[0], ",", self.finger3.bottom_2[1])
        #Ip.show_pic(p, "finger3")

        cv2.circle(p, (self.finger4.top_1[0], self.finger4.top_1[1]), 4, (255, 0, 0), 2)
        cv2.circle(p, (self.finger4.top_2[0], self.finger4.top_2[1]), 4, (255, 0, 0), 2)
        cv2.circle(p, (self.finger4.bottom_2[0], self.finger4.bottom_2[1]), 4, (255, 0, 0), 2)
        print("finger 4: top_1 = ", self.finger4.top_1[0], ",", self.finger4.top_1[1], "top_2 = ", self.finger4.top_2[0]
              , ",", self.finger4.top_2[1], "bottom_2 = ", self.finger4.bottom_2[0], ",", self.finger4.bottom_2[1])
        #Ip.show_pic(p, "finger4")

        cv2.circle(p, (self.finger5.top_1[0], self.finger5.top_1[1]), 4, (255, 0, 0), 2)
        cv2.circle(p, (self.finger5.top_2[0], self.finger5.top_2[1]), 4, (255, 0, 0), 2)
        cv2.circle(p, (self.finger5.bottom_1[0], self.finger5.bottom_1[1]), 4, (255, 0, 0), 2)
        cv2.circle(p, (self.finger5.bottom_2[0], self.finger5.bottom_2[1]), 4, (255, 0, 0), 2)
        print("finger 5: top_1 = ", self.finger5.top_1[0], ",", self.finger5.top_1[1], "top_2 = ", self.finger5.top_2[0]
              , ",", self.finger5.top_2[1], "bottom_2 = ", self.finger5.bottom_2[0], ",", self.finger5.bottom_2[1])
        #Ip.show_pic(p, "finger5")

    def detect_bottom_point(self, top_finger, bottom_finger):
        start_i = top_finger.top_1[1]
        end_i = bottom_finger.top_1[1] - self.finger_width
        start_j = top_finger.top_1[0]
        end_j = self.finger1.bottom_2[0]
        border_point = []
        b_w_i = Ip.edge_detecting(self.image, 500, 500)
        # aa = np.array(self.image)
        bb = np.array(b_w_i)

        #Ip.show_pic(bb, "before border")

        for j in range(start_j, end_j):
            for i in range(start_i, end_i):
                if b_w_i[i][j] != 0:
                    # print(b_w_i[i][j])
                    # print(image[i][j])
                    number_tuple = (j, i)
                    border_point.append(number_tuple)

        length = len(border_point)
        temp = 0
        position = 0
        print("**************")
        # print(border_point)
        # aa = np.array(self.image)
        for i in range(0, length - 1):
            if border_point[i][0] > temp:
                temp = border_point[i][0]
                position = i
        top_finger.bottom_2[0] = border_point[position][0]
        top_finger.bottom_2[1] = border_point[position][1]
        bottom_finger.bottom_1[0] = border_point[position][0]
        bottom_finger.bottom_1[1] = border_point[position][1]

    def detect_tow_points(self, i, j, current_finger):
        print("192 - i , j , current_finger", i, j, current_finger.top_1[0], current_finger.top_1[1])

        rows, columns = self.image.shape
        found = 0
        temp = np.array([current_finger.top_1[0], current_finger.top_1[1]])  # holds: row, column/[y,x]/[j,i]/[k,l]
        for k in range(j, rows - 1):
            if found == 2:  # found both the points
                found = 0
                break
            if found == 0:  # looking for first terning point
                for l in range(0, i):
                    if self.image[k][l] == 0 and self.image[k][l + 1] != 0:

                        if k > temp[1] and l < temp[0]:  # if lower row and a lower column
                            temp[0] = l
                            temp[1] = k
                        if k > temp[1] and l > temp[0]:  # if lower row and a higher column - pasted the terning point
                            current_finger.top_2[0] = temp[0]
                            current_finger.top_2[1] = temp[1]
                            found = 1

            elif found == 1 and k > current_finger.top_2[1] + 102:  # looking for bottom second point

                for l in range(self.finger1.top_2[0], columns - 1):
                    if self.black_white_image[k][l] == 0 and self.black_white_image[k][l + 1] != 0:
                        # print("149 , k , l ,", k , l ,self.black_white_image[k][l] ,self.black_white_image[k][l + 1])
                        # if  temp[1] > l:  # if lower row and a lower column

                        # if lower row and a higher column - pasted the terning point
                        if inclination_between_two_points(temp, k, l) < 0:
                            print("222 , k , l ,", k, l, self.black_white_image[k][l], self.black_white_image[k][l + 1])
                            current_finger.bottom_2[0] = l
                            current_finger.bottom_2[1] = k
                            print("225 , k , l ,", k, l, temp[0], temp[1])
                            found = 2
                            break
                        else:
                            print("229 ", k, l)
                            temp[0] = l
                            temp[1] = k
                            continue

        print("234 ", current_finger.top_1[0], current_finger.top_1[1], current_finger.top_2[0], current_finger.top_2[1]
              , current_finger.bottom_2[0], current_finger.bottom_2[1])

    def detect_bottom2_point(self, i, j, current_finger):
        rows, columns = self.image.shape
        found = 0
        temp = np.array([current_finger.top_1[0], current_finger.top_1[1]])  # holds: row , column /[y,x]/[j,i]/[k,l]

        for k in range(j, rows - 1):
            if found == 1:
                break
            for l in range(i, columns - 1):
                if self.black_white_image[k][l] == 0 and self.black_white_image[k][l + 1] != 0:
                    inclination = inclination_between_two_points(temp, k, l)
                    #  cv2.circle(self.image, (l, k), 4, (255, 0, 0), 2)
                    # ip.show_pic(self.image, "*******")
                    #  print(inclination)

                    if inclination < -0.5:  # if lower row and a higher column - pasted the terning point
                        current_finger.bottom_2[0] = l
                        current_finger.bottom_2[1] = k
                        found = 1
                        break
                    else:
                        temp[0] = l
                        temp[1] = k
                        continue

    def detect_bottom2_finger5(self):

        rows, columns = self.image.shape
        print("263  - ", self.finger4.bottom_2[0], self.finger4.bottom_1[0], self.finger5.bottom_1[0])
        i_distance = self.finger4.bottom_2[0] - self.finger4.bottom_1[0]
        i = self.finger5.bottom_1[0] + i_distance
        self.finger5.bottom_2[0] = i

        for j in range(rows - 1, 1, -1):
            if self.black_white_image[j][i] == 0 and self.black_white_image[j-1][i] != 0:
                self.finger5.bottom_2[1] = j
                print("271 ", i, j)
                break

        print("273")

    def detect_second_finger(self, i, j):
        rows, columns = self.image.shape
        found = 0
        for l in range(i, columns - 1):
            if found == 1:
                break
            for k in range(0, j):
                if self.black_white_image[k][l] == 0 and self.black_white_image[k][l + 1] != 0:
                    self.finger2.top_1[0] = l
                    self.finger2.top_1[1] = k
                    found = 1
                    break

        self.detect_bottom2_point(self.finger2.top_1[0] + int(self.finger_width/2), self.finger2.top_1[1], self.finger2)

    def detect_fourth_finger(self, i, j):
        rows, columns = self.image.shape
        found = 0
        for l in range(i, columns - 1):
            if found == 1:
                break
            for k in range(j, rows - 1):
                if self.black_white_image[k][l] == 0 and self.black_white_image[k][l + 1] != 0:
                    self.finger4.top_1[0] = l
                    self.finger4.top_1[1] = k
                    found = 1
                    break
        self.finger4.top_2[0] = self.finger4.top_1[0]
        self.finger4.top_2[1] = self.finger4.top_1[1]
        self.detect_bottom2_point(self.finger4.top_1[0] + int(self.finger_width / 2),
                                  self.finger4.top_1[1], self.finger4)

    def detect_fifth_finger(self, i, j):
        rows, columns = self.image.shape
        found = 0
        for l in range(i, columns - 1):
            if found == 1:
                break
            for k in range(j, rows - 1):
                # print("l , k" , l," , ", k)
                # p = np.array(self.image)
                # cv2.circle(p, (l, k), 4, (255, 0, 0), 2)
                # ip.show_pic(p,"p pic")
                if self.black_white_image[k][l] == 0 and self.black_white_image[k][l + 1] != 0:
                    self.finger5.top_1[0] = l+1
                    self.finger5.top_1[1] = k
                    found = 1
                    break

    def detect_fingers(self):
        # critical_point = np.array()
        rows, columns = self.image.shape
        count = 1
        # first = 0
        # temp = np.array([0, 0])  # holds: row , column
        #Ip.show_pic(self.black_white_image, "image")

        for j in range(0, rows-1):
            if count == 2:
                break
            for i in range(0, columns-1):
                if self.black_white_image[j][i] == 0 and self.black_white_image[j][i+1] != 0:
                    # self.image[j][i]=255
                    if count == 1:  # detected first finger
                        count = 2

                        self.finger1.top_1[0] = i
                        self.finger1.top_1[1] = j

                        self.detect_tow_points(i, j, self.finger1)

                        self.finger_width = int(distance(self.finger1.top_1, self.finger1.top_2))
                        print("348 - self.finger_width = ", self.finger_width)
                        # print("178", self.finger1.bottom_2, self.black_white_image[self.finger1.bottom_2[0]]--
                        # --[self.finger1.bottom_2[1]+1])
                        break

        # search for finger 3
        for i in range(0, columns - 1):
            if count == 3:
                break
            for j in range(0, rows - 1):

                if (self.black_white_image[j][i] == 0) and (self.black_white_image[j][i+1] != 0):
                    if count == 2:  # detect third finger
                        count = 3

                        self.finger3.top_1[0] = i
                        self.finger3.top_1[1] = j
                        print("369 j = ", j, " finger = ", self.finger3.top_1[0])

                        self.detect_second_finger(int(i - self.finger_width), int(j - self.finger_width))
                        self.detect_fourth_finger(int(i + self.finger_width), int(j + self.finger_width))
                        self.detect_fifth_finger(int(self.finger4.top_2[0] + self.finger_width * 2)
                                                 , int(self.finger4.top_2[1] + self.finger_width))
                        break

        # self.detect_bottom_point(self.finger1, self.finger2)
        self.detect_bottom_point(self.finger2, self.finger3)
        self.detect_bottom_point(self.finger3, self.finger4)
        self.detect_bottom_point(self.finger4, self.finger5)

        self.detect_bottom2_finger5()

        ''' self.finger3.bottom_1[0] = self.finger2.bottom_2[0]
        self.finger3.bottom_1[1] = self.finger2.bottom_2[1]
        self.finger4.bottom_1[0] = self.finger3.bottom_2[0]
        self.finger4.bottom_1[1] = self.finger3.bottom_2[1]
        self.finger5.bottom_1[0] = self.finger4.bottom_2[0]
        self.finger5.bottom_1[1] = self.finger4.bottom_2[1]'''

        self.detect_palm_points()

        #Ip.show_pic(self.image, "image")

    def detect_palm_points(self):

        rows, columns = self.image.shape
        border_point = []
        b_w_i = Ip.edge_detecting(self.image, 500, 500)
        aa = np.array(self.image)
        j_top = 0
        j_bottom = 0

        for j in range(0, rows - 1):
            if (self.black_white_image[j][columns - 2] == 0) and (self.black_white_image[j + 1][columns - 2] != 0):
                j_top = j + 1
                break

        for j in range(rows - 1, 0, -1):
            if (self.black_white_image[j][columns - 2] == 0) and (self.black_white_image[j - 1][columns - 2] != 0):
                j_bottom = j - 1
                break

        start_i = self.finger1.top_1[0]
        end_i = columns - 1
        start_j = self.finger1.top_1[1]
        end_j = j_top

       # Ip.show_pic(b_w_i, "((((")
        print("440 - ", start_j, end_j, start_i, end_i)
        for i in range(start_i, columns - 1):
            for j in range(start_j, j_bottom):

                if b_w_i[j][i] != 0:
                    cv2.circle(aa, (i, j), 4, (255, 0, 0), 2)
                    # print(b_w_i[i][j])
                    # print(image[i][j])
                    number_tuple = (i, j)
                    border_point.append(number_tuple)
                    break
        #Ip.show_pic(aa, "&&&&&&&&")
        length = len(border_point)
        temp = border_point[0][1]
        position = 0
        print("**************")
        # print(border_point)
        aa = np.array(self.image)
        for i in range(0, length - 1):
            if border_point[i][1] > temp:
                temp = border_point[i][1]
                position = i
        self.palm_base_top[0] = border_point[position][0]
        self.palm_base_top[1] = border_point[position][1]
        cv2.circle(aa, (self.palm_base_top[0],  self.palm_base_top[1]), 4, (255, 0, 0), 2)
        #Ip.show_pic(aa, "++++++++")

        # ----------------------------
        aa = np.array(self.image)

        start_i = self.finger5.bottom_2[0]
        end_i = columns - 1
        start_j = self.finger5.bottom_2[1]
        end_j = j_top

        print("440 - ", start_j, end_j, start_i, end_i)
        for i in range(columns - 1, start_i, -1):
            for j in range(rows - 1, self.palm_base_top[1]):
                cv2.circle(aa, (i, j), 4, (255, 0, 0), 2)
                aa = np.array(self.image)

                if b_w_i[j][i] != 0:
                    cv2.circle(aa, (i, j), 4, (255, 0, 0), 2)
                    # print(b_w_i[i][j])
                    # print(image[i][j])
                    number_tuple = (i, j)
                    border_point.append(number_tuple)
                    break
       # Ip.show_pic(aa, "&&&&&&&&")
        length = len(border_point)
        temp = border_point[0][1]
        position = 0
        print("**************")
        # print(border_point)
        aa = np.array(self.image)
        for i in range(0, length - 1):
            if border_point[i][1] < temp:
                temp = border_point[i][1]
                position = i
        # self.palm_base_top[0] = border_point[position][0]
        # self.palm_base_top[1] = border_point[position][1]
        cv2.circle(aa, (self.palm_base_top[0], self.palm_base_top[1]), 4, (255, 0, 0), 2)
        #Ip.show_pic(aa, "///////////")

        print("414 - ", j_top, j_bottom)


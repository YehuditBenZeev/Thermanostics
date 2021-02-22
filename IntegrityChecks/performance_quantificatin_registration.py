#from alignment import get_point
from __future__ import print_function
from matplotlib import pylab as plt
import os
import glob
from registration import alignment
import numpy as np
from IntegrityChecks import registration_data as data
# import registration_data as data


def quantification():
    image_list = glob.glob(os.path.join("../test_images", '*.bmp'))
    # for i, image_path in enumerate(image_list):
    i = 0
    true_counter = 0
    false_counter = 0
    for image_path, real_points in data.images_514.items():
        #image = plt.imread(image_path)
        points = alignment.get_points(i, image_path)
        print(points.shape, "_________________")

        real_points = np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]])
        print(real_points.shape, "_________________")
        bool_array = map(lambda x: True if((x[0][0]-x[1][0])**2+(x[0][1]-x[1][1])**2)**0.5 < 5 else False, zip(points[0], real_points[0]))
        ture_in_arr = np.sum(bool_array)
        true_counter += ture_in_arr
        false_counter += (len(bool_array) - ture_in_arr)
        i += 1

    plt.show(block=True)


if __name__ == '__main__':
    quantification()
    # v = [True, True, False, False, True]
    # print(np.sum(v))

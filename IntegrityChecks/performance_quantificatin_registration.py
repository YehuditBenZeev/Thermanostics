from __future__ import print_function
from matplotlib import pylab as plt
from registration import alignment
import numpy as np
from IntegrityChecks import registration_data as data
from registration import matcher
from registration import akaze
from registration import orb
from registration import sift_cv
from registration import good_features_orb
from registration import surf_cv
from registration import fast

def quantification():
    # image_list = glob.glob(os.path.join("../test_images", '*.bmp'))
    # for i, image_path in enumerate(image_list):
    i = 0
    # true_counter = 0
    # false_counter = 0
    dict_counter = {
        'true': 0,
        'false': 0
    }

    dict_counter_514 = {
        'true': 0,
        'false': 0
    }

    for image_path, real_points in data.images_514.items():
        ref_image_link = "../images/514 RF.bmp"
        ref_image_points = data.image_ref['RF_514']

        points = alignment.get_points(ref_image_link, image_path, ref_image_points, fast.get_matching_points, matcher.matcher_DescriptorMatcher)

        bool_array = list(map(lambda x: True if((x[0][0]-x[1][0])**2+(x[0][1]-x[1][1])**2)**0.5 < 10 else False, zip(points[0], real_points[0])))
        ture_in_arr = np.sum(bool_array)
        dict_counter_514['true'] += ture_in_arr
        dict_counter_514['false'] += (len(bool_array) - ture_in_arr)
        i += 1

    for image_path, real_points in data.images.items():
        ref_image_link = ''
        ref_image_points = np.float64([[[]]])
        if 'RF' in image_path:
            ref_image_link = "../images/514 RF.bmp"
            ref_image_points = data.image_ref['RF_514']
        elif 'RB' in image_path:
            ref_image_link = "../images/514 RB.bmp"
            ref_image_points = data.image_ref['RB_514']
        elif 'LF' in image_path:
            ref_image_link = "../images/514 LF.bmp"
            ref_image_points = data.image_ref['LF_514']
        elif 'LB' in image_path:
            ref_image_link = "../images/514 LB.bmp"
            ref_image_points = data.image_ref['LB_514']

        points = alignment.get_points(ref_image_link, image_path, ref_image_points, fast.get_matching_points, matcher.matcher_DescriptorMatcher)

        bool_array = list(map(lambda x: True if((x[0][0]-x[1][0])**2+(x[0][1]-x[1][1])**2)**0.5 < 15 else False, zip(points[0], real_points[0])))
        ture_in_arr = np.sum(bool_array)

        dict_counter['true'] += ture_in_arr
        dict_counter['false'] += (len(bool_array) - ture_in_arr)
        i += 1

    plt.show(block=True)
    with open("registration.txt", "a") as out_file:

        out_file.write("fast - matcher matcher_DescriptorMatcher:\n\tregistration test 514 image result.\n")
        for item in dict_counter_514:
            out_file.write("\t\t" + item + ": " + str(dict_counter_514[item]) + "\n")
        percent_514 = (dict_counter_514['true'] / (dict_counter_514['true'] + dict_counter_514['false']))*100
        out_file.write("\t\tsuccess: {:.2f} %\n\n".format(percent_514))

        out_file.write("\tregistration test all images result.\n")
        for item in dict_counter:
            out_file.write("\t\t" + item + ": " + str(dict_counter[item]) + "\n")
        percent_all = (dict_counter['true'] / (dict_counter['true'] + dict_counter['false']))*100
        out_file.write("\t\tsuccess: {:.2f} %\n\n".format(percent_all))
    print(dict_counter)


if __name__ == '__main__':
    quantification()
    # v = [True, True, False, False, True]
    # sum_ = np.sum(v)
    # print(type(sum_))



import cv2 as cv
import csv
import os
from image_processing.finding_hotspots import FindingHotspots
from image_processing.division_palm_area import DivisionPalmArea
from image_processing.sort_hotspots import SortHotPointInArea
from normalization.normalization_part_0 import NormalizationPart0


def get_file_name(image_path):
    head, tail = os.path.split(image_path)
    image_name = os.path.splitext(tail)[0]
    file_mane = image_name + ".csv"
    return file_mane


def white_to_file(file_name, point_list, area):

    fields = ['X', 'Y', 'Area']
    # writing to csv file
    with open(file_name, 'a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fields, delimiter=';')
        if os.stat(file_name).st_size == 0:
            print("true")
            writer.writeheader()
        for point in point_list:
            row_ = {'X': point[0], 'Y': point[1], 'Area': area}
            writer.writerow(row_)


def normalization_part_0_points(hotspots_list, area_points, image_path):
    normalize = NormalizationPart0(image_path, area_points)

    normalized_points = normalize.find_new_locations(hotspots_list)
    file_name = get_file_name(image_path)
    white_to_file(file_name, normalized_points, 0)


def normalization_part_1_points(hotspots_list, area_points, image_path):
    # normalize = NormalizationPart1(image_path, area_points)
    # normalized_points = normalize.find_new_locations(hotspots_list)
    file_name = get_file_name(image_path)
    white_to_file(file_name, hotspots_list, 1)  # change hotspots_list to normalized_points


def normalization_part_2_points(hotspots_list, area_points, image_path):
    # normalize = NormalizationPart2(image_path, area_points)
    # normalized_points = normalize.find_new_locations(hotspots_list)
    file_name = get_file_name(image_path)
    white_to_file(file_name, hotspots_list, 2)  # change hotspots_list to normalized_points


def normalization_part_3_points(hotspots_list, area_points, image_path):
    # normalize = NormalizationPart3(image_path, area_points)
    # normalized_points = normalize.find_new_locations(hotspots_list)
    file_name = get_file_name(image_path)
    white_to_file(file_name, hotspots_list, 3)  # change hotspots_list to normalized_points


def normalization_part_4_points(hotspots_list, image_info, image_path):
    # normalize = NormalizationPart4(image_path, area_points)
    # normalized_points = normalize.find_new_locations(hotspots_list)
    file_name = get_file_name(image_path)
    white_to_file(file_name, hotspots_list, 4)  # change hotspots_list to normalized_points


def normalization_part_5_points(hotspots_list, area_points, image_path):
    # normalize = NormalizationPart5(image_path, area_points)
    # normalized_points = normalize.find_new_locations(hotspots_list)
    file_name = get_file_name(image_path)
    print(len(hotspots_list))
    white_to_file(file_name, hotspots_list, 5)  # change hotspots_list to normalized_points


def normalized_hotspots(file_name):
    with open(file_name, 'r') as file:  # could pot all edge-points of palm in file with appropriate names and normalize all points with one file
        csv_file = csv.DictReader(file, delimiter=';')
        for row in csv_file:
            path = row['imagePath']
            rbg_image = cv.imread(path)
            gray_image = cv.cvtColor(rbg_image, cv.COLOR_RGB2GRAY)  # or image processed image depends on the final algorithm decision
            area_0_points = [(int(row['X1-0']), int(row['Y1-0'])),
                             (int(row['X2-0']), int(row['Y2-0'])),
                             (int(row['X3-0']), int(row['Y3-0'])),
                             (int(row['X4-0']), int(row['Y4-0'])),
                             (int(row['X5-0']), int(row['Y5-0'])),
                             (int(row['X6-0']), int(row['Y6-0'])),
                             (int(row['X7-0']), int(row['Y7-0'])),
                             (int(row['X8-0']), int(row['Y8-0'])),
                             (int(row['X9-0']), int(row['Y9-0']))]

            area_1_points = [(int(row['X1-1']), int(row['Y1-1'])),
                             (int(row['X2-1']), int(row['Y2-1'])),
                             (int(row['X3-1']), int(row['Y3-1'])),
                             (int(row['X4-1']), int(row['Y4-1']))]

            area_2_points = [(int(row['X1-2']), int(row['Y1-2'])),
                             (int(row['X2-2']), int(row['Y2-2'])),
                             (int(row['X3-2']), int(row['Y3-2'])),
                             (int(row['X4-2']), int(row['Y4-2']))]

            area_3_points = [(int(row['X1-3']), int(row['Y1-3'])),
                             (int(row['X2-3']), int(row['Y2-3'])),
                             (int(row['X3-3']), int(row['Y3-3'])),
                             (int(row['X4-3']), int(row['Y4-3']))]

            area_4_points = [(int(row['X1-4']), int(row['Y1-4'])),
                             (int(row['X2-4']), int(row['Y2-4'])),
                             (int(row['X3-4']), int(row['Y3-4'])),
                             (int(row['X4-4']), int(row['Y4-4']))]

            area_5_points = [(int(row['X1-5']), int(row['Y1-5'])),
                             (int(row['X2-5']), int(row['Y2-5'])),
                             (int(row['X3-5']), int(row['Y3-5'])),
                             (int(row['X4-5']), int(row['Y4-5']))]

            area_points_list = [area_0_points, area_1_points, area_2_points, area_3_points, area_4_points, area_5_points]

            # image_processing
            hotspots_obj = FindingHotspots(gray_image, 20)  # or read from file  # 20 - size of matrix which we lock at in finding the hotspots
            division_obj = DivisionPalmArea(gray_image, area_points_list)
            sort_obj = SortHotPointInArea(gray_image, division_obj, hotspots_obj)

            # normalization
            normalization_part_0_points(sort_obj.array_area_0, area_0_points, path)
            normalization_part_1_points(sort_obj.array_area_1, area_1_points, path)
            normalization_part_2_points(sort_obj.array_area_2, area_2_points, path)
            normalization_part_3_points(sort_obj.array_area_3, area_3_points, path)
            normalization_part_4_points(sort_obj.array_area_4, area_4_points, path)
            normalization_part_5_points(sort_obj.array_area_5, area_5_points, path)


if __name__ == '__main__':
    file = "edge_points.csv"
    normalized_hotspots(file)  # detected and write normalized hotspots to file

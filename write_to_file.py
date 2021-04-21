import csv
import os


def white_points_to_file(file_name, point_list, area):

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


def get_file_name(image_path, type=''):
    head, tail = os.path.split(image_path)
    image_name = os.path.splitext(tail)[0]
    file_name = image_name + type + ".csv"
    return file_name


import csv
import pandas as pd
import cv2 as cv
from image_processing import finding_hotspots as find


MAX_DIST = 5


class ObjectTest:
    def __init__(self, boolean, point):
        self.boolean = boolean
        self.point = point  # (x, y)  # example:(1,1) found(1,2)


def convert_exel_csv(exelFile):
    read_file = pd.read_excel(exelFile)
    read_file.to_csv("Test.csv", index=None, header=True)
    df = pd.DataFrame(pd.read_csv("Test.csv"))
    print(df)


def read_from_file(file_name):  # reads csv files
    point_list = []
    with open(file_name, 'r') as infile:
        csv_writer = csv.DictReader(infile)
        for row in csv_writer:
            point_list.append(ObjectTest(False, (int(row['X']), int(row['Y']))))
    return point_list


# finds the distance between two points
def distance(point1, point2):
    x = point1[0] - point2[0]
    y = point1[1] - point2[1]

    point_distance = (x**2 + y**2)**0.5
    return point_distance


class TestsHotSpots:
    def __init__(self, expected_points, detected_points):
        self.expected_points = read_from_file(expected_points)  # algoritm
        self.detected_points = read_from_file(detected_points)  # alona

    def check_detected_points(self):
        # open file to read point
        for point in self.detected_points:
            if self.is_in_area(point.point):
                point.boolean = True

    def is_in_area(self, point_det):
        for point in self.expected_points:
            if distance(point.point, point_det) < MAX_DIST:
                point.boolean = True
                return True
        return False

    def check_success(self):
        true_positive = 0  # The algorithm predicted a hot spot and there
        true_negative = 0  # The algorithm predicted that there is no hot spot and no
        false_positive = 0  # The algorithm predicted that there is no hotspot but there is
        false_negative = 0  # The algorithm predicted that there is no hotspot but there is
        print(self.detected_points[0].boolean, self.expected_points[0].boolean)

        for point in self.detected_points:
            if point.boolean:
                true_positive += 1
            else:
                false_positive += 1

        for point in self.expected_points:
            print(point.point, "--")
            if not point.boolean:
                false_negative += 1
        print("true_positive,true_negative,false_positive,false_negative", true_positive, true_negative, false_positive, false_negative)

        print("true_positive,true_negative,false_positive,false_negative", true_positive, true_negative, false_positive,
              false_negative)
        accuracy = (true_positive + true_negative) / (true_positive + true_negative + false_negative + false_negative)
        precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) else "infinity"
        tpr = true_positive / (true_positive + false_negative) if (true_positive + false_negative) else "infinity"
        fpr = false_positive / (false_positive + true_negative) if (false_positive + true_negative) else "infinity"
        print("accuracy:", accuracy, "\n", "precision", precision)
        print("tpr", tpr)
        print("fpr", fpr)


if __name__ == "__main__":
    a = TestsHotSpots("algoritm_505_LB.csv", "alona_505_LB.csv")
    a.check_detected_points()
    a.check_success()
    im = cv.imread("../im1.jpg", cv.IMREAD_COLOR)
    gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)

    find_hotspot = find.FindingHotspotsInPicture(gray)
    find_hotspot.pass_on_image(10)
    algoritm_file = find_hotspot.write_in_file()

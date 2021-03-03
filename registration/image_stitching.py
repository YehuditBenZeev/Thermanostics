import numpy as np
import cv2 as cv


def harris_corner_detection():
    file_name = '../images/514 RF.bmp'
    img = cv.imread(file_name)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv.cornerHarris(gray, 9, 3, 0.06)

    #result is dilated for marking the corners, not important
    dst = cv.dilate(dst, None)

    # Threshold for an optimal value, it may vary depending on the image.
    img[dst > 0.01 * dst.max()] = [0, 0, 255]
    cv.imshow('dst', img)
    if cv.waitKey(0) & 0xff == 27:
        cv.destroyAllWindows()

    h, w, c = img.shape
    points = []
    for i in range(h - 1):
        for j in range(w - 1):
            if img[i][j][0] == [0] and img[i][j][1] == [0] and img[i][j][2] == [255]:
                points.append((i, j))

    # points = [x for i in img if img[x] == [0, 0, 255]]
    # print("points:")
    # print(len(points))
    # print(points)
    return points


harris_corner_detection()

import numpy as np
import cv2 as cv


def harris_corner_detection(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv.cornerHarris(gray, 9, 3, 0.06)

    dst = cv.dilate(dst, None)
    img[dst > 0.01 * dst.max()] = [0, 0, 255]

    h, w, c = img.shape
    points = []
    for i in range(h - 1):
        for j in range(w - 1):
            if img[i][j][0] == [0] and img[i][j][1] == [0] and img[i][j][2] == [255]:
                points.append([i, j])
    final = [points, ]
    return final


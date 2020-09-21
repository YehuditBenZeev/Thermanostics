import numpy as np


class Finger:
    def __init__(self):
        self.top_1 = np.array([0, 0])  # holds (i , j) when i is the width position and j us the height position.
        self.top_2 = np.array([0, 0])
        self.bottom_1 = np.array([0, 0])
        self.bottom_2 = np.array([0, 0])

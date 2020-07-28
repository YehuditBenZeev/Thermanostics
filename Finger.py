import cv2
import numpy as np
import argparse

class Finger:
    def __init__(self):
        self.top_1 = np.array([0,0])
        self.top_2 =  np.array([0,0])
        self.bottom_1 =  np.array([0,0])
        self.bottom_2 =  np.array([0,0])
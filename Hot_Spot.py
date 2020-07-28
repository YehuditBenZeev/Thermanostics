import cv2
import numpy as np
import argparse

class Hot_Spot:

    def __init__(self , value , location):
        self.max_value = value
        self.location = location

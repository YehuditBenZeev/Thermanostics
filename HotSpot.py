import cv2
import numpy as np
import argparse

class HotSpot:

    def __init__(self , value , location):
        self.max_value = value
        self.location = location

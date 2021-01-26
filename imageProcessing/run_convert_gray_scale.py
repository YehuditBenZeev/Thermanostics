import matplotlib.pyplot as plt
import os, sys
import glob
import numpy as np
import argparse
from imageProcessing import ConvertGrayScale

# sys.path.append(os.path.dirname(os.path.abspath("../")))


def main():
    image_list = glob.glob(os.path.join("../images", '*.bmp'))
    for image_path in image_list:
        # image = plt.imread(image_path)
        ConvertGrayScale.edge(image_path)
        # plt.imshow(image)  # , cmap=plt.get_cmap('gray'))
    plt.show(block=True)


if __name__ == "__main__":
    main()


import matplotlib.pyplot as plt
import os
import glob
from imageProcessing import ConvertGrayScale


def main():
    image_list = glob.glob(os.path.join("../images", '*.bmp'))
    for image_path in image_list:
        ConvertGrayScale.edge(image_path)
    plt.show(block=True)


if __name__ == "__main__":
    main()


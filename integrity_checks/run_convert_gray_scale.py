import matplotlib.pyplot as plt
import os
import glob
from image_processing import convert_gray_scale


def main():
    image_list = glob.glob(os.path.join("../images", '*.bmp'))
    for image_path in image_list:
        convert_gray_scale.edge(image_path)
    plt.show(block=True)


if __name__ == "__main__":
    main()


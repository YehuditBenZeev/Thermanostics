import skimage.io as io
import numpy as np
from matplotlib import pyplot as plt
from skimage.color import rgb2gray
from skimage.data import stereo_motorcycle  #, vortex
from skimage.transform import warp
from skimage.registration import optical_flow_tvl1  #, optical_flow_ilk
from skimage.transform import resize


def try_package():
    image1 = io.imread("../images/514 RF.bmp")
    image2 = io.imread("../images/515 RF.bmp")

    grayscale1 = rgb2gray(image1)
    grayscale2 = rgb2gray(image2)

    grayscale2 = resize(grayscale2, grayscale1.shape)

    # image0, image1, disp = stereo_motorcycle()
    # # --- Convert the images to gray level: color is not supported.
    # image0 = rgb2gray(image0)
    # image1 = rgb2gray(image1)

    fig1, (ax, ax_) = plt.subplots(2, 1, figsize=(5, 10))

    ax.imshow(grayscale1)
    ax.set_title("grayscale1")
    ax.set_axis_off()

    ax_.imshow(grayscale2)
    ax_.set_title("grayscale2")
    ax_.set_axis_off()

    fig1.tight_layout()

    # --- Compute the optical flow
    v, u = optical_flow_tvl1(grayscale1, grayscale2)

    # --- Use the estimated optical flow for registration

    nr, nc = grayscale1.shape

    row_coords, col_coords = np.meshgrid(np.arange(nr), np.arange(nc),
                                         indexing='ij')

    image1_warp = warp(grayscale2, np.array([row_coords + v, col_coords + u]),
                       mode='nearest')

    # build an RGB image with the unregistered sequence
    seq_im = np.zeros((nr, nc, 3))
    seq_im[..., 0] = grayscale2
    seq_im[..., 1] = grayscale1
    seq_im[..., 2] = grayscale1

    # build an RGB image with the registered sequence
    reg_im = np.zeros((nr, nc, 3))
    reg_im[..., 0] = image1_warp
    reg_im[..., 1] = grayscale1
    reg_im[..., 2] = grayscale1

    # build an RGB image with the registered sequence
    target_im = np.zeros((nr, nc, 3))
    target_im[..., 0] = grayscale1
    target_im[..., 1] = grayscale1
    target_im[..., 2] = grayscale1

    # --- Show the result

    fig2, (ax0, ax1, ax2) = plt.subplots(3, 1, figsize=(5, 10))

    ax0.imshow(seq_im)
    ax0.set_title("Unregistered sequence")
    ax0.set_axis_off()

    ax1.imshow(reg_im)
    ax1.set_title("Registered sequence")
    ax1.set_axis_off()

    ax2.imshow(target_im)
    ax2.set_title("Target")
    ax2.set_axis_off()

    fig2.tight_layout()
    plt.show(block=True)


if __name__ == "__main__":
    try_package()

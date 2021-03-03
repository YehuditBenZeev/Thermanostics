import SimpleITK as sitk
import sys
import os
from matplotlib import pylab as plt


def command_iteration(method):
    print(f"{method.GetOptimizerIteration():3} = {method.GetMetricValue():10.5f}")

link2 = '../514 images/514 RF dark.bmp'
link1 = '../514 images/514 RF.bmp'

# image = sitk.ReadImage(link1, imageIO="BMPImageIO")
# # plt.imshow(image)
# # plt.show(block=True)
#
# # sitk.Show(image, title="Hello World: Python")
#
# sitk.WriteImage(image, 'SimpleITK.bmp')
fixed = sitk.ReadImage(link1, sitk.sitkFloat32)

moving = sitk.ReadImage(link2, sitk.sitkFloat32)
# plt.imshow(fixed)
# plt.show(block=True)
matcher = sitk.HistogramMatchingImageFilter()
matcher.SetNumberOfHistogramLevels(1024)
matcher.SetNumberOfMatchPoints(7)
matcher.ThresholdAtMeanIntensityOn()
moving = matcher.Execute(moving, fixed)

sitk.Show(moving, "DeformableRegistration1 Composition")

sitk.WriteImage(moving, 'SimpleITK.bmp')

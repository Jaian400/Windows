from skimage import io, color, filters, transform
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from datetime import datetime
# from tensorflow import keras
# from keras.constraints import maxnorm
# from keras.utils import np_utils

from load_images import load_images

columns = ["Image", "Date", "Time"]
images = pd.DataFrame(load_images(), columns=columns)

print(images)

# LOADING A TEST PICTURE
# image = io.imread("IMG_20250129_002603.jpg")

# pixel_value = image[50, 100]
# print("Wartość piksela na (50, 100):", pixel_value)

# MAKING AN IMAGE GREY
gray_image = color.rgb2gray(images.iloc[0, 0])

hsv_image = color.rgb2hsv(images.iloc[0, 0])
brightness = hsv_image[:, :, 2]

threshold = 0.4
binary_mask = np.where(brightness < threshold, 0, 1)
output_image = (binary_mask * 255).astype(np.uint8)
io.imsave('proccessed_image.jpg',output_image)
# modified_image = np.where(gray_image < threshold, 1, gray_image)

# fig, ax = plt.subplots(1, 2, figsize=(10, 5))
#
# ax[0].imshow(image)
# ax[0].set_title("Original Image")
# ax[0].axis("off")
#
# ax[1].imshow(output_image, cmap="gray")
# ax[1].set_title("output_image")
# ax[1].axis("off")
#
# ax[2].imshow(modified_image)
# ax[2].set_title("modified_image")
# ax[2].axis("off")

# plt.imshow(modified_image, cmap="gray")
# plt.axis("off")
# plt.tight_layout()
# plt.show()
from skimage import io, color, filters, transform, exposure
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from datetime import datetime
from load_images import load_images
from scipy.ndimage import median_filter
import logging

LOGS_DIR = "../logs"
os.makedirs(LOGS_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOGS_DIR, "app.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

DATA_PATH = "../data/raw"
SAVE_PATH = "../data/processed"

def detect_windows(image):
    """Detects lit windows in an image and returns a binary mask."""
    gray_image = color.rgb2gray(image)
    gray_image = exposure.equalize_adapthist(gray_image)
    # Otsu method
    threshold = filters.threshold_otsu(gray_image)
    binary_mask = (gray_image > threshold).astype(np.uint8)
    binary_mask = median_filter(binary_mask, size=2)
    output_image = (binary_mask * 255).astype(np.uint8)

    return output_image

def process_and_save_images():
    os.makedirs(SAVE_PATH, exist_ok=True)

    for filename in os.listdir(DATA_PATH):
        if filename.lower().endswith((".jpg", ".png")):
            image_path = os.path.join(DATA_PATH, filename)
            image = io.imread(image_path)

            binary_matrix = detect_windows(image)

            # Save matrix as CSV
            matrix_filename = f"{os.path.splitext(filename)[0]}.csv"
            np.savetxt(os.path.join(SAVE_PATH, matrix_filename), binary_matrix, delimiter=",", fmt="%d")

            logging.info(f"Processed {filename}, saved as {matrix_filename}")

#GOOOO
process_and_save_images()

# COLUMNS: Image in skimage format, date in %Y%m%d, time in %H%M%S
# images = load_images()
#
# print(images.head(10))
#
# # pixel_value = image[50, 100]
# # print("Wartość piksela na (50, 100):", pixel_value)
#
# # MAKING AN IMAGE GREY
# gray_image = color.rgb2gray(images.iloc[0, 0])
#
# hsv_image = color.rgb2hsv(images.iloc[0, 0])
# brightness = hsv_image[:, :, 2]


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
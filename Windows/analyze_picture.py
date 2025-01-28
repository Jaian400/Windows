from skimage import io, color, filters, transform
import matplotlib.pyplot as plt

image = io.imread("IMG_20250129_002603.jpg")

gray_image = color.rgb2gray(image)

fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].imshow(image)
ax[0].set_title("Original Image")
ax[0].axis("off")

ax[1].imshow(gray_image, cmap="gray")
ax[1].set_title("gray_image")
ax[1].axis("off")

plt.tight_layout()
plt.show()
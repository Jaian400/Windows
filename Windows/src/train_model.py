from load_images import load_images
import numpy as np

# COLUMNS: Image in skimage format, Date in %Y%m%d, Time in %H%M%S
data = load_images()

X = np.array([img for img in data["Image"]])
y = X.copy()

X = X.reshape(-1, 128, 128, 1).astype(np.float32)
y = y.reshape(-1, 128, 128, 1).astype(np.float32)

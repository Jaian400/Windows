import os
from skimage import io, color, filters, transform
from datetime import datetime

folder_path = "\images"

def extract_date_and_time(image_path):
    filename = os.path.basename(image_path)
    timestamp_str = filename.split('_')[1]
    timestamp = datetime.strptime(timestamp_str, '%Y%m%d_%H%M%S')
    return timestamp.date(), timestamp.time()


def load_images():
    images = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(folder_path, filename)
            image = io.imread(image_path)
            images.append(image)
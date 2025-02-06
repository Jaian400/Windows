import os
from skimage import io, color, filters, transform
from datetime import datetime

folder_path = "images"

def extract_date_and_time(image_path):
    filename = os.path.basename(image_path)
    timestamp_str = filename.split('_')[1]
    timestamp = datetime.strptime(timestamp_str, '%Y%m%d')
    timestamp_str = filename.split('_')[2]
    timestamp_str = timestamp_str.split('.')[0]
    print(timestamp_str)
    timestamp_time = datetime.strptime(timestamp_str, '%H%M%S')

    return timestamp.date(), timestamp_time.time()

def load_images():
    data = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(folder_path, filename)
            date, time = extract_date_and_time(image_path)

            image = io.imread(image_path)
            data.append([image, date, time])

    return data
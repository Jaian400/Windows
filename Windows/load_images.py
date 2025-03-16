import os
from skimage import io, color, filters, transform
from datetime import datetime
import pandas as pd

folder_path = "../data/raw"

def extract_date_and_time(image_path):
    filename = os.path.basename(image_path)

    try:
        parts = filename.split('_')
        if len(parts) < 3:
            raise ValueError(f"Filename {filename} is not in expected format.")

        date_part = parts[1]
        time_part = parts[2].split('.')[0]

        date = datetime.strptime(date_part, '%Y%m%d').date()
        time = datetime.strptime(time_part, '%H%M%S').time()

        return date, time

    except Exception as e:
        print(f"Error processing {filename}: {e}")
        return None, None

def load_images():
    columns = ["Image", "Date", "Time"]
    data = pd.DataFrame(columns=columns)

    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(folder_path, filename)
            date, time = extract_date_and_time(image_path)

            if date and time:
                image = io.imread(image_path)
                data.loc[len(data)] = [image, date, time]

    return data
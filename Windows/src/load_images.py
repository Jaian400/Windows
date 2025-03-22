import os
import logging
from skimage import io, color, transform
from datetime import datetime
import pandas as pd

LOGS_DIR = "../logs"
os.makedirs(LOGS_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOGS_DIR, "app.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

FOLDER_PATH = "../data/raw"
IMAGE_SIZE = (256, 256)

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

    for filename in os.listdir(FOLDER_PATH):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(FOLDER_PATH, filename)
            date, time = extract_date_and_time(image_path)

            if date and time:
                image = io.imread(image_path)
                image = transform.resize(image, IMAGE_SIZE, anti_aliasing=True)
                data.loc[len(data)] = [image, date, time]

    logging.info(f"Loaded {len(data)} images successfully.")
    return data
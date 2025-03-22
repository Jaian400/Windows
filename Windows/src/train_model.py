import os
import numpy as np
import tensorflow as tf
from tensorflow import keras

DATA_PATH = "../data/processed"
MODEL_PATH = "../models/window_detector.h5"


def load_training_data():
    """Loads binary matrices from CSV files as training data."""
    x, y = [], []

    for filename in os.listdir(DATA_PATH):
        if filename.endswith(".csv"):
            matrix = np.loadtxt(os.path.join(DATA_PATH, filename), delimiter=",")

            x.append(matrix.reshape(128, 128, 1))
            y.append(matrix)

    x = np.array(x, dtype=np.float32)
    y = np.array(y, dtype=np.float32)
    return x, y

def build_model(input_shape=(128, 128, 1)):
    """Defines a simple CNN for learning window lighting patterns."""
    model = keras.models.Sequential([
        keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=input_shape),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), activation="relu"),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Flatten(),
        keras.layers.Dense(128, activation="relu"),
        keras.layers.Dense(128 * 128, activation="sigmoid"),
        keras.layers.Reshape((128, 128))
    ])

    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    return model


def train_and_save_model():
    """Loads training data, trains the model, and saves it."""
    X, y = load_training_data()

    model = build_model(input_shape=X.shape[1:])
    model.fit(X, y, epochs=10, batch_size=8, validation_split=0.2)

    # Save trained model
    model.save(MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train_and_save_model()

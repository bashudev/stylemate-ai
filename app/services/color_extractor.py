import cv2
import numpy as np


def get_average_color(image):
    """
    Returns the average RGB colour of the uploaded image.
    """

    # Convert PIL image to NumPy array
    image = np.array(image)

    # Convert RGB to BGR (OpenCV format)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Calculate average colour
    average = image.mean(axis=0).mean(axis=0)

    return {
        "blue": int(average[0]),
        "green": int(average[1]),
        "red": int(average[2])
    }
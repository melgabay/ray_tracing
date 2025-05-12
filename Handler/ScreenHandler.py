
from PIL import Image
import numpy as np

def save_image(array: np.ndarray, path: str):
    img = Image.fromarray(array, mode="RGB")
    img.save(path)

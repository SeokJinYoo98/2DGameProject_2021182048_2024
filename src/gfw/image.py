import os
from pico2d import *
from gfw.config import SPRITES_DIR

_images = {}

def load(file):
    global _images
    if file in _images:
        return _images[file]
        
    file_path = os.path.join(SPRITES_DIR, file)
    image = load_image(file_path)
    _images[file] = image
    return image

def unload(file):
    global _images
    if file in _images:
        del _images[file]


import pico2d
import os
from gfw.config import SOUNDS_DIR
_sounds = {}

def music(file):
    return load(file, pico2d.load_music)

def sfx(file): # sfx = Sound Effect
    return load(file, pico2d.load_wav)

def load(file, func):
    global _sounds
    if file in _sounds:
        return _sounds[file]
    file_path = os.path.join(SOUNDS_DIR, file)
    sound = func(file_path)
    _sounds[file_path] = sound
    return sound

def unload(file):
    global _sounds
    if file in _sounds:
        del _sounds[file]


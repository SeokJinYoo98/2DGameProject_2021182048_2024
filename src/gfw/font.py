from pico2d import *
from gfw.config import Font_DIR
_fonts = {}

def load(file, size=20):
    key = file + '_' + str(size)
    global _fonts
    if key in _fonts:
        return _fonts[key]

    # print("Loading font:", file, size)
    file_path = os.path.join(Font_DIR, file)
    font = load_font(file_path, size)
    _fonts[key] = font
    return font

def unload(file, size=20):
    key = file + '_' + str(size)
    global _fonts
    if key in _fonts:
        del _fonts[key]

def get_text_extent(font, text):
    w, h = c_int(), c_int()
    TTF_SizeText(font.font, text.encode('utf-8'), ctypes.byref(w), ctypes.byref(h))
    return w.value, h.value

def draw_centered_text(font, text, x, y, color=(0,0,0)):
    tw, th = get_text_extent(font, text)
    tx = x - tw // 2
    ty = y - th // 2
    font.draw(tx, ty, text, color)

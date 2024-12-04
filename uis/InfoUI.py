import gfw
class InfoUI:
    def __init__(self, zom):
        self.__zom = zom
        self.__font = gfw.font.load('neodgm.TTF', 36)
    def update(self):
        pass

    def draw(self):
        time_text = f"Stage:{self.__zom.level + 1}"
        centerX = gfw.get_canvas_width() / 2 - 70
        y = gfw.get_canvas_height() - 50
        self.__font.draw(centerX, y, time_text, (255,0,0))
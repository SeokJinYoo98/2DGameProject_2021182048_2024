import gfw
class TimeUI:
    def __init__(self):
        self.__startMin = 10
        self.__startSec = 0
        self.__elapsed = 0
        self.__font = gfw.font.load('neodgm.TTF', 36)

    def update(self):
        self.__elapsed += gfw.frame_time

        if self.__elapsed >= 1: 
            self.__elapsed -= 1
            self.__startSec -= 1

            if self.__startSec < 0:
                self.__startMin -= 1
                self.__startSec = 59

            if self.__startMin < 0:
                gfw.top().ending()

    def draw(self):
        time_text = f"{self.__startMin:02}:{self.__startSec:02}"
        centerX = gfw.get_canvas_width() / 2 - 45
        y = gfw.get_canvas_height() - 100
        self.__font.draw(centerX, y, time_text)
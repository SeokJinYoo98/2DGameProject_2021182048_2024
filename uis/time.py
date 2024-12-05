import gfw
class TimeUI:
    def __init__(self):
        self.__startMin = 10
        self.__startSec = 0
        self.__elapsed = 0
        self.__font = gfw.font.load('neodgm.TTF', 36)
        self.__sound = gfw.sound.sfx('Win.wav')
        self.end = False
        self.endTime = 2
    def update(self):
        if self.end:

            self.endTime -= gfw.frame_time
            if self.endTime <= 0:
                self.__sound.play()
                gfw.top().ending()
            else:
                return            
        self.__elapsed += gfw.frame_time
            
        if self.__elapsed >= 1: 
            self.__elapsed -= 1
            self.__startSec -= 1

            if self.__startSec < 0:
                self.__startMin -= 1
                self.__startSec = 59

            if self.__startMin < 0:
                gfw.top().Winner()
                self.__startMin = 0
                self.__startSec = 0

    def draw(self):
        time_text = f"{self.__startMin:02}:{self.__startSec:02}"
        centerX = gfw.get_canvas_width() / 2 - 45
        y = gfw.get_canvas_height() - 100
        self.__font.draw(centerX, y, time_text)
    def reduceTime(self):
        self.__startMin -=1
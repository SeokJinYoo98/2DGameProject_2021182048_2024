import gfw

class XpUI:
    def __init__(self):
        self.__gauge = gfw.Gauge('progress/progress_fg.png', 'progress/progress_bg.png')
        self.__player = gfw.top().world.player
        self.__x = gfw.get_canvas_width() - 150
        self.__width = 150
        self.__y = gfw.get_canvas_height() - 100
        self.rate = 0
    def update(self):
        if self.__player.Xp <= 0:
            self.rate = 0.05
        else:
            self.rate = self.__player.Xp / 10
    def draw(self):
        self.__gauge.draw(self.__x, self.__y, self.__width, self.rate)
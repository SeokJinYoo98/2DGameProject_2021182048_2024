import gfw

class HpUI:
    def __init__(self):
        self.__gauge = gfw.Gauge('progress/progress_hp.png', 'progress/progress_bg.png')
        self.__player = gfw.top().world.player
        self.__x = 150
        self.__width = 150
        self.__y = gfw.get_canvas_height() - 100
        self.rate = 0
    def update(self):
        if self.__player.hp <= 0:
            self.rate = 0.1
        else:
            self.rate = self.__player.hp / self.__player.maxHp
    def draw(self):
        self.__gauge.draw(self.__x, self.__y, self.__width, self.rate)
    
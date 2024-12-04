import gfw

class MagGauge:
    def __init__(self):
        self.__gauge = gfw.Gauge('progress/gauge_fg.png', 'progress/gauge_bg.png')
        self.__player = gfw.top().world.player
        self.__rate = 0
        self.__width = 38
        self.__no = False
        self.__world = gfw.top().world
    def update(self):
        if self.__no: return
        if self.__player.magTime <= 0.1:
            self.__no = True
            self.__player.magGauge = None
            self.__world.remove(self, self.__world.layer.UI)
        else:
            self.__rate = self.__player.magTime / 3
                
    def draw(self):
        screen = self.__world.bg.to_screen(self.__player.x, self.__player.y - 30)
        self.__gauge.draw(*screen, self.__width, self.__rate)
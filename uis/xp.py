import gfw

class XpUI:
    def __init__(self):
        self.__gauge = gfw.Gauge('progress/progress_xp.png', 'progress/progress_bg.png')
        self.__player = gfw.top().world.player
        self.__x = gfw.get_canvas_width() - 150
        self.__width = 150
        self.__y = gfw.get_canvas_height() - 100
        self.__rate = 0
        self.__font = gfw.font.load('neodgm.TTF', 24)
    def update(self):
        if self.__player.Xp <= 0:
            self.__rate = 0.02
        else:
            self.__rate = self.__player.Xp / self.__player.maxXp
    def draw(self):
        self.__gauge.draw(self.__x, self.__y, self.__width, self.__rate)
        hp_text = f"{self.__player.Xp}/{self.__player.maxXp}"
        self.__font.draw(self.__x - 20, self.__y, hp_text, (255, 255, 255))
        
    
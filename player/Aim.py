import gfw

class Aim(gfw.Sprite):
    def __init__(self):
        super().__init__('ui/Aim.png', 0, 0)
        self.x, self.y = 0, 0
        self.collType = False
    def draw(self):
        self.image.draw(self.x, self.y, 50, 50)
    def setLoaction(self, x, y):
        self.x, self.y = x, y
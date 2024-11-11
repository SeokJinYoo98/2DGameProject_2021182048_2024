import gfw

class Item(gfw.Sprite):
    def __init__(self, fileName, x, y):
        super().__init__(fileName, x, y)

        self.height *= 2
        self.width *= 2
    def draw(self):
        pos = gfw.top().bg.to_screen(self.x, self.y)
        self.image.draw(*pos, 2, 2)
    def magnetic(self):
        pass
    
    def special_function(self):
        pass

class Coin(Item):
    def __init__(self, x, y):
        COIN_PATH = 'prop/Coin.png'
        super().__init__(COIN_PATH, x, y)

class Vaccine(Item):
    def __init__(self, x, y):
        VACCINE_PATH = 'prop/Vaccine.png'
        super().__init__(VACCINE_PATH, x, y)

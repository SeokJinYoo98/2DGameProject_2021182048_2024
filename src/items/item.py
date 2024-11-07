import gfw

class Item(gfw.Sprite):
    def __init__(self, x, y, fileName):
        super().__init__(fileName, x, y)
        
    def draw(self):
        pass
    def update(self):
        pass
    def magnetic(self):
        pass
    def get_bb(self):
        pass
    def special_function(self):
        pass

class Vacine(Item):
    pass

class Coin(Item):
    pass
    
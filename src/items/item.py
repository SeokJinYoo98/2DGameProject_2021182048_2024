import gfw

class Item(gfw.Sprite):
    def __init__(self, x, y, fileName):
        super().__init__(fileName, x, y)


class Vacine(Item):
    pass

class Coin(Item):
    pass
    
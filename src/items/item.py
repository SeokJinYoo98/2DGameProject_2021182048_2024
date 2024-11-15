import gfw

class Item(gfw.Sprite):
    Speed = 1
    def __init__(self, fileName, x, y, Type):
        super().__init__(fileName, x, y)
        self.target = None
        self.Type = Type
    def __del__(self):
        self.target = None
        self.Type = None
    def update(self):
        if self.target is None: return
        
        tx = self.target.x
        ty = self.target.y
        
    def toTarget(self):
        tx, ty = int(self.target.x), int(self.target.y)
        zx, zy = int(self.x), int(self.y)
        
        dx = tx - zx
        dy = ty - zy
            
        normal = (dx ** 2 + dy ** 2) ** 0.5
        if normal != 0:
            dx /= normal
            dy /= normal
             
        self.x += dx * gfw.frame_time * Item.Speed
        self.y += dy * gfw.frame_time * Item.Speed
            
    
    def setTarget(self, target):
        if self.target is None:
            self.target = target
            
    def deleteTarget(self):
        if self.target is not None:
           self.target = None
        
    def draw(self):
        pos = gfw.top().bg.to_screen(self.x, self.y)
        self.image.draw(*pos, 10, 10)
    
    def special_function(self):
        pass

class Coin(Item):
    def __init__(self, x, y):
        COIN_PATH = 'prop/Coin.png'
        super().__init__(COIN_PATH, x, y, Coin)

class Vaccine(Item):
    def __init__(self, x, y):
        VACCINE_PATH = 'prop/Vaccine.png'
        super().__init__(VACCINE_PATH, x, y, Vaccine)

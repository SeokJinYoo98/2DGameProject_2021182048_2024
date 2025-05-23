import gfw

class Item(gfw.Sprite):
    Speed = 350
    def __init__(self, fileName, x, y, Type):
        super().__init__(fileName, x, y)
        self.target = None
        self.Type = Type

    def update(self):
        if self.target is None: return
        self.toTarget()
        
    def toTarget(self):
        dx = int(self.target.x - self.x)
        dy = int(self.target.y - self.y)
            
        dist = (dx ** 2 + dy ** 2)
        if dist != 0:
            inv_dist = 1 / (dist ** 0.5)
            dx *= inv_dist
            dy *= inv_dist
             
        self.x += dx * gfw.frame_time * Item.Speed
        self.y += dy * gfw.frame_time * Item.Speed
            
    
    def setTarget(self, target):
        if self.target is None:
            self.target = target
            
    def deleteTarget(self):
        if self.target is not None:
           self.target = None
        
    def draw(self):
        pos = gfw.top().world.bg.to_screen(self.x, self.y)
        self.image.draw(*pos, 20, 20)
    
    def erase(self):
        world = gfw.top().world
        world.remove(self, world.layer.item)
    
    def special_Function(self, target):
        pass

class Coin(Item):
    SOUND = None
    def __init__(self, x, y):
        if Coin.SOUND is None:
            Coin.SOUND = gfw.sound.sfx('Coin.wav')
            Coin.SOUND.set_volume(100)
        COIN_PATH = 'prop/Coin.png'
        super().__init__(COIN_PATH, x, y, Coin)

    def special_Function(self, target):
        Coin.SOUND.play()
        target.Xp += 1
        #print(f'{target.Xp=}')
        self.erase()
        
class Vaccine(Item):
    SOUND = None
    def __init__(self, x, y):
        if Vaccine.SOUND is None:
            Vaccine.SOUND = gfw.sound.sfx('Vaccine.wav')
            Vaccine.SOUND.set_volume(300)
        VACCINE_PATH = 'prop/Vaccine.png'
        super().__init__(VACCINE_PATH, x, y, Vaccine)
    def special_Function(self, target):
        Vaccine.SOUND.play()
        if target.hp < target.maxHp and target.hp != 0:
            target.hp += 1
           # print(f'{target.hp=}')
        self.erase()    
class Magnetic(Item):
    SOUND = None
    def __init__(self, x, y):
        if Magnetic.SOUND is None:
            Magnetic.SOUND = gfw.sound.sfx('Magnetic.wav')
            Magnetic.SOUND.set_volume(30)
        MagneticPath = 'prop/Magnetic.png'
        super().__init__(MagneticPath, x, y, Magnetic)
    def special_Function(self, target):
        Magnetic.SOUND.play()
        target.magneticTime()
        self.erase()
        
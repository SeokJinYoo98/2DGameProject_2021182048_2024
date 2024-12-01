import gfw
import math

class Gun(gfw.Sprite):
    def __init__(self):        
        super().__init__('prop/Gun.png', 0, 0)
        self.angle = 0
        self._offset_x = 5
        self._offset_y = -6
        self.flip = ' '
        self.collType = False
        self.__fire_sound = gfw.sound.sfx('machine_gun.wav')
        self.__fire_sound.set_volume(70)
    def update(self):
        pass
    def draw(self):
        pass
    def draw_(self, flip, x, y):
        self.x, self.y = x + self._offset_x, y + self._offset_y
        info = self.angle, self.flip, self.x, self.y, self.width * 2, self.height * 2
        self.image.composite_draw(*info)
    def playSound(self):
        self.__fire_sound.play()
    def rotate(self, mouse_x, mouse_y, flip):
        self.angle = math.atan2(mouse_y - self.y, mouse_x - self.x)
        self._Flip(flip)
    
    def _Flip(self, flip):
        if flip == 'h':
            f = 'v'
            self._offset_x = -5
        else:
            f = ' '
            self._offset_x = 5
            
        self.flip = f

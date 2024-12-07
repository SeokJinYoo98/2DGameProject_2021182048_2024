import math
import gfw
class Bullet(gfw.Sprite):
    def __init__(self, x, y, angle, range, speed, flip, scale, pene):
        self._dist_travelled = 0
        self._range = range
        self._speed = speed
        self._angle = angle
        self._scale = scale
        self._dirX, self._dirY = math.cos(angle), math.sin(angle) 
        self._flip = flip
        self._penetration = pene
        super().__init__('prop/Bullet2.png', x + self._dirX * 30, y + self._dirY * 30)

        
    def update(self):
        if self.check_is_death(): self._erase()
            
        self.y += self._dirY * gfw.frame_time * self._speed
        self.x += self._dirX * gfw.frame_time * self._speed

        move_dist = self._speed * gfw.frame_time
        
        self._dist_travelled += move_dist
     
        if self._dist_travelled >= self._range:
           self._erase()
            
    def draw(self):
        pos = gfw.top().world.bg.to_screen(self.x, self.y)
        bulletInfo = self._angle, self._flip, *pos, self.width * self._scale, self.height * self._scale
        self.image.composite_draw(*bulletInfo)
    
    def _erase(self):
        self._dist_travelled = 0
        world = gfw.top().world
        world.remove(self, world.layer.bullet)
            
    def collide(self):
        self._penetration -= 1
        
    def get_bb(self):
        l = self.x - self.width // 3
        b = self.y - self.height // 2
        r = self.x + self.width // 3
        t = self.y + self.height // 2
        return l, b, r, t
            
    def check_is_death(self):
        if 0 < self._penetration:
            return False
        return True


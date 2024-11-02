import math
import gfw
class Bullet(gfw.Sprite):
    def __init__(self, x, y, angle, range, speed, flip):
        self._speed = speed # pixels per second
        self._dist_travelled = 0
        self._range = range
        self._speed = speed
        self._angle = angle
        self._dirX, self._dirY = math.cos(angle), math.sin(angle) 
        self._flip = flip
        super().__init__('prop/Bullet2.png', x + self._dirX * 30, y + self._dirY * 30)
        
    def update(self):
        self.y += self._dirY * gfw.frame_time * self._speed
        self.x += self._dirX * gfw.frame_time * self._speed
        
        move_dist = self._speed * gfw.frame_time
        
        self._dist_travelled += move_dist
        
        # 사거리만큼 이동했다면 지운다.
        if self._dist_travelled >= self._range:
           self._erase()
            
    def draw(self):
        bulletInfo = self._angle, self._flip, self.x, self.y, self.width * 2, self.height * 2
        self.image.composite_draw(*bulletInfo)
    
    def _erase(self):
            world = gfw.top().world
            world.remove(self, world.layer.bullet)
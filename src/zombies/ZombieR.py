from zombies import Zombie
import math
import gfw
class ZombieR(Zombie):
    Target = None
    BG = None
    Hp = 1
    Speed = 80
    ATTACK_COLLTIME = 1
    FRAMES = {
        'IDLE': [ 
            (0, 19, 19, 19)
        ],
        'WALK': [ 
            (0, 19, 19, 19), (19, 19, 19, 19)
        ],
        'HIT': [
            (38, 19, 19, 19)
        ],
        'DEAD': [
            (0, 0, 19, 19)
        ],
        'ATTACK': [
            (0, 19, 19, 19), (19, 19, 19, 19)
        ]
    }
    FRAME_INFO = {
        # Frame Index Count, fps
        'IDLE': (1, 1 / 2),
        'WALK': (2, 1 / 4),
        'HIT': (1, 1 / 2),
        'DEAD': (1, 1 / 2),
        'ATTACK': (2, 1 / 4)
    }
    
    def __init__(self, x, y):
        fileName = 'zombie/zombieR.png'
        super().__init__(fileName, x, y, ZombieR)
        self.special_Range = 400
        self.Attack_Time = 0
        
    def special_Function(self):
        if Zombie.Target is None: return
        px, py = Zombie.Target.x, Zombie.Target.y
    
        angle = math.atan2(py - self.y, px - self.x)
        dir_x = math.cos(angle)
        dir_y = math.sin(angle)
        dist = ((px - self.x) ** 2 + (py - self.y) ** 2) ** 0.5
        if dist <= self.special_Range - 100:
            self.__move_Back(dir_x, dir_y)
        
        self.__Attack(px, py, dir_x, dir_y)

    
    def __move_Back(self, dir_x, dir_y):
        self.x -= dir_x * gfw.frame_time * ZombieR.Speed
        self.y -= dir_y * gfw.frame_time * ZombieR.Speed
        
    def __Attack(self, px, py, dir_x, dir_y):
        if self.Attack_Time <= ZombieR.ATTACK_COLLTIME:
            self.Attack_Time += gfw.frame_time
            return
        b = zBullet(self.x + dir_x * 10, self.y + dir_y * 10, dir_x, dir_y)
        world = gfw.top().world
        world.append(b, world.layer.zbullet)
        self.Attack_Time = 0
    
class zBullet(gfw.Sprite):
    def __init__(self, x, y, dir_x, dir_y):
        super().__init__('prop/Bullet2_purple.png', x, y)
        self.__speed = 200
        self.__dist_travelled = 0
        self.__range = 600
        self.__dir_x = dir_x
        self.__dir_y = dir_y
        self.__penetration = 1
        
    def update(self):
        if self.__check_is_death(): self.__erase()
        self.x += self.__dir_x * self.__speed * gfw.frame_time
        self.y += self.__dir_y * self.__speed * gfw.frame_time
        self.__dist_travelled += self.__speed * gfw.frame_time
        if self.__dist_travelled >= self.__range:
           self.__erase()
           
    def draw(self):
        pos = gfw.top().world.bg.to_screen(self.x, self.y)
        self.image.draw(pos[0], pos[1], self.width * 3, self.height * 3)
        
    def __erase(self):
        world = gfw.top().world
        world.remove(self, world.layer.zbullet)
        
    def collide(self):
        self.__penetration -= 1
        
    def get_bb(self):
        l = self.x - self.width
        b = self.y - self.height
        r = self.x + self.width
        t = self.y + self.height
        return l, b, r, t
    
    def __check_is_death(self):
        if 0 < self.__penetration:
            return False
        return True
           
from zombies import Zombie
import math
import gfw
class ZombieR(Zombie):
    Hp = 1
    Speed = 100
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
        self.hit_Sound = gfw.sound.sfx('Range.wav')
        self.hit_Sound.set_volume(60)
        self.attack_Sound = gfw.sound.sfx('card.wav')
        self.attack_Sound.set_volume(60)
    def special_Function(self):
        target = Zombie.Target
        if target is None:
            return

        px, py = target.x, target.y
        dx, dy = target.x - self.x, target.y - self.y
        dist_squared = dx ** 2 + dy ** 2

        if dist_squared <= (self.special_Range - 100) ** 2:
            normal = dist_squared ** 0.5
            dir_x, dir_y = dx / normal, dy / normal
            self.__move_Back(dir_x, dir_y)
        else:
            angle = math.atan2(dy, dx)
            dir_x, dir_y = math.cos(angle), math.sin(angle)
            
        self.__Attack(px, py, dir_x, dir_y)

    def __move_Back(self, dir_x, dir_y):
        self.x -= dir_x * gfw.frame_time * ZombieR.Speed
        self.y -= dir_y * gfw.frame_time * ZombieR.Speed
        
    def __Attack(self, px, py, dir_x, dir_y):
        if self.Attack_Time <= ZombieR.ATTACK_COLLTIME:
            self.Attack_Time += gfw.frame_time
            return
        self.attack_Sound.play()
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
        self.__dist_travelled = 0
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
           